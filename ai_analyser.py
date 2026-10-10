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
            "Please try again shortly."
        )