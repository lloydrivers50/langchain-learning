from typing import TypedDict, NotRequired

class STATE(TypedDict):
    question: str
    retrieval_results: list[str]
    graph_context: list[dict]
    final_answer: NotRequired[str]
