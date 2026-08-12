import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configures page layout
st.set_page_config(page_title="AI Cover Letter Checker", page_icon="📄", layout="centered")

st.title("AI Cover Letter Checker")
st.markdown("Upload your Cover Letter and get AI-powered feedback designed to help you create a stronger resume.")

# Loading API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# File uploader and text input
uploaded_file = st.file_uploader("Upload your Cover Letter (PDF or TXT)", type=["pdf", "txt"])
job_position = st.text_input("Enter the job position details for the job you're targeting (optional)")

# A button
analyze = st.button("Analyze Cover LEtter")

# Takes in pdf file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Loading text from pdf or txt file
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# If the button was pressed and a file was uploaded
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()
        
        target_role = job_position if job_position else 'Software Engineering / General Roles'

        prompt = f"""You are an expert HR Executive and Tech Recruiter. Analyze the provided cover letter specifically for a **{target_role}** position.

Deliver your analysis strictly using the structured format below.

### 📊 Executive Scorecard
Provide a quick numerical score (1-10) for each area in a clean Markdown Table:
| Dimension | Score (1-10) | Key Status |
| :--- | :---: | :--- |
| Customization & Alignment | [Score] | [1-sentence status] |
| Relevance to {target_role} | [Score] | [1-sentence status] |
| Evidence & Metrics | [Score] | [1-sentence status] |
| Writing Quality & Structure | [Score] | [1-sentence status] |

---

### 🔑 Top Priority Fixes (Actionable Checklist)
List 3-4 critical changes the user should make immediately before submitting. Use bold bullet points.

---

### 📝 Detailed Category Breakdown
For each category below, provide:
- **Observation:** What is currently lacking or done well.
- **Action Step:** Exact instructions on how to fix it.
- **Example Rewrite:** A concrete before-and-after sentence suggestion tailored to the user's content.

1. **Targeting & Customization** (Company alignment, job title match)
2. **Technical Relevance & Impact** (Connecting projects like AI/ML or networking directly to {target_role})
3. **Quantifiable Evidence** (Transforming passive statements into metric-driven wins)
4. **Structure & Call to Action** (Opening hook and strong closing)

---

### 🎯 Role-Specific Recommendations ({target_role})
Provide 3 bullet points with direct advice on frameworks, methodologies, or technical tools that should be highlighted for this exact job.

Cover Letter Content:
{file_content}
"""

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a direct, highly analytical tech recruiter who provides concrete, formatted, and instantly actionable resume/cover letter reviews."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower temperature keeps outputs structured and consistent
            max_tokens=1200
        )

        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")