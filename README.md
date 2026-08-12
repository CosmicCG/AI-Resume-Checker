# AI Career Center

An AI-powered career toolkit built with **Streamlit** and **OpenAI GPT** to help job seekers improve their resumes, cover letters, and interview preparation.

## Current Features

- 📄 **AI Resume Checker** — Upload a resume and job description to receive AI-powered feedback, content analysis, and suggestions for improvement.
- ✉️ **AI Cover Letter Checker** — Analyze a cover letter against a target position and receive actionable feedback.
- 🎤 **AI Interview Prep** *(In Development)* — Generate position-specific interview questions, practice responses, and receive AI-powered feedback and scoring.

Built with **Streamlit** and managed with **uv** for Python dependency management.

---

## Requirements

Before running the application, make sure you have:

- **Python 3.10+**
- **uv** Python package manager
- **OpenAI API Key**
- A resume PDF file for testing
- A cover letter for testing

---

# Setup Instructions

## 1. Install uv

Follow the official installation instructions:

[https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

### Windows PATH Setup

Make sure the directory containing `uv.exe` is included in your system's `PATH`.

If `uv` isn't recognized after installation:

1. Press **Win + S**
2. Search for **Environment Variables**
3. Select **Edit the system environment variables**
4. Click **Environment Variables**
5. Under **User Variables**, select `Path`
6. Click **Edit**
7. Add the directory containing `uv.exe`

For example:

```text
C:\Users\yourname\.local\bin
