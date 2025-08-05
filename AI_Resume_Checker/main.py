import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#Configures page to make it look nice
st.set_page_config(page_title="AI Resume Checker", page_icon="📄", layout="centered")

#Writing title and text onto the page
st.title("AI Resume Checker")
st.markdown("Upload your resume and get AI-powered feedback designed to help you create a stronger resume.")

#Loading API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#File uploader and text input
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targetting (optional)")

#A button
analyze = st.button("Analyze Resume")

#Takes in pdf file
def extract_text_from_pdf(pdf_file):
    #loades in pdf file using pyPDF2
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    #Adding text from pdf to text variable
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

#loading text from pdf or txt file
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        #Converting read information into byte object which is then loaded by pdf reader
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

#If the button was pressed and a file was uploaded
if analyze and uploaded_file:
    try:
        #Loading text from the file
        file_content = extract_text_from_file(uploaded_file)

        #if file is empty
        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()
        
        #prompt for LLM to analyze resume
        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific reccomendations."""

        #Creating OpenAI Client
        client = OpenAI(api_key=OPENAI_API_KEY)

        #Generating response from the LLM by specifying the model and messages
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment." },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        #Printing out the response
        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)
    
    except Exception as e:
        st.error(f"AN error occured: {str(e)}")

        