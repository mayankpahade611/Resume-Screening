import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Title
st.title("AI-Powered Resume Screening System")

# Upload resumes CSV
uploaded_file = st.file_uploader("Upload Resume Dataset (CSV)", type="csv")

if uploaded_file is not None:
    # Load dataset
    df = pd.read_csv(uploaded_file)
    st.write("### Sample Resumes Data", df.head())

    # Input job description
    job_description = st.text_area("Enter Job Description")

    if st.button("Rank Candidates"):
        if job_description.strip() != "":
            # TF-IDF
            vectorizer = TfidfVectorizer(stop_words="english")
            tfidf_matrix = vectorizer.fit_transform(df["Resume"] + " " + df["Skills"])

            # Transform job description
            jd_vector = vectorizer.transform([job_description])

            # Cosine similarity
            scores = cosine_similarity(jd_vector, tfidf_matrix).flatten()

            # Add scores to df
            df["Match Score"] = scores
            ranked_df = df.sort_values(by="Match Score", ascending=False)

            st.write("### Ranked Candidates", ranked_df[["Candidate Name", "Skills", "Match Score"]].head(10))
        else:
            st.warning("Please enter a job description first.")
