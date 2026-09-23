import pandas as pd 

def load_job_roles(file_path):
    job_roles_df = pd.read_csv(file_path)
    return job_roles_df

def convert_skills_to_list(job_roles_df):
    job_roles_df["required_skills"] = job_roles_df["required_skills"].apply(
        lambda skills: [skill.strip() for skill in skills.split(",")]
    )

    return job_roles_df

def calculate_match_scores(resume_skills, job_roles_df):
    match_results = []

    for index in job_roles_df.index:
         role = job_roles_df.loc[index, "role"]
         required_skills = job_roles_df.loc[index, "required_skills"]

         matched_skills = [skill for skill in required_skills if skill in resume_skills]
         missing_skills = [skill for skill in required_skills if skill not in resume_skills]
         matched_count = len(matched_skills)
         total_required = len(required_skills)
         match_score = (matched_count / total_required) * 100

         match_results.append({
             "role": role,
             "match_score": match_score,
             "matched_skills": matched_skills,
             "missing_skills": missing_skills
         })

    results_df = pd.DataFrame(match_results)

    return results_df

def find_missing_skills(resume_skills, required_skills):
    missing_skills = [skill for skill in required_skills if skill not in resume_skills]
    return missing_skills
