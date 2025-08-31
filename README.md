#  Resume Screening App  

An AI-powered **Resume Screening Application** built with **Streamlit** and **Sentence Transformers**.  
This project helps recruiters automatically match resumes against job descriptions and rank candidates based on relevance.  

🔗 **Live Demo:** [Click here to try the app](https://resume-screening-krsubtfuscdmwk8o2awp9b.streamlit.app/)  


---

##  Features
- Upload resumes in CSV format  
- Enter a job description to compare resumes  
- AI-based similarity scoring using **Sentence-BERT**  
- Ranks candidates by relevance to the job description  
- Simple and interactive UI with **Streamlit**  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **Streamlit** – Frontend app  
- **Sentence-Transformers** – Resume & job description embeddings  
- **Scikit-learn** – Cosine similarity  
- **Pandas, NumPy** – Data handling  


---

=======

##  Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>

2. **Create virtual environment**
    ```bash
    python -m venv myvenv
    source myvenv/bin/activate   # Mac/Linux  
    myvenv\Scripts\activate      # Windows

3. **Install dependencies**                                        
    ```bash
    pip install -r requirements.txt

4. **Run the app**
    ```bash
    streamlit run app.py

---

##  Sample Test

- Use the provided resumes.csv dataset.

- Example Job Description:
We are looking for a Data Scientist with experience in Python, Machine Learning,
and NLP to build predictive models and deploy AI solutions.

---

##  Demo
### After running the app, you’ll get:

- ✅ Resume ranking by similarity score
- ✅ Top candidates highlighted

---

##  Future Improvements
- Support for PDF/Docx resume uploads

- Advanced ranking with LLMs

- Dashboard for recruiters


  
