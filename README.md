Resume Screening App

An AI-powered Resume Screening application that matches resumes against job descriptions using NLP and Semantic Similarity.
This project helps recruiters and HR teams quickly identify the best-fit candidates.

🔹 Features

Upload multiple resumes in .csv format

Paste or input a job description

Uses Sentence-Transformers with TensorFlow for semantic similarity

Calculates match scores between resumes and job descriptions

Built with Streamlit for an interactive web interface

🔹 Tech Stack

Python

Streamlit (for UI)

Sentence-Transformers (NLP embeddings)

Scikit-learn

Pandas, NumPy

🔹 Installation
Clone the repository:

git clone https://github.com/your-username/resume-screening.git
cd resume-screening


Create and activate a virtual environment:

python -m venv myvenv
# Windows
myvenv\Scripts\activate
# Mac/Linux
source myvenv/bin/activate


🔹 Usage

Run the Streamlit app:

streamlit run app.py


Upload resumes and enter a job description to get matching scores.

🔹 Sample Dataset

The repository includes sample resumes (resumes.csv) and a test job description.