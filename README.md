# 🤖 Future AI
## About the Project
Future AI is an AI-powered career guidance platform that helps students and job seekers analyze resumes, identify skill gaps, discover suitable career paths, find learning resources, and prepare for interviews. The platform provides ATS-based resume analysis, personalized recommendations, and career roadmaps to help users become industry-ready and make smarter career decisions.
##  Features & Enhancements

##  Resume Analysis
- Upload resumes in **PDF** and **DOCX** formats.
- AI-powered **ATS (Applicant Tracking System) scoring**.
- Semantic resume evaluation and keyword matching.
- Automatic **skill extraction** and resume summarization.
- Personalized suggestions to improve resume quality.
- Job description matching and career fit analysis.

---
##  Career Recommendation

- Recommends suitable career roles based on user skills.
- Calculates **match scores** for different job profiles.
- Provides role descriptions and required skills.
- Supports multiple IT domains, including:
  -  Web Development
  -  Data Science
  -  Artificial Intelligence
  -  Cyber Security
  -  Cloud Computing
  -  DevOps

---

##  Skill Gap Analysis

- Identifies missing skills for target job roles.
- Compares current skills with industry requirements.
- Generates a personalized upskilling plan.
- Highlights strengths and areas for improvement.

---

##  Course Finder

- Recommends relevant learning resources and certifications.
- Suggests beginner, intermediate, and advanced courses.
- Provides project-based learning recommendations.
- Supports platforms such as:
  -  YouTube
  -  Coursera
  -  Udemy
  -  NPTEL
  -  freeCodeCamp
  -  edX

---

## Market Trends & Insights

- Displays trending technologies and in-demand skills.
- Provides career growth and hiring insights.
- Shows emerging job opportunities.
- Helps users understand current industry requirements.

---

##  Personalized Roadmap

- Generates step-by-step learning paths.
- Provides milestone-based skill development plans.
- Recommends projects and certifications.
- Guides users from beginner to job-ready level.

---

##  Interview Preparation

- Technical interview question bank covering:
  - Programming
  -  Object-Oriented Programming (OOP)
  -  Database Management Systems (DBMS)
  -  Operating Systems (OS)
  -  Computer Networks (CN)
  -  Data Structures & Algorithms (DSA)
- Aptitude and reasoning practice.
- HR and behavioral interview questions.
- AI-powered interview guidance and preparation tips.

##  Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Groq API
- CSS
  ## 📂 Project Structure
```text
Future-AI/
│
├── app.py                    
├── requirements.txt          
├── README.md                 
│
├── data/
│   ├── IT_Job_Roles_Skills.csv    
│   ├── courses.csv               
│   └── market_trends.csv          
│
├── modules/
│   ├── resume_parser.py          
│   ├── resume_analyzer.py         
│   ├── career_recommender.py     
│   ├── skill_gap.py              
│   ├── course_finder.py          
│   ├── market_trends.py           
│   ├── roadmap_generator.py      
│   ├── interview_prep.py                  
├── assets/                
│   ├── style.css             
│               
│
└── .streamlit/
    └── secrets.toml               
```
## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │   User Uploads  │
                    │ Resume + Job JD │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Resume Parser   │
                    │ (PDF/DOCX)      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Skill Extraction│
                    │ & ATS Analysis  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Career          │
                    │ Recommendation  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Skill Gap       │
                    │ Analysis        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Course Finder   │
                    │ & Certifications│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Market Trends   │
                    │ & Insights      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Personalized    │
                    │ Roadmap         │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Interview       │
                    │ Preparation     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ 🤖 Future AI    │
                    │ Career Guidance │
                    │ Dashboard       │
                    └─────────────────┘
```
# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Future-AI.git
cd Future-AI
```

##  Create Virtual Environment

```bash
python -m venv .venv
```

###  Windows

```bash
.venv\Scripts\activate
```

###  Linux/Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Configure API Key

Create a `.streamlit/secrets.toml` file and add:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

---

## Run the Application
```bash
streamlit run app.py
```
After running the command, open your browser and navigate to:

```text
http://localhost:8501/
```

