
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from compliance_agent.state.schema import STATE


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

SYSTEM_PROMPT = """You are a compliance assistant. Your job is to answer questions
about company policies using ONLY the context provided below.

Rules:
- Only use the provided context to answer. Do not make up information.
- If the context doesn't contain enough information to answer, say so clearly.
- Cite which policy document(s) your answer comes from.
- Be concise and direct.
"""


def synthesis_node(current_state: STATE) -> dict:
    question = current_state["question"]
    chunks = current_state["retrieval_results"]

    if chunks:
        context = "\n\n".join(
            f"[{i}] {chunk}" for i, chunk in enumerate(chunks, 1)
        )
    else:
        context = "No relevant policy documents were found."


    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Context:\n{context}\n\nQuestion: {question}"),
    ])

    return {"final_answer": response.content}
