import pandas as pd

def load_skills(file_path):

    skills_df = pd.read_csv(file_path)

    skills = skills_df['skill'].tolist()

    return skills

def extract_skills(text, skills):

    found_skills = []

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills