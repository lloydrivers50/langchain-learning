from langgraph.graph import StateGraph, START
from compliance_agent.agents.synthesis_agent import synthesis_node
from compliance_agent.state.schema import STATE


builder = StateGraph(STATE)

builder.add_node("synthesis", synthesis_node)

builder.add_edge(START, "synthesis")

graph = builder.compile()

final_state = graph.invoke({
    "question": "What are the compliance requirements for data storage?",
    "retrieval_results": ["Data must be encrypted at rest.", "Access controls must be implemented."],
    "graph_context": [{"source": "compliance_docs", "content": "Data must be encrypted at rest."}, {"source": "compliance_docs", "content": "Access controls must be implemented."}]
})

print("Final state:", final_state)
