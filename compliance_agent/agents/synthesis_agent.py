from compliance_agent.state.schema import STATE



def synthesis_node(current_state: STATE) -> dict[str, str]:
    return {"final_answer": f"Based on the question '{current_state['question']}' and the retrieval results {current_state['retrieval_results']}, the final answer is: ..."}
