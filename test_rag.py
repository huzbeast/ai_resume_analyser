from rag_engine import chunk_resume_text

sample_text = """
I built a machine learning project using Python. The project used Pandas and Scikit-learn.
I also  created a web application using Flask.
"""

chunks = chunk_resume_text(
    sample_text,
    chunk_size=10,
    overlap=2
)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}:")
    print(chunk)
    print()