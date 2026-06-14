# FutureAI
Future AI is an AI-powered career guidance platform that helps students and job seekers analyze resumes, identify skill gaps, discover learning paths, explore market trends, and prepare for interviews with personalized recommendations.
Project Structure:
Future-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── IT_Job_Roles_Skills.csv
│   ├── courses.csv
│   └── salary_data.csv
│
├── modules/
│   ├── resume_parser.py
│   ├── career_recommender.py
│   ├── skill_gap.py
│   ├── course_finder.py
│   ├── market_trends.py
│   ├── roadmap_generator.py
│   ├── interview_prep.py
│   └── ai_helper.py
│
└── .streamlit/
    └── secrets.toml
    
    Technologies Used
  Python,
     Streamlit	,
   Pandas	,
   NumPy	,
  PyPDF2	,
python-docx,
  Scikit-Learn	,
  Groq API	AI-Powered Responses,
  Plotly,
  Matplotlib	,
  css

     System Architecture:
     Resume Upload
      ↓
Resume Parser
      ↓
Skill Extraction
      ↓
ATS Analysis
      ↓
Career Recommendation
      ↓
Skill Gap Detection
      ↓
Course Recommendation
      ↓
Roadmap Generation
      ↓
Interview Preparation

    Create Virtual Environment
 python -m venv .venv
Windows
.venv\Scripts\activate
Linux/Mac
source .venv/bin/activate
          Install Dependencies
pip install -r requirements.txt
            Run Application
streamlit run app.py
