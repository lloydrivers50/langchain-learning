import chromadb
from compliance_agent.state.schema import STATE


# -----------------------------------------------------------------------------
# retrieval_node
# -----------------------------------------------------------------------------
# LangGraph node that queries ChromaDB for policy chunks relevant to the
# user's question. Takes the full graph state in, returns the matching
# documents under "retrieval_results" so the synthesis node can use them.
# -----------------------------------------------------------------------------
def retrieval_node(current_state: STATE) -> dict:
    """Given a user query, retrieve relevant documents from ChromaDB."""

    # Connect to the ChromaDB Docker container running on port 8000.
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)
    collection = chroma_client.get_collection("compliance_policies")

    # query_texts: ChromaDB converts this to a vector and finds the closest matches.
    # n_results: how many matching chunks to return.
    results = collection.query(
        query_texts=[current_state["question"]],
        n_results=5,
        include=["documents", "metadatas", "distances"],
    )

    # results["documents"] is a list of lists (one per query), so [0] gets
    # the results for our single query. This gets merged back into state.
    return {"retrieval_results": results["documents"][0]}

