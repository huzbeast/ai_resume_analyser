import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skills, extract_skills

skills = load_skills("data\skill_dictionary.csv")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type = ["pdf","docx"]
)

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

    resume_text = extract_resume_text(uploaded_file) # raw text from uploaded file

    cleaned_text = clean_text(resume_text)

    found_skills = extract_skills(cleaned_text, skills)

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

    st.subheader("Detected Skills")

    if found_skills:

        for skill in found_skills:
            st.write("•", skill)
    else:
        st.write("No skills detected.")