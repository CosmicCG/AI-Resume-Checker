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
        
        prompt = f"""Please analyze this cover letter and provide constructive feedback.
        Focus on the following aspects:
        1. Customization - How specifically it targets the job/company
        2. Relevance - How well experience matches the position
        3. Evidence - Use of concrete examples and accomplishments
        4. Company Alignment - Understanding of and interest in the company
        5. Value Proposition - What the candidate brings to the employer
        6. Writing Quality	Grammar, clarity, tone, and professionalism
        7. Structure - Organization and logical flow
        8. Persuasiveness - Overall ability to convince the employer to interview the candidate
        9. Specific improvements specficially for {job_position if job_position else 'general job applications'}
        

        Cover Letter content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations."""

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert Cover Letter reviewer with years of experience in HR and recruitment."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")