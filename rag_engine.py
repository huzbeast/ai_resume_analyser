from ai_analyser import generate_resume_answer

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
    in a ChromaDB alongwith metadat.
    """

    # Create a collection to store the resume's information.
    collection = chroma_client.get_or_create_collection(
        name="resume_collection"
    )

    # Generate a unique ID for every chunk. 
    chunk_ids = [
        f"chunk_{i}" 
        for i in range(len(chunks))
    ]

    # Convert every chunk into a numerical embedding.
    embeddings = embedding_model.encode(chunks).tolist()

    # Store metadata about where each chunk came from in the resume.
    metadata = [
        {
            "chunk_number": i + 1,
            "source": "resume"
        }
        for i in range(len(chunks))
    ]
    
    # Store the chunks, their embeddings, and IDs in the collection.
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=chunk_ids,
        metadatas=metadata
    )

    return collection

def search_resume(collection, query, n_results=3):
    """
    Retrieve the most relevant resume chunks
    for a user's question.
    """

    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding, 
        n_results=n_results,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results

def build_resume_context(results):
    """
    Convert ChromaDB search results into a clean
    context string that can be sent to Gemini.
    """

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    context_parts = []

    for i, document in enumerate(documents):

        chunk_number = metadatas[i]["chunk_number"]
        distance = distances[i]

        context_parts.append(
            f"""
Resume Chunk {chunk_number}
Relevance distance: {distance:.4f}

{document}
"""
        )

    return "\n".join(context_parts)