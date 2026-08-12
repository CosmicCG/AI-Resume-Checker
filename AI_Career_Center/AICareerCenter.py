import streamlit as st


st.set_page_config(
    page_title="AI Career Center",
    page_icon="🎓",
    layout="wide"
)


# Custom CSS for styling the landing page
st.markdown("""
    <style>
    .hero-container {
        padding: 3rem 1rem;
        text-align: center;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 1rem;
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: #4b5563;
        max-width: 600px;
        margin: 0 auto;
    }

    .card {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    /* Make the entire card clickable without link styling */
    .card-link,
    .card-link:hover,
    .card-link:visited,
    .card-link:active {
        text-decoration: none !important;
        color: inherit !important;
        display: block;
        height: 100%;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.75rem;
    }

    .card-text {
        color: #6b7280;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }

    .card-action {
        margin-top: 1.5rem;
        font-weight: 600;
        color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)


# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🚀 Welcome to the AI Career Center</div>
        <div class="hero-subtitle">
            Your centralized hub for intelligent career tools, resume optimization,
            and application feedback.
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown("### 🛠️ Available Tools")
st.markdown("Select a tool below or use the sidebar navigation to get started.")


# Grid Layout for Tools
col1, col2 = st.columns(2, gap="large")

# Resume Checker Card
with col1:
    st.markdown("""
        <a href="/Resume_Checker" target="_self" class="card-link">
            <div class="card">
                <div class="card-title">📄 AI Resume Checker</div>
                <div class="card-text">
                    Upload your resume and target job description to get deep
                    AI-driven feedback, content clarity ratings, and actionable
                    enhancement strategies.
                </div>
                <div class="card-action">🚀 Open Resume Checker →</div>
            </div>
        </a>
    """, unsafe_allow_html=True)


# Cover Letter Checker Card
with col2:
    st.markdown("""
        <a href="/Cover_Letter_Checker" target="_self" class="card-link">
            <div class="card">
                <div class="card-title">✉️ AI Cover Letter Checker</div>
                <div class="card-text">
                    Upload your cover letter and provide the job description
                    to receive AI-driven feedback across multiple criteria,
                    along with actionable improvement strategies.
                </div>
                <div class="card-action">🚀 Open Cover Letter Checker →</div>
            </div>
        </a>
    """, unsafe_allow_html=True)


# Add spacing between rows
st.markdown("<br>", unsafe_allow_html=True)


# Interview Prep Card
col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("""
        <a href="/Interview_Prep" target="_self" class="card-link">
            <div class="card">
                <div class="card-title">🎤 AI Interview Prep <span style="color:#f59e0b; font-size:0.8rem;">(In Development)</span></div>
                <div class="card-text">
                    Enter the position you're interviewing for and provide
                    details about the job to generate likely interview
                    questions. Practice your responses and receive AI-powered
                    feedback and scoring to improve your interview performance.
                </div>
                <div class="card-action">🚀 Open Interview Prep →</div>
            </div>
        </a>
    """, unsafe_allow_html=True)
    
st.markdown("---")


# Quick Tips Section
with st.container():
    st.markdown("### 💡 Tips for Success")

    t1, t2, t3 = st.columns(3)

    t1.info(
        "**Tailor Your Resume**\n\n"
        "Always specify your target role or paste the exact job description "
        "for more precise feedback."
    )

    t2.success(
        "**Use PDF or TXT**\n\n"
        "Export your resume cleanly to ensure the text parser captures every "
        "detail accurately."
    )

    t3.warning(
        "**Iterate & Improve**\n\n"
        "Run your resume through multiple checks after making adjustments "
        "to track improvements."
    )