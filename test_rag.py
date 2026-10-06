from rag_engine import (
    chunk_resume_text,
    create_resume_collection,
    search_resume
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

chunks = chunk_resume_text(
    sample_text,
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
    