import re

def clean_text(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = text.strip()

    return text