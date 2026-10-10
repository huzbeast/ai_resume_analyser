from rag_engine import (
    chunk_resume_text,
    create_resume_collection,
    search_resume,
    build_resume_context
)

sample_text = """
I built a machine learning project using Python. 
The project used Pandas and Scikit-learn.

I cleaned the dataset by handling missing values 
and removing duplicate rows.

I also  created a web application using Flask.
the application allowed users to upload data and
view the results through a browser.

I have experience using SQL for querying databases.
I used SELECT, WHERE, GROUP BY and JOIN operations.
"""

sample_resume = """
Education:
Bachelor of Science in Physics.

Projects:
Built a machine learning project using Python,
Pandas and Scikit-learn. The project classified
data into different categories.

Web Development:
Created a Flask web application that allowed
users to upload documents and process them.

Database:
Used SQL queries including SELECT, WHERE,
GROUP BY and JOIN.
"""

chunks = chunk_resume_text(
    sample_resume,
    chunk_size=30,
    overlap=5
)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)

collection = create_resume_collection(chunks)

query = " what machine learning experience do I have?"

results = search_resume(
    collection,
    query,
    n_results=2
)

print("\n\nRetrieved chunks:")

for i, document in enumerate(results["documents"][0]):
    print(f"\nResult {i + 1}:")
    print(document)
    
    print(
        "Distance:",
        results["distances"][0][i]
    )

context = build_resume_context(results)

print("\n\nContext sent to AI:")
print(context)