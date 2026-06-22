from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, ats_score, skills, missing_skills, careers):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("AI Career Intelligence Report", styles["Title"]))
    content.append(Spacer(1, 20))
    content.append(Paragraph(f"ATS Score: {ats_score}%", styles["BodyText"]))
    content.append(Paragraph(f"Skills: {', '.join(skills)}", styles["BodyText"]))
    content.append(Paragraph(f"Missing Skills: {', '.join(missing_skills)}", styles["BodyText"]))
    content.append(Paragraph("Career Recommendations", styles["Heading2"]))

    for career in careers:
        content.append(Paragraph(career["Role"], styles["BodyText"]))

    doc.build(content)
    return filename
