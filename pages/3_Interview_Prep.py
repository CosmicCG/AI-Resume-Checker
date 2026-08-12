import streamlit as st

st.set_page_config(
    page_title="AI Interview Prep",
    page_icon="🎤",
    layout="centered"
)

# Page title
st.title("🎤 AI Interview Prep")

st.markdown(
    """
    <div style="
        text-align: center;
        padding: 20px;
        color: #6b7280;
        font-size: 1.1rem;
    ">
        Practice smarter, prepare with confidence, and get AI-powered
        feedback tailored to the position you're pursuing.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Development notice
st.warning("🚧 **This Tool Is Currently In Development**")

st.markdown(
    """
    We're building an AI-powered interview preparation experience designed
    to help you practice realistic interview questions, improve your
    responses, and prepare for your next opportunity.
    """
)

st.markdown("### 🔮 Planned Features")

st.info(
    "**🎯 Job-Specific Questions**\n\n"
    "Generate interview questions based on the position and job description "
    "you're applying for."
)

st.info(
    "**🤖 AI-Powered Feedback**\n\n"
    "Receive feedback on your answers and identify areas where your responses "
    "can be improved."
)

st.info(
    "**📊 Interview Scoring**\n\n"
    "Get an overall evaluation of your responses to help track your "
    "interview readiness."
)

st.info(
    "**🔄 Practice & Improve**\n\n"
    "Practice repeatedly and refine your answers before your real interview."
)

st.divider()

if st.button("← Back to AI Career Center"):
    st.switch_page("app.py")