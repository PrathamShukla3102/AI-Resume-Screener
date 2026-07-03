import os
import tempfile
import pandas as pd
import streamlit as st

from app.services.resume_service import ResumeService
from app.services.job_service import JobService
from app.services.ranking_service import RankingService


# ===========================================
# PAGE CONFIG
# ===========================================

st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide"
)

st.title("AI Resume Screener")


# ===========================================
# SERVICES
# ===========================================

resume_service = ResumeService()
job_service = JobService()
ranking_service = RankingService()


# ===========================================
# SIDEBAR
# ===========================================

st.sidebar.header("Upload Files")

job_file = st.sidebar.file_uploader(
    "Job Description",
    type=["pdf", "docx", "txt"]
)

resume_files = st.sidebar.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

top_k = st.sidebar.slider(
    "Top Candidates",
    1,
    20,
    5
)

rank_button = st.sidebar.button("🚀 Rank Candidates")


# ===========================================
# MAIN
# ===========================================

if rank_button:

    if job_file is None:

        st.error("Please upload a Job Description.")

        st.stop()

    if not resume_files:

        st.error("Please upload at least one resume.")

        st.stop()

    with st.spinner("Processing resumes..."):

        resumes = []

        temp_dir = tempfile.mkdtemp()

        # ----------------------------------
        # Save Job Description
        # ----------------------------------

        job_path = os.path.join(
            temp_dir,
            job_file.name
        )

        with open(job_path, "wb") as f:

            f.write(job_file.getbuffer())

        # ----------------------------------
        # Save Resumes
        # ----------------------------------

        for uploaded_resume in resume_files:

            resume_path = os.path.join(
                temp_dir,
                uploaded_resume.name
            )

            with open(resume_path, "wb") as f:

                f.write(uploaded_resume.getbuffer())

            resume = resume_service.process_resume(
                resume_path
            )

            resumes.append(resume)

        # ----------------------------------
        # Process Job
        # ----------------------------------

        job = job_service.process_job(
            job_path
        )

        # ----------------------------------
        # Ranking
        # ----------------------------------

        results = ranking_service.rank(

            resumes,

            job,

            top_k

        )

    st.success("Ranking Completed Successfully!")

    st.subheader("Job Profile")

    st.code(job["profile"])

    st.subheader("Candidate Ranking")

    table = []

    for i, r in enumerate(results, start=1):

        table.append({

            "Rank": i,

            "Candidate": r["candidate"],

            "Resume": r["resume"],

            "Final Score": r["final_score"],

            "Semantic": r["semantic"],

            "Skills": r["skill"],

            "Experience": r["experience"],

            "Education": r["education"]

        })

    df = pd.DataFrame(table)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Candidate Details")

    for r in results:

        with st.expander(
            f"{r['candidate']} ({r['final_score']:.2f})"
        ):

            col1, col2 = st.columns(2)

            with col1:

                st.write("### Matched Skills")

                for skill in r["matched_skills"]:

                    st.success(skill)

            with col2:

                st.write("### Missing Skills")

                for skill in r["missing_skills"]:

                    st.error(skill)

            st.metric(
                "Final Score",
                f"{r['final_score']:.2f}"
            )

            st.metric(
                "Semantic Score",
                f"{r['semantic']:.2f}"
            )

            st.metric(
                "Skill Score",
                f"{r['skill']:.2f}"
            )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Ranking CSV",

        csv,

        "candidate_ranking.csv",

        "text/csv"

    )
# ===========================================
# FOOTER
# ===========================================

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
    """
    <div style="
        text-align:center;
        padding:15px;
        font-size:16px;
        color:gray;
    ">
        Made with ❤️ by <span style="font-weight:bold;color:#4F46E5;">Hasslerzz</span>
    </div>
    """,
    unsafe_allow_html=True,
    )