import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skills, extract_skills
from job_matcher import load_job_roles, convert_skills_to_list, calculate_match_scores
from roadmap_generator import generate_roadmap

skills = load_skills("data/skill_dictionary.csv")
job_roles = load_job_roles("data/job_roles.csv")
job_roles = convert_skills_to_list(job_roles)

st.title("AI Resume Analyzer")
st.write(
    "Upload your resume to analyse your skills,"
    "job-role mathches, missing skills, and learning roadmap."
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
    
    found_skills = extract_skills(cleaned_text, skills)

    if not found_skills:
        st.warning(
            "No recognized skills were detected. "
                   "Try uploading a resume containing technical skills"
                   "such as Python, Java, SQL, etc."
                   )
        st.stop()

    match_results = calculate_match_scores(found_skills, job_roles)

    st.subheader("Job Role Match comparison")

    chart_data = match_results.set_index("role")[["match_score"]]

    st.bar_chart(
        chart_data,
        y="match_score",
        y_label="Match Score (%)"
    )

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

    st.subheader("Job Role Match")

# Dispaying match scores for each job role
    for index in match_results.index:

        role = match_results.loc[index, "role"]
        score = match_results.loc[index, "match_score"]

        st.write(f'**{role}**')
        
        st.progress(int(score))

        st.write(f"Match Score: {score:.1f}%")

        st.divider()

    st.subheader("Top Recommended Roles")
    
    top_roles = match_results.sort_values(
        by="match_score",
        ascending=False
    ).head(3)

    for index in top_roles.index:

        role = top_roles.loc[index, "role"]
        score = top_roles.loc[index, "match_score"]

        st.write(f"**{role}** - {score:.1f}% match")    

    st.subheader("Missing Skills")

    for index in match_results.index:
        role = match_results.loc[index, "role"]
        missing_skills = match_results.loc[index, "missing_skills"]

        st.write(f'### {role}')

        if missing_skills:
            for skill in missing_skills:
                st.write("•", skill)
        else:
            st.write('No missing skills.')

    st.subheader("Learning Roadmap")
    
    for index in match_results.index:
        role = match_results.loc[index, "role"]
        missing_skills = match_results.loc[index, "missing_skills"]

        st.write(f'### {role}')

        if missing_skills:
            roadmap = generate_roadmap(missing_skills)

            for skill, steps in roadmap.items():
                st.write(f'**{skill.title()}**')
                for step in steps:
                    st.write("•", step)
        else:
            st.write("You already have the required skills!")

