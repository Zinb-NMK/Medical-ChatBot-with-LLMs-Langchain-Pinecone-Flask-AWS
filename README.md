# 🩺 Build a Complete Medical Chatbot using LLMs, LangChain, Pinecone & Flask

This project is a **Retrieval-Augmented Generation (RAG) based Medical Chatbot** built using **LangChain**, **Pinecone**, **Flask**, and **Hugging Face LLMs (FLAN-T5)**.

The chatbot allows users to ask **medical-related questions**, retrieves relevant context from indexed medical documents stored in Pinecone, and generates **concise, factual answers** using a local Hugging Face model.

---

## 📘 Documentation Status

> ⚠️ **Note:** This README is currently undergoing **minor updates** to improve clarity, structure, and accuracy.

✔️ **Project Functionality:** Complete & Stable  
🛠️ **Documentation:** Small refinements in progress  
🚀 **Application Status:** Fully operational  

---

### 🔍 Purpose of Update
• Improve readability and formatting  
• Reflect recent enhancements  
• Align with industry documentation standards  

---

### ⏳ Current Status Summary
🔹 Codebase: **Finalized**  
🔹 Backend & Frontend: **Working as expected**  
🔹 Documentation: **Being polished**  

---

🙏 Thank you for your patience.

----

## 🚀 Features

- Medical Question Answering using **RAG architecture**
- Semantic search with **Pinecone Vector Database**
- Local **Hugging Face FLAN-T5** model (no OpenAI dependency)
- Flask-based web interface
- Handles spelling mistakes and vague queries
- Prevents repetitive or hallucinated answers
- Lightweight and CPU-friendly setup

---

## 🧠 Architecture Overview

1. Medical documents are converted into embeddings
2. Embeddings are stored in **Pinecone**
3. User question is embedded and matched against stored vectors
4. Relevant context is retrieved
5. LLM generates an answer **only using retrieved context**

---

## 🛠️ Tech Stack Used

- Python 3.10
- LangChain
- Pinecone
- Flask
- Hugging Face Transformers (FLAN-T5)
- HTML, CSS (Frontend)

---

## 📂 Project Structure

```text
├── app.py                  # Flask application
├── store_index.py          # Stores document embeddings in Pinecone
├── src/
│   ├── helper.py           # PDF loading & embeddings
│   └── prompt.py           # System prompt
├── templates/
│   └── chat.html           # Frontend UI
├── static/
│   └── style.css           # UI styling
├── .env                    # Environment variables
├── requirements.txt
└── README.md


### ⚙️ How to Run the Project

**STEP 01: Clone the Repository**
git clone https://github.com/Zinb-NMK/Medical-ChatBot-with-LLMs-Langchain-Pinecone-Flask-AWS.git  
cd Medical-ChatBot-with-LLMs-Langchain-Pinecone-Flask-AWS

**STEP 02: Create and Activate Conda Environment**
conda create -n medibot python=3.10 -y  
conda activate medibot

**STEP 03: Install Requirements**
pip install -r requirements.txt

**STEP 04: Setup Environment Variables**
Create a `.env` file in the root directory:
PINECONE_API_KEY=your_pinecone_api_key_here

**STEP 05: Store Embeddings in Pinecone**
python store_index.py  
(Loads medical documents → Creates embeddings → Stores in Pinecone)

**STEP 06: Run the Flask Application**
python app.py

**STEP 07: Open the Application**
http://127.0.0.1:5000

---

### 🧪 Example Questions
• What is diabetes?  
• What are the causes of fever?  
• Cough medications and prevention tips  
• What is acne?

---

### ⚠️ Important Notes
• Educational purpose only  
• No medical diagnosis  
• Always consult healthcare professionals  

---

### 🧹 Git Best Practices
• Large files ignored using `.gitignore`  
• Avoid `git add .`  
Use:
git add app.py src/ templates/ static/ .gitignore README.md

---

### 📌 Future Enhancements
• Conversation memory  
• Source citations  
• Improved medical coverage  
• Cloud deployment (AWS / Render)

---

### 👤 Author
Nagaram Manoj Kumar  
Aspiring AI/ML Engineer | Medical AI Enthusiast

⭐ If you like this project, give it a star!
