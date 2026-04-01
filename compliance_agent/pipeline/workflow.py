from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, START
from compliance_agent.agents.retrieval_agent import retrieval_node
from compliance_agent.agents.synthesis_agent import synthesis_node
from compliance_agent.state.schema import STATE

builder = StateGraph(STATE)

builder.add_node("retrieval", retrieval_node)
builder.add_node("synthesis", synthesis_node)

builder.add_edge(START, "retrieval")
builder.add_edge("retrieval", "synthesis")

graph = builder.compile()

if __name__ == "__main__":
    final_state = graph.invoke({
        "question": "What are the compliance requirements for data storage?",
        "retrieval_results": [],
        "graph_context": [],
    })

    print("\n" + "=" * 60)
    print("QUESTION:", final_state["question"])
    print("=" * 60)
    print("\nRETRIEVED CHUNKS:")
    for i, chunk in enumerate(final_state["retrieval_results"], 1):
        print(f"  [{i}] {chunk[:100]}...")
    print("\nFINAL ANSWER:")
    print(final_state["final_answer"])
    print("=" * 60)
