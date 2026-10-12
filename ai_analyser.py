import streamlit as st
from google import genai
import time


PRIMARY_MODEL = "gemini-3.8-flash"
FALLBACK_MODEL = "gemini-3.5-flash-lite"

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

def generate_resume_answer(question, context):
    """
    Generate an answer using the resume context
    retrieved from ChromaDB.
    """

    prompt = f"""
    You are an AI resume analysis assistant.

    Answer the user's question using the resume contest below.
    Do not invent experience, skills, or qualifications.
    If the context does not contain enough information, 
    clearly say so.

    Resume context:
    {context}

    User question:
    {question}

    Answer:
    """
    for attempt in range(2):
        try:

            response = client.models.generate_content(
                model=PRIMARY_MODEL,
                contents=prompt
            )

            if response.text:
                return response.text

            print("Primart model returned an empty response.")

        except Exception as error:

            print(
                f"Primary model {attempt + 1} failed:"
                f"{type(error).__name__}: {error}"
            )
        # Wait before retrying except for the final attempt.
        if attempt == 0:
            time.sleep(2)

    # If both primary attempts fail, try the fallback model.
    try:
        response = client.models.generate_content(
            model=FALLBACK_MODEL,
            contents=prompt
        )

        if response.text:
            return response.text

        print("Fallback model returned an empty response.")

    except Exception as error:
        print(
            f"Fallback model failed: "
            f"{type(error).__name__}: {error}"
        )

        return(
            "I'm unable to generate an AI answer right now."
            "The AI service may be temporarily unavailable."
            "Please try again"
        )

def generate_resume_report(resume_text):
    """
    Analyze the complete resume and generate a structured report.
    """

    prompt = f"""
    You are a professional resume reviewer and career advisor.
    
    Analyze the resume below. Base your conclusions only on
    information supported by the resume.

    Do not invent skills, experience, qualifications, or achievements.
    A missing detail does not neccessarily mean the candidate lacks it.

    Return your analysis using these sections:

    ## 1. Resume Overview 
    Summarize the candidate's background and profile.

    ## 2. Key Strengths
    Identify demonstrated skills, projects, education, and experience.
    Explain why the strongest points are valuable.

    ## 3. Areas for Improvement
    Identify unclear descriptions, missing details, and weak presentation.
    Distinguish missing resume information from actual skill deficiencies.

    ## 4. Evidence from the Resume
    Give specific examples from the resume supporting your observaions.
    Reference project names or responsibilities where possible.
    Do not fabricate quotations or evidence.

    ## 5. Recommended Improvements
    Suggest practical, prioritized changes to improve the resume.

    ## 6. Skills to Develop
    Recommend relevant skills based on the candidate's background.
    Clearly distinguish new recommendations from demonstrated skills.

    ## 7. Overall Assessment
    Summarize the resume's strongest points and main opportunities
    for improvement. Do not assign an arbitrary numerical score.

    Be constructive, specific, and concise.

    RESUME:
    {resume_text}
    """

    for model in (PRIMARY_MODEL, FALLBACK_MODEL):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                return response.text

            print(f"{model} returned an empty response.")

        except Exception as error:
            print(
                f"Report generation failed with {model}: "
                f"{type(error).__name__}: {error}"
            )

    return (
        "The AI resume report could not be generated right now. "
        "Please try again shortly."    
    )

def analyze_job_match(resume_text, job_description):
    """
    Compare a resume with a specific job description.
    """

    prompt = f"""
    You are a professional career advisor.
    
    Compare the candidate's resume with the supplied job description.

    Rules:
    -Use only evidence found in the rsume for candidate claims.
    -Do not invent qualifications, evidence, or skills.
    -Distinguish a missing resume detail from a confirmed lack of skill. 
    -Treat the job description as the employer's requirements,
    not as facts anout the candidate.
    -Do not assign a numerical match score.
    -Be specific and constructive.

    Return these sections:

    ## 1. Role Overview
    Summarize the main responsibilities and requirements of the job.

    ## 2. Strongest Matches
    Identify requirements supported by resume evidence.
    Explain how the evidence relates to each requirement.

    ## 3. Partial Matches and Transferable Skills
    Identify related experience or skills that may transfer, 
    while explaining any limitations.

    ## 4. Requirements Without Resume Evidence
    List important requirements that the resume does not
    demonstrate. Do not assume the candidate lacks them. 

    ## 5. Resume Improvements for This Role 
    Recommend truthful, specific changes that improve 
    the resume's relevance to this job position.

    ## 6. Learning Priorities
    Recommend skills or knowledge areas to develop,
    prioritizing those most relevant to the role.

    ## 7. Overall Assessment
    Give a balanced qualitative assessment of the alignment
    between the resume and the job descripition.

    RESUME :
    {resume_text}

    JOB_DESCRIPTION:
    {job_description}
    """

    for model in (PRIMARY_MODEL, FALLBACK_MODEL):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text: return response.text

        except Exception as error:
            print(
            f"Job analysis failed with {model}: "
            f"{type(error).__name__}: {error}"
        )

    return (
        "Job-specific analysis could not be generated right now."
        "Please try again shortly."
    )