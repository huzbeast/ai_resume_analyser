import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text

from rag_engine import chunk_resume_text, create_resume_collection, search_resume

from ai_analyser import generate_resume_answer

st.title("AI Resume Analyzer")

st.write(
    "Upload your resume to explore its contents and ask"
    "AI-powered questions about your skills, projects,"
    "education, and experience."
)

uploaded_file = st.file_uploader(
    "Upload your resume",
    type = ["pdf","docx"]
)

if uploaded_file is None:
    st.info("Please upload a PDF or DOCX resume to continue.")
    st.stop()



if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

    try:
        resume_text = extract_resume_text(uploaded_file) # raw text from uploaded file

    except Exception as e:
        st.error(f"Could not read the uploaded resume: {e}")
        st.stop()

    if not resume_text or not resume_text.strip():
        st.error( 
            "No readable text was found in this file. "
            "Please upload a text-based PDF or DOCX file."
        )
        st.stop()

    cleaned_text = clean_text(resume_text)

    chunks = chunk_resume_text(
        cleaned_text,
        chunk_size=100,
        overlap=20
    )

    st.info(
        f"Resume processed into {len(chunks)} knowledge chunks."
    )

    collection = create_resume_collection(chunks)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )

    st.subheader("Cleaned Resume Text")

    st.text_area(
        "Cleaned Content",
        cleaned_text,
        height=400
    )

    st.divider()
 
    st.subheader("Ask Questions About Your Resume")

    question = st.text_input(
        "Ask something about your resume:",
        placeholder="What are my strongest technical skills?"
    )

    if question:
        with st.spinner("Searching your resume..."):

            results = search_resume(
                collection,
                question,
                n_results=3
            )

            retrieved_chunks = results["documents"][0]

            context = "\n\n".join(retrieved_chunks)

        with st.spinner("Generating answer..."):

            answer = generate_resume_answer(
                question,
                context            
            )

        st.markdown('### AI Answer')

        st.write(answer)

        