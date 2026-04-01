import logging
import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

logger = logging.getLogger(__name__)
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")


def build_vector_store(chunks):
    if not chunks:
        logger.warning("build_vector_store called with 0 chunks")
        return None
   
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        client=chroma_client,
        collection_name="compliance_policies",
    )

    logger.info(f"Stored {len(chunks)} chunks in ChromaDB")

    return vector_store
