import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os, io, requests, json

st.set_page_config(
    page_title=" Future AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── GALAXY THEME: Deep Purple + Violet + Pink ── */

/* Animated starfield background */
.stApp {
    background: linear-gradient(135deg, #0d0221 0%, #1a0533 30%, #0f0a2e 60%, #1e0535 100%);
    color: pink;
    min-height: 100vh;
}

/* Subtle star shimmer overlay */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image:
        radial-gradient(1px 1px at 10% 15%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 30% 40%, rgba(255,200,255,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 55% 20%, rgba(200,180,255,0.5) 0%, transparent 100%),
        radial-gradient(1px 1px at 75% 60%, rgba(255,255,255,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 90% 10%, rgba(255,150,255,0.5) 0%, transparent 100%),
        radial-gradient(1px 1px at 20% 80%, rgba(180,150,255,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 65% 85%, rgba(255,255,255,0.3) 0%, transparent 100%),
        radial-gradient(1px 1px at 45% 70%, rgba(255,200,255,0.4) 0%, transparent 100%);
    pointer-events: none;
    z-index: 0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #120428 0%, #1e0840 100%) !important;
    border-right: 1px solid #6d28d9 !important;
}
section[data-testid="stSidebar"] * { color: #d8b4fe !important; }
section[data-testid="stSidebar"] .stRadio label { color: #c4b5fd !important; }

/* Headings */
h1 { 
    color: red !important;
    background: yellow!important;
    -webkit-background-clip: text !important;
    background-clip: text !important;
    font-weight: 800 !important;
}
h2, h3 { color: green !important; }
p, label, .stMarkdown { color: #ddd6fe; }

/* Glowing button */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #7c3aed;
    padding: 11px;
    font-size: 15px;
    font-weight: 600;
    background: linear-gradient(135deg, #7c3aed, #db2777);
    color: white;
    transition: 0.3s;
    box-shadow: 0 0 15px rgba(167, 85, 247, 0.4);
}
.stButton > button:hover {
    background: linear-gradient(135deg, #6d28d9, #be185d);
    box-shadow: 0 0 25px rgba(167, 85, 247, 0.7);
    transform: scale(1.02);
}

/* Metric cards */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1e0a40, #2d0f5e);
    border-radius: 14px;
    padding: 16px;
    border: 1px solid #7c3aed;
    box-shadow: 0 0 12px rgba(124, 58, 237, 0.2);
}
[data-testid="metric-container"] * { color: #e9d5ff !important; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: #f0abfc !important; }

/* Inputs */
textarea, input {
    border-radius: 10px !important;
    background: #1e0a40 !important;
    color: #e9d5ff !important;
    border: 1px solid #7c3aed !important;
}
textarea:focus, input:focus {
    border-color: #f472b6 !important;
    box-shadow: 0 0 8px rgba(244, 114, 182, 0.4) !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: #1e0a40;
    padding: 14px;
    border-radius: 12px;
    border: 1px dashed #a855f7;
}

/* Cards */
.card {
    background: linear-gradient(135deg, #1a0533, #230d4a);
    padding: 18px 20px;
    border-radius: 14px;
    border: 1px solid #5b21b6;
    margin-bottom: 12px;
    color: #e8d5f5;
    box-shadow: 0 4px 15px rgba(91, 33, 182, 0.2);
    transition: box-shadow 0.2s;
}
.card:hover { box-shadow: 0 4px 25px rgba(168, 85, 247, 0.35); }
.card-green  { border-left: 4px solid #34d399 !important; }
.card-blue   { border-left: 4px solid #a855f7 !important; }
.card-amber  { border-left: 4px solid #fbbf24 !important; }
.card-red    { border-left: 4px solid #f87171 !important; }

/* Skill pills */
.skill-pill {
    display: inline-block;
    padding: 4px 13px;
    margin: 3px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 500;
}
.pill-have    { background: #064e3b; color: #6ee7b7; border: 1px solid #34d399; }
.pill-missing { background: #450a0a; color: #fca5a5; border: 1px solid #f87171; }
.pill-blue    { background: #3b0764; color: #e9d5ff; border: 1px solid #a855f7; }

/* Progress / steps */
.step-done { color: #34d399; font-weight: 600; }
.step-todo { color: #a78bfa; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: #1e0a40;
    border-radius: 12px;
    padding: 4px;
    border: 1px solid #5b21b6;
}
.stTabs [data-baseweb="tab"] { color: #c4b5fd !important; border-radius: 8px; }
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #db2777) !important;
    color: white !important;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(167, 85, 247, 0.5);
}

/* Expander */
.streamlit-expanderHeader {
    background: #1e0a40 !important;
    color: #d8b4fe !important;
    border-radius: 10px;
    border: 1px solid #5b21b6 !important;
}

/* Select / multiselect */
[data-baseweb="select"] { background: #1e0a40 !important; border-color: #7c3aed !important; }
[data-baseweb="select"] * { color: #e9d5ff !important; }

/* Dataframe */
.dataframe { background: #1e0a40 !important; color: #e8d5f5 !important; }
[data-testid="stDataFrame"] { border: 1px solid #5b21b6; border-radius: 10px; overflow:hidden; }

/* Success / warning / error / info boxes */
.stSuccess { background: #064e3b !important; border-color: #34d399 !important; color: #6ee7b7 !important; }
.stWarning { background: #451a03 !important; border-color: #fbbf24 !important; color: #fde68a !important; }
.stError   { background: #450a0a !important; border-color: #f87171 !important; color: #fca5a5 !important; }
.stInfo    { background: #1e1b4b !important; border-color: #818cf8 !important; color: #c7d2fe !important; }

/* Slider */
[data-testid="stSlider"] > div > div { background: #7c3aed !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #0d0221; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #7c3aed, #db2777);
    border-radius: 8px;
}

footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Imports ───────────────────────────────────────────────────────────────────
from modules.resume_parser       import parse_resume
from modules.ats_checker         import calculate_ats_score
from modules.skill_gap           import get_missing_skills, extract_skills
from modules.interview_assistant import generate_questions
from modules.career_recommender  import recommend_career
from modules.course_recommender  import recommend_courses
from modules.resume_feedback     import generate_resume_feedback
from modules.salary_predictor    import predict_salary
from modules.roadmap_generator   import generate_roadmap
from modules.report_generator    import generate_report
from modules.interview           import get_answer

# ── Session state ─────────────────────────────────────────────────────────────
for k, v in {
    "resume_text": "", "resume_skills": [], "missing_skills": [],
    "ats_score": None, "career_results": [], "course_results": [],
    "feedback": [], "jd_text": "", "analyzed": False,
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Helpers ───────────────────────────────────────────────────────────────────
def pills(skills, cls="pill-blue"):
    return "".join(f'<span class="skill-pill {cls}">{s.title()}</span>' for s in skills)

def gauge(score):
    c = "#22c55e" if score >= 70 else "#f59e0b" if score >= 40 else "#ef4444"
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={"suffix":"%","font":{"size":44,"color":c}},
        gauge={
            "axis":{"range":[0,100],"tickcolor":"#475569","tickfont":{"color":"#94a3b8"}},
            "bar":{"color":c,"thickness":0.25},
            "bgcolor":"#1e0a40",
            "steps":[
                {"range":[0,40],"color":"#2d1a1a"},
                {"range":[40,70],"color":"#2d2a0a"},
                {"range":[70,100],"color":"#0a2d1a"},
            ],
        },
        domain={"x":[0,1],"y":[0,1]},
    ))
    fig.update_layout(paper_bgcolor="rgba(13,2,33,0)", font_color="#e8d5f5",
                      height=240, margin=dict(t=10,b=10,l=20,r=20))
    return fig
def ask_claude_ai(question):
    """Call Groq API (free & fast) for AI-powered interview answers."""
    import os
 
    # 1. Try Streamlit secrets first
    api_key = None
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
 
    # 2. Fall back to environment variable
    if not api_key:
        api_key = os.environ.get("GROQ_API_KEY", "").strip()
 
    if not api_key:
        return (
            "Groq API key not set. Add it to `.streamlit/secrets.toml`:\n"
            "`GROQ_API_KEY = \"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\"`\n\n"
            "Get your FREE key at: https://console.groq.com"
        )
 
    try:
        resp = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 512,
                "messages": [{
                    "role": "user",
                    "content": (
                        f"You are an expert technical interview coach. "
                        f"Answer this interview question clearly and concisely for a job seeker:\n\n"
                        f"Q: {question}\n\n"
                        f"Give a direct, practical answer in 3-5 sentences."
                    )
                }]
            },
            timeout=20,
        )
        data = resp.json()
        return data["content"][0]["text"]
    except Exception as e:
        return f"AI answer unavailable: {str(e)}"

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='display:flex;align-items:center;gap:10px;padding-bottom:14px;
         border-bottom:1px solid #6d28d9;margin-bottom:14px'>
        <div style='width:40px;height:40px;background:linear-gradient(135deg,#7c3aed,#db2777);
             border-radius:10px;display:flex;align-items:center;justify-content:center;
             font-size:22px'>🤖</div>
        <div>
            <div style='font-weight:700;font-size:16px;color:#f1f5f9'>Future AI</div>
            <div style='font-size:11px;color:#c084fc'>Your Intelligent Career Assistant</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("nav", [
        "  Dashboard",
        "  Resume Analysis",
        "  Career Match",
        "  Skill Gap",
        "  Course Finder",
        "  Market & Salary",
        "  Roadmap",
        "  Interview Prep",
    ], label_visibility="collapsed")

    st.markdown("---")
    if st.session_state.analyzed:
        st.markdown(f"""
        <div style='background:#2d0f5e;border-radius:10px;padding:12px;font-size:12px'>
        <div style='color:#a78bfa;margin-bottom:6px'>Last Analysis</div>
        <div style='color:#f0abfc'>ATS: <b>{st.session_state.ats_score}%</b></div>
        <div style='color:#22c55e'>Skills: <b>{len(st.session_state.resume_skills)}</b> found</div>
        <div style='color:#ef4444'>Missing: <b>{len(st.session_state.missing_skills)}</b> skills</div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# DASHBOARD
# ══════════════════════════════════════════════════════════════════
if page == "  Dashboard":
    st.markdown("<h1 style='text-align:center'> Future AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#c084fc;margin-top:-8px;margin-bottom:24px'>Your intelligent career command center</p>", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("ATS Score",     f"{st.session_state.ats_score}%" if st.session_state.ats_score else "—")
    c2.metric("Skills Found",  len(st.session_state.resume_skills) or "—")
    c3.metric("Missing Skills",len(st.session_state.missing_skills) or "—")
    c4.metric("Top Role",      st.session_state.career_results[0]["Role"] if st.session_state.career_results else "—")

    st.markdown("---")
    st.markdown("### How to use Future AI")
    for icon, title, desc in [
        ("1","Resume Analysis",   "Upload your resume (PDF/DOCX) and paste a job description. Click **Analyze** to get your ATS score, skill match, and career fit."),
        ("2","Career Match",      "See which IT roles match your skills with percentage scores and gap breakdown per role."),
        ("3","Skill Gap",         "View exactly which skills you have vs. what the job needs — with visual charts."),
        ("4","Course Finder",     "Get personalised course recommendations to close your skill gaps."),
        ("5","Market & Salary",   "Explore salary projections and compare roles by experience level."),
        ("6","Roadmap",           "Get a step-by-step learning path to your target role with progress tracking."),
        ("7","Interview Prep",    "Practice questions from your skills OR ask any question — AI answers it instantly."),
    ]:
        st.markdown(f"""
        <div class='card card-blue'>
        <b>{icon}. {title}</b><br>
        <span style='color:#a78bfa;font-size:13px'>{desc}</span>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# RESUME ANALYSIS
# ══════════════════════════════════════════════════════════════════
elif page == "  Resume Analysis":
    st.markdown("## Resume Analysis")
    st.markdown("<p style='color:#c084fc'>Upload your resume + job description to get ATS score, skills, gaps & feedback.</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        uploaded = st.file_uploader("Upload Resume (PDF / DOCX / TXT)", type=["pdf","docx","txt"])
        jd       = st.text_area("Paste Job Description", height=180,
                                placeholder="Paste the full job description here…")
        go_btn   = st.button("Analyze Resume")

    with col2:
        if uploaded:
            try:
                preview = parse_resume(uploaded)
                uploaded.seek(0)
                with st.expander("Resume Preview", expanded=True):
                    st.text(preview[:2500])
            except Exception as e:
                st.error(f"Could not preview: {e}")

    if go_btn:
        if not uploaded or not jd.strip():
            st.error("Please upload a resume AND paste a job description.")
        else:
            with st.spinner("Analyzing your resume with AI…"):
                rt = parse_resume(uploaded)
                uploaded.seek(0)
                ats   = calculate_ats_score(rt, jd)
                rs, ms = get_missing_skills(rt, jd)
                cr    = recommend_career(rs)
                co    = recommend_courses(ms)
                fb    = generate_resume_feedback(rt)

                st.session_state.update({
                    "resume_text": rt, "ats_score": ats,
                    "resume_skills": rs, "missing_skills": ms,
                    "career_results": cr, "course_results": co,
                    "feedback": fb, "jd_text": jd, "analyzed": True,
                })
            st.success("Analysis complete! Explore results in the sidebar sections.")

    if st.session_state.analyzed:
        st.markdown("---")
        g, info = st.columns([1,1], gap="large")
        with g:
            st.markdown("#### ATS Match Score")
            st.plotly_chart(gauge(st.session_state.ats_score), use_container_width=True)
            score = st.session_state.ats_score
            if score >= 70:   st.success("Strong match! Great alignment with this role.")
            elif score >= 40: st.warning("Moderate match. Add missing keywords.")
            else:             st.error("Low match. Update your resume with key skills.")

        with info:
            st.markdown("#### Skills Detected in Resume")
            if st.session_state.resume_skills:
                st.markdown(pills(st.session_state.resume_skills, "pill-have"), unsafe_allow_html=True)
            else:
                st.warning("No skills detected. Make sure your resume text is readable and lists technologies like 'Python', 'SQL', 'React' etc. Try the **Skill Gap** page to check manually.")
                # Show a preview of extracted text for debugging
                if st.session_state.resume_text:
                    with st.expander("Show extracted resume text (first 500 chars)"):
                        st.text(st.session_state.resume_text[:500])

            st.markdown("#### Missing Skills (from Job Description)")
            if st.session_state.missing_skills:
                st.markdown(pills(st.session_state.missing_skills, "pill-missing"), unsafe_allow_html=True)
            else:
                jd = st.session_state.jd_text
                if not jd.strip():
                    st.info("No job description provided — go to **Skill Gap** page to check gaps by role.")
                else:
                    st.success("No missing skills — your resume covers everything in the JD!")

        st.markdown("---")
        st.markdown("#### Resume Feedback")
        for fb in st.session_state.feedback:
            st.markdown(f"<div class='card card-amber'>{fb}</div>", unsafe_allow_html=True)

        st.markdown("---")
        if st.button("Generate PDF Report"):
            pdf_path = "/tmp/career_report.pdf"
            generate_report(pdf_path, st.session_state.ats_score,
                            st.session_state.resume_skills,
                            st.session_state.missing_skills,
                            st.session_state.career_results)
            with open(pdf_path,"rb") as f:
                st.download_button("Download PDF", data=f,
                                   file_name="career_report.pdf", mime="application/pdf")

# ══════════════════════════════════════════════════════════════════
# CAREER MATCH
# ══════════════════════════════════════════════════════════════════
elif page == "  Career Match":
    st.markdown("## Career Match")
    st.markdown("<p style='color:#c084fc'>Roles ranked by how well your skills match their requirements.</p>", unsafe_allow_html=True)
    st.markdown("---")

    if not st.session_state.analyzed:
        st.info("Run **Resume Analysis** first to see your personalised career matches.")
    else:
        results = st.session_state.career_results

        # Bar chart
        roles  = [r["Role"]        for r in results]
        scores = [r["Match Score"] for r in results]
        colors = ["#22c55e" if s>=70 else "#f59e0b" if s>=40 else "#ef4444" for s in scores]

        fig = go.Figure(go.Bar(
            x=scores, y=roles, orientation="h",
            marker_color=colors,
            text=[f"{s}%" for s in scores],
            textposition="outside",
            textfont=dict(color="#ffffff"),
        ))
        fig.update_layout(
            paper_bgcolor="rgba(13,2,33,0)", plot_bgcolor="rgba(13,2,33,0)",
            font_color="#e8d5f5", height=300,
            xaxis=dict(range=[0,115], showgrid=False),
            yaxis=dict(autorange="reversed"),
            margin=dict(t=10,b=10,l=10,r=60),
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        medals = ["1st","2nd","3rd","4th","5th"]
        for i, r in enumerate(results):
            s     = r["Match Score"]
            color = "#22c55e" if s>=70 else "#f59e0b" if s>=40 else "#ef4444"
            cls   = "card-green" if s>=70 else "card-amber" if s>=40 else "card-red"
            matched_html  = pills(r["Matched Skills"],  "pill-have")    if r["Matched Skills"]  else "<span style='color:#c084fc'>None</span>"
            missing_html  = pills(r["Missing Skills"][:6], "pill-missing") if r["Missing Skills"]  else "<span style='color:#22c55e'>All covered</span>"
            st.markdown(f"""
            <div class='card {cls}'>
              <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:10px'>
                <b style='font-size:16px'>{medals[i]} {r["Role"]}</b>
                <span style='color:{color};font-size:20px;font-weight:700'>{s}%</span>
              </div>
              <div style='height:8px;background:#1e0a40;border-radius:4px;margin-bottom:12px'>
                <div style='width:{s}%;height:100%;background:{color};border-radius:4px'></div>
              </div>
              <div style='font-size:13px;margin-bottom:4px'><b style='color:#a78bfa'>You have:</b> {matched_html}</div>
              <div style='font-size:13px'><b style='color:#a78bfa'>You need:</b> {missing_html}</div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# SKILL GAP
# ══════════════════════════════════════════════════════════════════
elif page == "  Skill Gap":
    st.markdown("## Skill Gap Analysis")
    st.markdown("<p style='color:#c084fc'>See exactly what you have vs. what the job needs.</p>", unsafe_allow_html=True)
    st.markdown("---")

    if not st.session_state.analyzed:
        st.info("Run **Resume Analysis** first.")
    else:
        from modules.skill_gap import extract_skills, SKILLS_DB

        have = st.session_state.resume_skills

        # ── Mode selector: JD-based or Role-based gap ────────────────
        gap_mode = st.radio("Show missing skills based on:",
                            ["Job Description", "Target Role"],
                            horizontal=True)

        if gap_mode == "Job Description":
            jd = st.session_state.jd_text
            if jd.strip():
                jd_skills = extract_skills(jd)
                miss = [s for s in jd_skills if s not in have]
                source_label = "from Job Description"
            else:
                # Fallback: show top skills user is missing from full database sample
                top_skills = ["python","sql","git","docker","aws","react",
                              "javascript","machine learning","postgresql","linux",
                              "typescript","kubernetes","tensorflow","power bi","tableau"]
                miss = [s for s in top_skills if s not in have]
                source_label = "suggested baseline (no JD provided)"
        else:
            # Role-based gap
            ROLE_SKILLS = {
                "Web Developer":            ["html","css","javascript","react","nodejs","mongodb","git","typescript"],
                "Python Developer":         ["python","sql","flask","django","git","pandas","numpy","postgresql"],
                "Data Analyst":             ["python","sql","pandas","excel","power bi","numpy","tableau","matplotlib"],
                "Machine Learning Engineer":["python","machine learning","pandas","numpy","sql","tensorflow","deep learning","docker"],
                "Backend Developer":        ["java","sql","nodejs","python","git","docker","postgresql","rest api"],
                "Full Stack Developer":     ["html","css","javascript","react","nodejs","sql","mongodb","git","docker"],
                "Data Scientist":           ["python","machine learning","pandas","sql","numpy","deep learning","tableau","scikit-learn"],
                "DevOps Engineer":          ["linux","docker","kubernetes","aws","git","python","terraform","ci/cd"],
            }
            role_pick = st.selectbox("Choose target role", list(ROLE_SKILLS.keys()))
            role_required = ROLE_SKILLS[role_pick]
            miss = [s for s in role_required if s not in have]
            source_label = f"for {role_pick}"

        total = len(have) + len(miss)
        coverage = round(len(have) / total * 100) if total > 0 else 0

        m1, m2, m3 = st.columns(3)
        m1.metric("Skills You Have",  len(have))
        m2.metric("Skills to Build",  len(miss))
        m3.metric("Coverage",         f"{coverage}%")

        st.markdown("---")
        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown(f"#### Skills Found in Resume ({len(have)})")
            if have:
                st.markdown(pills(have, "pill-have"), unsafe_allow_html=True)
            else:
                st.warning("No recognisable skills detected in your resume. Make sure your resume lists skills clearly (e.g. 'Python', 'SQL', 'React').")

        with c2:
            st.markdown(f"#### Missing Skills — {source_label} ({len(miss)})")
            if miss:
                st.markdown(pills(miss, "pill-missing"), unsafe_allow_html=True)
            else:
                st.success("You cover all required skills for this selection!")

        # Donut chart
        if have or miss:
            st.markdown("---")
            fig = go.Figure(go.Pie(
                labels=["Skills You Have", "Skills to Build"],
                values=[max(len(have), 0), max(len(miss), 0)],
                hole=0.65,
                marker_colors=["#34d399", "#f87171"],
                textinfo="percent+label",
                textfont=dict(color="#e8d5f5", size=13),
            ))
            fig.update_layout(
                paper_bgcolor="rgba(13,2,33,0)", font_color="#e8d5f5",
                height=320, margin=dict(t=10, b=10),
                annotations=[dict(
                    text=f"{coverage}%<br><span style='font-size:12px'>covered</span>",
                    x=0.5, y=0.5, font_size=18, font_color="#34d399", showarrow=False
                )],
            )
            st.plotly_chart(fig, use_container_width=True)

        # Live JD checker
        st.markdown("---")
        st.markdown("#### Live Skill Checker — Paste Any Job Description")
        custom_jd = st.text_area("Paste a job description below to instantly check your gaps",
                                  height=130, key="custom_jd",
                                  placeholder="e.g. We are looking for a Python developer with SQL, Docker and AWS experience…")
        if custom_jd.strip():
            jd_skills      = extract_skills(custom_jd)
            custom_have    = [s for s in jd_skills if s in have]
            custom_missing = [s for s in jd_skills if s not in have]
            if not jd_skills:
                st.warning("No recognisable tech skills found in this text. Try a more detailed job description with specific technologies.")
            else:
                cc1, cc2 = st.columns(2)
                with cc1:
                    st.markdown(f"**You already have ({len(custom_have)}):**")
                    st.markdown(pills(custom_have, "pill-have") if custom_have
                                else "<span style='color:#a78bfa'>None from this JD</span>",
                                unsafe_allow_html=True)
                with cc2:
                    st.markdown(f"**You need to learn ({len(custom_missing)}):**")
                    st.markdown(pills(custom_missing, "pill-missing") if custom_missing
                                else "<span style='color:#34d399'>All covered!</span>",
                                unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# COURSE FINDER
# ══════════════════════════════════════════════════════════════════
elif page == "  Course Finder":
    st.markdown("## Course Finder")
    st.markdown("<p style='color:#c084fc'>Curated courses to close your skill gaps fast.</p>", unsafe_allow_html=True)
    st.markdown("---")

    if not st.session_state.analyzed:
        st.info("Run **Resume Analysis** first.")
    else:
        from modules.course_recommender import recommend_courses, BUILTIN_COURSES

        tab1, tab2 = st.tabs(["For Your Gaps", "Browse All Courses"])

        with tab1:
            miss = st.session_state.missing_skills
            if not miss:
                st.success("No missing skills — no courses needed for this JD!")
            else:
                courses = recommend_courses(miss)
                if not courses:
                    # Show courses for missing skills from builtin
                    df_all = pd.DataFrame(BUILTIN_COURSES)
                    courses = df_all[df_all["Skill"].str.lower().isin([m.lower() for m in miss])].to_dict("records")

                level_filter = st.multiselect("Filter by level",
                    ["Beginner","Intermediate","Advanced"],
                    default=["Beginner","Intermediate","Advanced"])

                filtered = [c for c in courses if c["Level"] in level_filter]
                st.markdown(f"**{len(filtered)} courses found for your {len(miss)} missing skills:**")
                st.markdown("")

                lc = {"Beginner":"#22c55e","Intermediate":"#f59e0b","Advanced":"#ef4444"}
                cols = st.columns(2)
                for i, c in enumerate(filtered):
                    lvl   = c["Level"]
                    color = lc.get(lvl,"#38bdf8")
                    with cols[i % 2]:
                        st.markdown(f"""
                        <div class='card card-blue'>
                          <div style='display:flex;justify-content:space-between;align-items:start'>
                            <b style='font-size:14px'>{c["Course"]}</b>
                            <span style='background:{color};color:#000;padding:2px 10px;
                                  border-radius:20px;font-size:11px;font-weight:600;
                                  white-space:nowrap;margin-left:8px'>{lvl}</span>
                          </div>
                          <div style='color:#a78bfa;font-size:12px;margin-top:6px'>
                            Skill: <b style='color:#c084fc'>{c["Skill"]}</b>
                          </div>
                        </div>""", unsafe_allow_html=True)

        with tab2:
            df_all = pd.DataFrame(BUILTIN_COURSES)
            search = st.text_input("Search courses or skills", placeholder="e.g. Python, SQL, React…")
            level2 = st.multiselect("Level", ["Beginner","Intermediate","Advanced"],
                                    default=["Beginner","Intermediate","Advanced"], key="browse_level")
            filtered2 = df_all[df_all["Level"].isin(level2)]
            if search:
                filtered2 = filtered2[
                    filtered2["Skill"].str.lower().str.contains(search.lower()) |
                    filtered2["Course"].str.lower().str.contains(search.lower())
                ]
            st.markdown(f"**{len(filtered2)} courses**")
            st.dataframe(filtered2.reset_index(drop=True),
                         use_container_width=True, height=420)

# ══════════════════════════════════════════════════════════════════
# MARKET & SALARY
# ══════════════════════════════════════════════════════════════════
elif page == "  Market & Salary":
    st.markdown("## Market Trends & Salary Insights")
    st.markdown("<p style='color:#c084fc'>Explore salary projections across roles and experience levels.</p>", unsafe_allow_html=True)
    st.markdown("---")

    ROLES = ["Web Developer","Python Developer","Data Analyst","Machine Learning Engineer"]

    col_sel, col_exp = st.columns([2,1])
    with col_sel:
        selected_role = st.selectbox("Target Role", ROLES)
    with col_exp:
        experience = st.slider("Years of Experience", 0, 10, 2)

    salary = predict_salary(selected_role, experience)

    if salary:
        s1,s2,s3 = st.columns(3)
        s1.metric("Estimated Salary", f"Rs.{salary:,}/yr")
        s2.metric("Role",             selected_role)
        s3.metric("Experience",       f"{experience} yrs")

    st.markdown("---")

    # Growth curve
    st.markdown("#### Salary Growth Curve")
    exp_vals = list(range(11))
    sal_vals = [predict_salary(selected_role, e) or 0 for e in exp_vals]
    fig_line = px.area(x=exp_vals, y=sal_vals,
                        labels={"x":"Years of Experience","y":"Salary (Rs.)"},
                        color_discrete_sequence=["#38bdf8"])
    fig_line.update_traces(line_color="#a855f7", fillcolor="rgba(168,85,247,0.15)")
    fig_line.update_layout(paper_bgcolor="rgba(13,2,33,0)", plot_bgcolor="rgba(13,2,33,0)",
                           font_color="#e8d5f5", height=300,
                           margin=dict(t=10,b=10),
                           xaxis=dict(showgrid=False),
                           yaxis=dict(showgrid=True, gridcolor="#1e293b"))
    st.plotly_chart(fig_line, use_container_width=True)

    # All roles comparison
    st.markdown("---")
    st.markdown(f"#### All Roles at {experience} Years Experience")
    cmp = [{"Role":r,"Salary":predict_salary(r,experience) or 0} for r in ROLES]
    df_cmp = pd.DataFrame(cmp).sort_values("Salary", ascending=False)
    fig_bar = px.bar(df_cmp, x="Role", y="Salary",
                     color="Salary", color_continuous_scale="Purples",
                     text=[f"Rs.{s:,}" for s in df_cmp["Salary"]])
    fig_bar.update_traces(textposition="outside", textfont_color="#e8d5f5")
    fig_bar.update_layout(paper_bgcolor="rgba(13,2,33,0)", plot_bgcolor="rgba(13,2,33,0)",
                          font_color="#e8d5f5", coloraxis_showscale=False,
                          height=320, margin=dict(t=30,b=10),
                          xaxis=dict(showgrid=False),
                          yaxis=dict(showgrid=True, gridcolor="#1e293b"))
    st.plotly_chart(fig_bar, use_container_width=True)

    # Skills in demand table
    st.markdown("---")
    st.markdown("#### Most In-Demand Skills (2024–25)")
    demand_data = {
        "Skill":["Python","Machine Learning","SQL","React","AWS","Docker",
                 "Deep Learning","Kubernetes","TensorFlow","Power BI"],
        "Demand (%)": [92, 87, 84, 78, 75, 70, 68, 62, 60, 58],
        "Avg Salary (Rs./yr)": ["18L","24L","14L","16L","22L","20L",
                               "26L","23L","25L","13L"],
        "Trend": ["Up","Up","Stable","Up","Up","Up","Up","Up","Stable","Stable"],
    }
    st.dataframe(pd.DataFrame(demand_data), use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════
# ROADMAP
# ══════════════════════════════════════════════════════════════════
elif page == "  Roadmap":
    st.markdown("## Learning Roadmap")
    st.markdown("<p style='color:#c084fc'>Step-by-step path from your current skills to role readiness.</p>", unsafe_allow_html=True)
    st.markdown("---")

    ROLES = ["Web Developer","Python Developer","Data Analyst","Machine Learning Engineer"]
    selected_role = st.selectbox("Select Your Target Role", ROLES)
    roadmap = generate_roadmap(selected_role)

    my_skills = [s.lower() for s in st.session_state.resume_skills]

    if roadmap and roadmap[0] != "Roadmap Not Available":
        done   = [s for s in roadmap if s.lower() in my_skills]
        todo   = [s for s in roadmap if s.lower() not in my_skills]
        pct    = round(len(done)/len(roadmap)*100) if roadmap else 0

        m1,m2,m3,m4 = st.columns(4)
        m1.metric("Total Steps",   len(roadmap))
        m2.metric("Completed",     len(done))
        m3.metric("Remaining",     len(todo))
        m4.metric("Readiness",     f"{pct}%")

        # Progress bar
        st.markdown(f"""
        <div style='margin:16px 0 4px;color:#a78bfa;font-size:13px'>Overall Progress — {pct}%</div>
        <div style='height:10px;background:#2d0f5e;border-radius:6px;margin-bottom:20px'>
          <div style='width:{pct}%;height:100%;background:linear-gradient(90deg,#7c3aed,#f472b6);
               border-radius:6px;transition:width 0.5s'></div>
        </div>""", unsafe_allow_html=True)

        st.markdown("---")
        for i, step in enumerate(roadmap, 1):
            is_done = step.lower() in my_skills
            status  = "Completed" if is_done else "Up Next" if i==len(done)+1 else "Upcoming"
            color   = "#22c55e" if is_done else "#38bdf8" if i==len(done)+1 else "#475569"
            cls     = "card-green" if is_done else "card-blue" if i==len(done)+1 else ""
            st.markdown(f"""
            <div class='card {cls}' style='display:flex;align-items:center;gap:16px'>
              <div style='flex:1'>
                <b style='font-size:15px'>Step {i}: {step}</b>
                <span style='float:right;color:{color};font-size:13px;font-weight:600'>{status}</span>
              </div>
            </div>""", unsafe_allow_html=True)

        if todo:
            st.markdown("---")
            st.markdown("#### Next Steps — Recommended Courses")
            from modules.course_recommender import recommend_courses
            next_courses = recommend_courses(todo[:3])
            for c in next_courses[:4]:
                st.markdown(f"<div class='card card-blue'><b>{c['Course']}</b> &nbsp;·&nbsp; <span style='color:#a78bfa'>{c['Skill']} — {c['Level']}</span></div>",
                            unsafe_allow_html=True)
    else:
        st.warning("Roadmap not available for this role yet.")

# ══════════════════════════════════════════════════════════════════
# INTERVIEW PREP
# ══════════════════════════════════════════════════════════════════
elif page == "  Interview Prep":
    st.markdown("## Interview Preparation")
    st.markdown("<p style='color:#c084fc'>Practice questions from your skills + AI-powered instant answers.</p>", unsafe_allow_html=True)
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Practice Questions", "Ask AI Anything", "Q&A Database"])

    # ── Tab 1: Practice questions from skills ─────────────────────
    with tab1:
        if not st.session_state.resume_skills:
            st.info("Run **Resume Analysis** first to get skill-based questions.")
        else:
            st.markdown(f"**Questions generated from your skills:** {pills(st.session_state.resume_skills,'pill-blue')}", unsafe_allow_html=True)
            st.markdown("")
            questions = generate_questions(st.session_state.resume_skills)

            if questions:
                for i, q in enumerate(questions, 1):
                    with st.expander(f"Q{i}. {q}"):
                        # Try CSV first, then AI
                        csv_ans = get_answer(q)
                        if csv_ans:
                            st.markdown(f"**Answer:** {csv_ans}")
                        else:
                            with st.spinner("Getting AI answer…"):
                                ai_ans = ask_claude_ai(q)
                            st.markdown(f"**AI Answer:** {ai_ans}")
            else:
                st.warning("No practice questions found for your current skills.")

        # Extra: pick skill manually
        st.markdown("---")
        st.markdown("#### Practice by Skill")
        from modules.interview_assistant import question_bank
        skill_pick = st.selectbox("Choose a skill to practice", list(question_bank.keys()))
        if skill_pick:
            for i, q in enumerate(question_bank[skill_pick], 1):
                with st.expander(f"Q{i}. {q}"):
                    csv_ans = get_answer(q)
                    if csv_ans:
                        st.markdown(f"**Answer:** {csv_ans}")
                    else:
                        if st.button(f"Get AI Answer", key=f"ai_{skill_pick}_{i}"):
                            with st.spinner("Asking AI…"):
                                st.markdown(f"**AI Answer:** {ask_claude_ai(q)}")

    # ── Tab 2: Ask AI anything ────────────────────────────────────
    with tab2:
        st.markdown("### Ask Any Interview Question — AI Answers Instantly")
        st.markdown("<p style='color:#c084fc'>Powered by Claude AI. Ask any technical or HR interview question.</p>", unsafe_allow_html=True)

        if "ai_chat" not in st.session_state:
            st.session_state.ai_chat = []

        user_q = st.text_input("Type your question…",
                               placeholder="e.g. What is a REST API? / How to answer 'tell me about yourself'?",
                               key="ai_q_input")

        col_ask, col_clear = st.columns([3,1])
        with col_ask:
            ask_btn = st.button("Get AI Answer", use_container_width=True)
        with col_clear:
            if st.button("Clear", use_container_width=True):
                st.session_state.ai_chat = []
                st.rerun()

        if ask_btn and user_q.strip():
            # Check CSV first
            csv_ans = get_answer(user_q.strip())
            if csv_ans:
                answer = f"(From knowledge base) {csv_ans}"
            else:
                with st.spinner("AI is thinking…"):
                    answer = ask_claude_ai(user_q.strip())
            st.session_state.ai_chat.append({"q": user_q.strip(), "a": answer})

        # Show chat history
        for item in reversed(st.session_state.ai_chat):
            st.markdown(f"""
            <div class='card card-blue' style='margin-bottom:8px'>
              <div style='color:#f0abfc;font-weight:600;margin-bottom:6px'>{item["q"]}</div>
              <div style='color:#e2e8f0;font-size:14px;line-height:1.6'>{item["a"]}</div>
            </div>""", unsafe_allow_html=True)

    # ── Tab 3: Browse Q&A database ────────────────────────────────
    with tab3:
        st.markdown("### Browse Q&A Knowledge Base")
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            df_qa = pd.read_csv(os.path.join(base_dir,"data","interview_questions.csv"))
            skills_list = ["All"] + sorted(df_qa["Skill"].unique().tolist())
            skill_filter = st.selectbox("Filter by Skill", skills_list)
            search_q     = st.text_input("Search questions", placeholder="e.g. decorator, JOIN…")

            df_show = df_qa.copy()
            if skill_filter != "All":
                df_show = df_show[df_show["Skill"] == skill_filter]
            if search_q:
                df_show = df_show[
                    df_show["Question"].str.lower().str.contains(search_q.lower()) |
                    df_show["Answer"].str.lower().str.contains(search_q.lower())
                ]

            st.markdown(f"**{len(df_show)} questions found**")
            for _, row in df_show.iterrows():
                with st.expander(f"{row['Question']}"):
                    st.markdown(f"**{row['Answer']}**")
        except Exception as e:
            st.error(f"Could not load Q&A database: {e}")