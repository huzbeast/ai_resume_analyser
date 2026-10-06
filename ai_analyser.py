import streamlit as st
from google import genai

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

Answer the user's question using ONLY the 
information provided in the resume context.

If the answer cannot be found in the context,
say that the resume does not provide enough 
information.

Resume context:
{context}

User question:
{question}

Answer:
"""
    try:

        response = client.models.generate_content(
            model=PRIMARY_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as primary_error:

        print("Primary model failed:")
        print(primary_error)

        try:
            response = client.models.generate_content(
                model=FALLBACK__MODEL,
                contents=prompt
            )

            return response.text

        except Exception as fallback_error:

            print("Fallvack model failed:")
            print(fallback_error)

            return(
                "I'm unable to analyze yout resume right now."
                "The AI service is temporarily unavailable."
                "Please try again in a few moments."
            )