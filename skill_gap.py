import re

SKILLS_DB = [
    # Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "php",
    "ruby", "scala", "kotlin", "swift", "r", "matlab", "go", "rust",
    # Web
    "html", "css", "react", "angular", "vue", "nodejs", "expressjs",
    "bootstrap", "tailwind", "graphql", "rest api", "flask", "django",
    "spring boot", "firebase", "next.js", "jquery",
    # Data / ML / AI
    "machine learning", "deep learning", "data science", "nlp",
    "computer vision", "tensorflow", "pytorch", "keras", "scikit-learn",
    "pandas", "numpy", "matplotlib", "seaborn", "opencv",
    # Data & BI
    "sql", "mysql", "postgresql", "mongodb", "redis", "sqlite",
    "power bi", "tableau", "excel", "hadoop", "spark", "hive",
    # Cloud & DevOps
    "aws", "azure", "google cloud", "docker", "kubernetes", "linux",
    "devops", "git", "github", "jenkins", "terraform", "ansible", "ci/cd",
    # Mobile
    "flutter", "android development", "react native", "ios development",
    # Other
    "cyber security", "networking", "blockchain", "figma", "unity",
    "selenium", "testing", "agile", "scrum",
]

# Sort by length descending so multi-word skills match before single words
SKILLS_DB = sorted(SKILLS_DB, key=len, reverse=True)


def extract_skills(text):
    """Extract skills from text using flexible matching."""
    text = text.lower()
    # Normalise common abbreviations
    text = text.replace("node.js", "nodejs").replace("node js", "nodejs")
    text = text.replace("next.js", "next.js")
    text = text.replace("scikit learn", "scikit-learn")
    text = text.replace("ci / cd", "ci/cd").replace("ci-cd", "ci/cd")
    text = text.replace("google cloud platform", "google cloud").replace("gcp", "google cloud")
    text = text.replace("microsoft azure", "azure")
    text = text.replace("amazon web services", "aws")
    text = text.replace("power bi", "power bi")
    text = text.replace("machine learning", "machine learning")

    found = set()
    for skill in SKILLS_DB:
        # Use word boundary for single-word skills, simple substring for multi-word
        if " " in skill or "-" in skill or "/" in skill:
            if skill in text:
                found.add(skill)
        else:
            pattern = r'(?<![a-z0-9])' + re.escape(skill) + r'(?![a-z0-9])'
            if re.search(pattern, text):
                found.add(skill)
    return list(found)


def get_missing_skills(resume_text, job_description):
    resume_skills = extract_skills(resume_text)

    # Extract from JD if provided
    if job_description and job_description.strip():
        jd_skills = extract_skills(job_description)
    else:
        jd_skills = []

    missing = [s for s in jd_skills if s not in resume_skills]

    # If JD has no detectable skills, show what the resume is missing
    # from a general full-stack baseline so the section is always useful
    if not jd_skills:
        baseline = ["python", "sql", "git", "docker", "aws", "react",
                    "javascript", "machine learning", "postgresql", "linux"]
        missing = [s for s in baseline if s not in resume_skills]

    return resume_skills, missing
