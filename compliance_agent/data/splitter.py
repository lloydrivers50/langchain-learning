import logging
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

def split_documents(documents):
    if not documents:
        logger.warning("split_documents called with 0 documents")
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )

    chunked_docs = splitter.split_documents(documents)

    logger.info(f"Loaded {len(documents)} docs")
    logger.info(f"Chunked into {len(chunked_docs)} chunks")

    return chunked_docs
