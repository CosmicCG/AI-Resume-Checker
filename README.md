# AI-Resume-Checker
A web app that uses AI (OpenAI GPT) to review and critique your resume for strengths, weaknesses, and improvements.

Built with Streamlit and managed with uv for Python dependency management.

Requirements:
Python
An Open API Key
A resume PDF file to test

Setup Instructions: 

1. Install uv
Follow Instructions Here: https://docs.astral.sh/uv/getting-started/installation/

Make sure the directory containing uv.exe is in your system's PATH.
If uv isn't recognized, fix it by:

Press Win + S → search “Environment Variables”

Under User Variables, edit Path

Add the path to the folder containing uv.exe (e.g. C:\Users\yourname\.local\bin)


2. Initialize Environment
Open your project in VS Code Terminal and run:
uv init .

3. Install Dependencies
In VS Code Terminal run:
uv add streamlit openai PyPDF2 python-dotenv

4. Add your OpenAI API Key
Create .env file in the root of your project with the line:
OPENAI_API_KEY=your-api-key

Run the App: 
uv run streamlit run main.py

or try Command: uv run python -m streamlit run main.py

