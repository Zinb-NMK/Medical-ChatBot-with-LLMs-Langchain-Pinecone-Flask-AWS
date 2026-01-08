from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from typing import List
from langchain.schema import Document

# Load PDF files
def load_pdf_files(data):
    loader = DirectoryLoader(
        data, 
        glob="*.pdf", 
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents

# Filter to min
def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """G
    """

    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs

# Split the documents into smaller Chunks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap=20,
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk

# Download Embedding Model From HuggingFace
def download_embeddings():
    """
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedding = HuggingFaceBgeEmbeddings(
        model_name=model_name,
    ) 
    return embedding
embedding = download_embeddings()