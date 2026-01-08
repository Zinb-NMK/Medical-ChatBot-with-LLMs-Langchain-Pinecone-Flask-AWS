from flask import Flask, render_template, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import system_prompt
import os
import re

# -------------------- ENV & CACHE --------------------
os.environ["HF_HOME"] = "E:/hf_cache"
os.environ["HUGGINGFACE_HUB_CACHE"] = "E:/hf_cache"

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# -------------------- FLASK APP --------------------
app = Flask(__name__)

rag_chain = None


# -------------------- QUERY NORMALIZATION --------------------
def normalize_query(text: str) -> str:
    corrections = {
        "feaver": "fever",
        "medictions": "medications",
        "medicines": "medications",
        "medicine": "medication",
        "causes": "causes",
        "cause": "causes"
    }

    words = re.findall(r"\w+", text.lower())
    corrected_words = [corrections.get(w, w) for w in words]
    return " ".join(corrected_words)


# -------------------- INIT RAG --------------------
def init_rag():
    global rag_chain

    print("Initializing RAG pipeline...")

    embeddings = download_embeddings()

    docsearch = PineconeVectorStore.from_existing_index(
        index_name="medical-chatbot",
        embedding=embeddings
    )

    retriever = docsearch.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    hf_pipeline = pipeline(
        task="text2text-generation",
        model="google/flan-t5-small",
        max_new_tokens=256,
        temperature=0.0,
        repetition_penalty=1.2,
        no_repeat_ngram_size=3,
        do_sample=False
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}")
        ]
    )

    qa_chain = create_stuff_documents_chain(llm, prompt)

    rag_chain = create_retrieval_chain(retriever, qa_chain)

    print("RAG pipeline initialized successfully ✅")


# -------------------- ROUTES --------------------
@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():
    global rag_chain

    user_input = request.form.get("msg", "").strip()

    # ---- Greeting handling ----
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    if user_input.lower() in greetings:
        return "Hello 👋 I’m your medical assistant. Please ask a medical question."

    # ---- Vague question guard ----
    vague_words = ["it", "this", "that", "they", "those", "these"]
    tokens = user_input.lower().split()

    if any(w in tokens for w in vague_words) and len(tokens) < 6:
        return (
            "Could you please clarify which medical condition you are referring to? "
            "For example: 'What is the treatment for fever?'"
        )

    # ---- Normalize spelling ----
    normalized_input = normalize_query(user_input)

    # ---- Query rewriting ----
    if "fever" in normalized_input and "cause" in normalized_input:
        normalized_input = "What are the causes and medications for fever?"

    if rag_chain is None:
        return "System is still starting. Please wait..."

    print("User:", user_input)
    print("Normalized:", normalized_input)

    response = rag_chain.invoke({"input": normalized_input})
    answer = response.get("answer", "Sorry, I could not find a relevant answer.")

    print("Bot:", answer)
    return answer


# -------------------- MAIN --------------------
if __name__ == "__main__":
    init_rag()
    app.run(host="127.0.0.1", port=5000, debug=False)
