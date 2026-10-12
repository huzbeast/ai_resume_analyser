import streamlit as st

# Configure the page before creating other UI elements.
st.set_page_config(
    page_title="ResumeX",
    page_icon="📄",
    layout="wide"
)

#--- Header ---
st.title("📄 ResumeX")
st.caption("AI-powered career insights")

st.divider()

# --- Sidebar ---
with st.sidebar:
    st.header("Navigation")

    selected_page = st.radio(
        "Go to",
        ["Overview", "Resume", "Job Match", "AI Chat"]
    )

# --- Main Content ---
st.header("Analyze your resume")

st.write(
    "Upload your resume and optionally add a job description."
    "to recieve personalised career insights."
)

# Create two side-by-side columns.
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Your Resume")

    resume_file = st.file_uploader(
        "Upload a PDF or DOCX",
        type=["pdf", "docx"]
    )

with right_col:
    st.subheader("Target Job")

    job_description = st.text_area(
        "Job description (optional)",
        placeholder = "Paste the job requirements here...",
        height= 180
    )

st.divider()

#--- Action ---
if st.button("Analyse Resume", type="primary"):
    if resume_file is None:
        st.warning("Please upload your resume first.")
    else:
        st.success("Resume uploaded successflly")

st.caption(f"Current section: {selected_page}")