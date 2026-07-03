# AI Resume Screener

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![NLP](https://img.shields.io/badge/NLP-SpaCy-green)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-Embeddings-orange)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-purple)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

An **AI-powered Applicant Tracking System (ATS)** that automatically parses resumes, extracts structured information using NLP, generates semantic embeddings with Sentence Transformers, and ranks candidates against a Job Description using a **Hybrid AI Ranking Engine**.

---

# Features

- Resume Parsing (PDF & DOCX)
- Job Description Parsing (PDF, DOCX & TXT)
- NLP-based Information Extraction
- Skill Extraction
- Education Extraction
- Experience Extraction
-  Project Extraction
- Certification Extraction
- Semantic Resume Matching
- Sentence Transformer Embeddings
- FAISS Vector Search
- Hybrid AI Ranking
-  Streamlit Dashboard
- Export Candidate Ranking to CSV

-------------

# Project Architecture

```text
                    Resume (PDF/DOCX)
                            │
                            ▼
                    Resume Parser
                            │
                            ▼
                 Resume Information Extractor
                            │
                            ▼
                 Structured Resume JSON
                            │
                            ▼
                   Profile Builder
                            │
                            ▼
              SentenceTransformer Embedding
                            │
                            ▼
                     FAISS Vector Index
                            ▲
                            │
               Job Description (PDF/TXT)
                            │
                            ▼
                     Job Parser
                            │
                            ▼
                  Job Information Extractor
                            │
                            ▼
                   Job Profile Builder
                            │
                            ▼
               SentenceTransformer Embedding
                            │
                            ▼
                  Hybrid Ranking Engine
                            │
                            ▼
               Ranked Candidates + Scores
```

---

# Project Structure

```text
AI-Resume-Screener/

├── app/
│
├── builder/
├── embeddings/
├── extractor/
├── job/
├── parser/
├── preprocessing/
├── ranking/
├── services/
│
├── data/
│
│── jobs/
│── resumes/
│── output/
│── embeddings/
│
├── streamlit_app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# AI Pipeline

### Resume Processing

- Parse Resume
- Clean Text
- Extract:
  - Name
  - Email
  - Phone
  - Skills
  - Education
  - Experience
  - Projects
  - Certifications
- Build Structured JSON
- Generate Embedding

---

### Job Processing

- Parse Job Description
- Extract Skills
- Extract Education
- Extract Experience
- Build Job Profile
- Generate Embedding

---

### Candidate Ranking

The ranking engine combines multiple factors:

```
Final Score =
40% Semantic Similarity
35% Skill Match
15% Experience Match
10% Education Match
```

---

# Tech Stack

### Languages

- Python

### NLP

- spaCy

### Deep Learning

- Sentence Transformers
- Hugging Face Transformers
- PyTorch

### Vector Search

- FAISS

### Resume Parsing

- PyMuPDF
- python-docx

### Data Processing

- NumPy
- Pandas

### Web App

- Streamlit

---

# Screenshots



# Installation

Clone the repository

```bash
git clone https://github.com/PrathamShukla3102/AI-Resume-Screener.git

cd AI-Resume-Screener
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download spaCy model

```bash
python -m spacy download en_core_web_sm
```

---

# Run Application

Console Version

```bash
python main.py
```

Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

---

# Example Output

| Rank | Candidate | Final Score |
|------|-----------|------------:|
| 1 | Candidate A | 73.68 |
| 2 | Candidate B | 69.54 |
| 3 | Candidate C | 63.11 |

---

# Future Improvements

- LLM-based Resume Understanding
- OCR Support
- Resume Recommendation System
- Recruiter Authentication
- PostgreSQL Integration
- FastAPI Backend
- Docker Deployment
- AWS Deployment
- Resume Chatbot
- Multi-language Resume Support

