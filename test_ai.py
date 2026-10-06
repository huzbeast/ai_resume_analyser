from ai_analyser import generate_resume_answer
from pathlib import Path
from rag_engine import (
    chunk_resume_text,
    create_resume_collection,
    search_resume
)
from resume_parser import extract_resume_text

resume_path = Path("sample_resumes/Data_Analyst_Resume.pdf")

with open(resume_path, "rb") as file:
    resume_text = extract_resume_text(file)

print("Resume extracted successfully.")
# print("Characters:", len(resume_text))

chunks = chunk_resume_text(
    resume_text,
    chunk_size=100,
    overlap=20
)

print("Number of chunks:", len(chunks))

collection = create_resume_collection(chunks)

question = "What technical skills and projects are mentioned in this resume?"

results = search_resume(
    collection,
    question,
    n_results=3
)

retrieved_chunks = results["documents"][0]

context = "\n\n".join(retrieved_chunks)

answer = generate_resume_answer(
    question,
    context
)

print("\nAI Answer:")
print(answer)