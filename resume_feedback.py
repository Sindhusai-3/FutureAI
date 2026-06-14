def generate_resume_feedback(resume_text):
    feedback = []
    text = resume_text.lower()

    if len(resume_text) < 500:
        feedback.append("Resume content is too short. Add more details.")
    if "project" not in text:
        feedback.append("Add academic or personal projects.")
    if "skill" not in text:
        feedback.append("Include a dedicated Skills section.")
    if "internship" not in text and "experience" not in text:
        feedback.append("Add internships or experience if available.")
    if "certification" not in text:
        feedback.append("Add certifications to strengthen your profile.")
    if not feedback:
        feedback.append("Resume looks good. Minor improvements only.")

    return feedback
