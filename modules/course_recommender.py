import pandas as pd
import os

BUILTIN_COURSES = [
    {"Skill": "Python", "Course": "Python for Beginners", "Level": "Beginner"},
    {"Skill": "Python", "Course": "Advanced Python Programming", "Level": "Advanced"},
    {"Skill": "Machine Learning", "Course": "Machine Learning A-Z", "Level": "Intermediate"},
    {"Skill": "Machine Learning", "Course": "Advanced Machine Learning", "Level": "Advanced"},
    {"Skill": "SQL", "Course": "SQL Bootcamp", "Level": "Beginner"},
    {"Skill": "SQL", "Course": "Advanced SQL Queries", "Level": "Advanced"},
    {"Skill": "React", "Course": "React Complete Guide", "Level": "Intermediate"},
    {"Skill": "JavaScript", "Course": "JavaScript Essentials", "Level": "Beginner"},
    {"Skill": "HTML", "Course": "HTML5 Complete Course", "Level": "Beginner"},
    {"Skill": "CSS", "Course": "CSS3 Complete Course", "Level": "Beginner"},
    {"Skill": "NodeJS", "Course": "Node.js Complete Course", "Level": "Intermediate"},
    {"Skill": "MongoDB", "Course": "MongoDB Fundamentals", "Level": "Beginner"},
    {"Skill": "Docker", "Course": "Docker for Developers", "Level": "Intermediate"},
    {"Skill": "Git", "Course": "Git and GitHub Complete Guide", "Level": "Beginner"},
    {"Skill": "AWS", "Course": "AWS Cloud Practitioner", "Level": "Beginner"},
    {"Skill": "Deep Learning", "Course": "Deep Learning Fundamentals", "Level": "Intermediate"},
    {"Skill": "TensorFlow", "Course": "TensorFlow for Beginners", "Level": "Intermediate"},
    {"Skill": "Power BI", "Course": "Power BI Dashboard Development", "Level": "Beginner"},
    {"Skill": "Tableau", "Course": "Tableau Data Visualization", "Level": "Beginner"},
    {"Skill": "Excel", "Course": "Advanced Excel for Data Analysis", "Level": "Intermediate"},
    {"Skill": "Django", "Course": "Django Web Development", "Level": "Intermediate"},
    {"Skill": "Flask", "Course": "Flask Web Development", "Level": "Intermediate"},
]

def recommend_courses(skills):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "data", "courses.csv")
        df = pd.read_csv(csv_path, encoding="utf-8")
    except Exception:
        df = pd.DataFrame(BUILTIN_COURSES)

    recommendations = []
    for skill in skills:
        filtered = df[df["Skill"].str.lower() == skill.lower()]
        for _, row in filtered.iterrows():
            recommendations.append({
                "Skill": row["Skill"],
                "Course": row["Course"],
                "Level": row["Level"]
            })
    return recommendations
