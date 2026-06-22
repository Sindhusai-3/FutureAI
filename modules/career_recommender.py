import pandas as pd
import os

BUILTIN_CAREERS = [
    {"Role": "Web Developer",             "Skills": "html,css,javascript,react,nodejs,mongodb,git"},
    {"Role": "Python Developer",          "Skills": "python,sql,flask,django,git,pandas,numpy"},
    {"Role": "Data Analyst",              "Skills": "python,sql,pandas,excel,power bi,numpy,tableau"},
    {"Role": "Machine Learning Engineer", "Skills": "python,machine learning,pandas,numpy,sql,tensorflow,deep learning"},
    {"Role": "Backend Developer",         "Skills": "java,sql,nodejs,python,git,docker,postgresql"},
    {"Role": "Frontend Developer",        "Skills": "html,css,javascript,react,git"},
    {"Role": "Full Stack Developer",      "Skills": "html,css,javascript,react,nodejs,sql,mongodb,git"},
    {"Role": "Data Scientist",            "Skills": "python,machine learning,pandas,sql,numpy,deep learning,tableau"},
    {"Role": "DevOps Engineer",           "Skills": "linux,docker,kubernetes,aws,git,python,devops"},
    {"Role": "Cloud Engineer",            "Skills": "aws,azure,google cloud,linux,docker,kubernetes"},
    {"Role": "Android Developer",         "Skills": "java,android development,sql,git"},
    {"Role": "Flutter Developer",         "Skills": "flutter,sql,git"},
    {"Role": "Database Administrator",    "Skills": "sql,mysql,postgresql,mongodb,linux"},
]

def recommend_career(user_skills):
    # Always try CSV first, fall back to builtin
    careers_df = None
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "data", "IT_Job_Roles_Skills.csv")
        df = pd.read_csv(csv_path, encoding="utf-8")
        df.columns = [c.strip() for c in df.columns]
        role_col  = next((c for c in df.columns if "role"  in c.lower()), None)
        skill_col = next((c for c in df.columns if "skill" in c.lower()), None)
        if role_col and skill_col:
            df = df.rename(columns={role_col: "Role", skill_col: "Skills"})
            careers_df = df[["Role", "Skills"]].dropna()
    except Exception:
        pass

    if careers_df is None or careers_df.empty:
        careers_df = pd.DataFrame(BUILTIN_CAREERS)

    user_skills_lower = [s.strip().lower() for s in user_skills]
    recommendations = []

    for _, row in careers_df.iterrows():
        role = str(row["Role"]).strip()
        required = [s.strip().lower() for s in str(row["Skills"]).split(",") if s.strip()]
        if not required:
            continue
        matched = len(set(user_skills_lower) & set(required))
        score   = round(matched / len(required) * 100, 2)
        matched_list  = [s for s in required if s in user_skills_lower]
        missing_list  = [s for s in required if s not in user_skills_lower]
        recommendations.append({
            "Role": role,
            "Match Score": score,
            "Matched Skills": matched_list,
            "Missing Skills": missing_list,
            "Required": required,
        })

    return sorted(recommendations, key=lambda x: x["Match Score"], reverse=True)[:5]
