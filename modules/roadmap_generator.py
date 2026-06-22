def generate_roadmap(role):
    role = role.lower()
    roadmaps = {
        "web developer": ["HTML", "CSS", "JavaScript", "React", "NodeJS", "MongoDB", "Projects"],
        "python developer": ["Python Basics", "OOP", "File Handling", "Flask", "Django", "SQL", "Projects"],
        "data analyst": ["Python", "Pandas", "NumPy", "SQL", "Power BI", "Excel", "Projects"],
        "machine learning engineer": ["Python", "Statistics", "Pandas", "Machine Learning", "Deep Learning", "TensorFlow", "Projects"],
    }
    return roadmaps.get(role, ["Roadmap Not Available"])
