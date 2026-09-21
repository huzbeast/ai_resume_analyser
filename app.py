import streamlit as st
from resume_parser import extract_resume_text
st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type = ["pdf","docx"]
)

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

    resume_text = extract_resume_text(uploaded_file)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )