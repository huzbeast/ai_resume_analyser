from sentence_transformers import SentenceTransformer
import chromadb

# Load a pretrained embedding model.
# It converts text into numerical vectors that capture semantic meaning.
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create an in-memory ChromaDB client. 
# # For now, the database exists only while the program runs.
chroma_client = chromadb.Client()

def chunk_resume_text(text, chunk_size=500, overlap=100):
    """
    Split the resume into smaller overlapping chunks.

    chunk_size: Approximate number of words per chunk.
    overlap: Number of words shared between consecutive chunks.

    Overlap helps preserve context when a sentence or project 
    description crosses a chunk boundary.
    """

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        # Select a section of words for the current chunk.
        end = start + chunk_size
        chunk_words = words[start:end]

        # Convert the selected words back into text.
        chunk_text = " ".join(chunk_words)

        chunks.append(chunk_text)

        # Move forward while retaining some overlapping words.
        start += chunk_size - overlap

        return chunks

def create_resume_collection(chunks):
    """
    Convert resume chunks into embeddings and store them 
    in a ChromaDB collection.
    """

    # Create a collection to store the resume's information.
    collection = chroma_client.create_collection(name="resume_collection")

    # Generate a unique ID for each chunk. 
    chunk_ids = [str(i) for i in range(len(chunks))]

    # Convert every chunk into a numerical embedding.
    embeddings = embedding_model.encode(chunks).tolist()

    # Store the chunks, their embeddings, and IDs in the collection.
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=chunk_ids
    )

    return collection