import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from compliance_agent.state.schema import STATE

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")


def retrieval_node(current_state: STATE) -> dict:
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)

    vector_store = Chroma(
        client=chroma_client,
        collection_name="compliance_policies",
        embedding_function=embedding_model,
    )

    results = vector_store.similarity_search(
        query=current_state["question"],
        k=5,
    )
    
    chunks = [
        f"[Source: {doc.metadata.get('filename', 'unknown')}]\n{doc.page_content}"
        for doc in results
    ]

    return {"retrieval_results": chunks}
