# Compliance Agent — Enterprise AI Q&A System

An agentic AI system that answers compliance and HR questions by reasoning across policy documents and a regulatory knowledge graph. Built to production-grade standards using LangGraph, LangChain, Neo4j, FastAPI, and Docker.

---

## What It Does

Enterprise employees and legal teams can ask plain-English questions:

> *"Can I expense a client dinner over £100?"*
> *"Is this contract termination clause compliant with UK employment law?"*
> *"What are our GDPR obligations if a user requests data deletion?"*

Instead of a human spending hours reading policy documents, three AI agents collaborate to return a **cited, auditable answer in seconds**.

Every answer is traceable. No black boxes. This is a hard requirement — in compliance, a wrong answer is a legal liability.

---

## Architecture

### The Three-Agent Pipeline

```
User Question
     │
     ▼
┌──────────────────┐
│  Retrieval Agent │  ← Searches policy documents via RAG
│  retrieval_agent │    Returns relevant chunks with source citations
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│   Graph Agent   │  ← Traverses Neo4j knowledge graph
│   graph_agent   │    Maps how regulations connect to each other
└────────┬────────┘
         │
         ▼
┌──────────────────┐
│ Synthesis Agent  │  ← Combines both sources
│ synthesis_agent  │    Produces final cited, structured response
└────────┬─────────┘
         │
         ▼
  Structured Answer
  (with citations + confidence)
```

### Why Three Agents?

| Agent | Problem It Solves |
|---|---|
| Retrieval | Raw document search — finds *what the policy says* |
| Graph | Relational reasoning — finds *how rules connect* (e.g. GDPR → Data Retention → Employee Records) |
| Synthesis | Accuracy + auditability — ensures the final answer cites its sources and doesn't hallucinate |

A single LLM call cannot reliably do all three. Separation of concerns = auditable, debuggable outputs.

---

## Folder Structure

```
compliance-agent/
├── agents/
│   ├── retrieval_agent.py     # RAG over policy documents (LangChain + vector store)
│   ├── graph_agent.py         # Cypher queries against Neo4j knowledge graph
│   └── synthesis_agent.py     # Final answer generation with citations
│
├── pipeline/
│   └── workflow.py            # LangGraph state machine — orchestrates agent flow
│
├── api/
│   └── main.py                # FastAPI — exposes /query endpoint to the frontend
│
├── data/
│   └── policies/              # Source documents (PDFs, markdown) ingested into RAG
│
├── requirements.txt           # Python dependencies
└── docker-compose.yml         # Runs API + Neo4j together
```

### What Each File Actually Does

**`pipeline/workflow.py`**
The brain. Defines the LangGraph state graph — what runs, in what order, and what gets passed between agents. State flows through nodes; each node transforms it. This is the file that makes the system *agentic* rather than just a chain.

**`agents/retrieval_agent.py`**
Embeds the question, searches the vector store, returns the top-k most relevant policy chunks. Knows nothing about the other agents.

**`agents/graph_agent.py`**
Takes the question (or entities extracted from it), queries Neo4j using Cypher, returns structured relational context. Knows how "GDPR Article 17" connects to "Data Subject Request" connects to "HR Policy: Employee Data".

**`agents/synthesis_agent.py`**
Receives output from both agents. Constructs a final answer that cites specific documents and graph nodes. Refuses to answer if confidence is below threshold.

**`api/main.py`**
FastAPI server. Single `POST /query` endpoint. Accepts a question, kicks off the workflow, returns the structured response. This is what the frontend (Lovable) talks to.

**`data/policies/`**
Raw source documents. UK GDPR, Employment Rights Act, ACAS codes of practice, internal HR policies. These get chunked and embedded during the ingestion pipeline.

---

## Tech Stack

| Layer | Technology | Why |
|---|---|---|
| Orchestration | LangGraph | State machine model — agents can branch, loop, and hand off with full state visibility |
| Tooling / RAG | LangChain | Document loaders, text splitters, vector store abstractions |
| Knowledge Graph | Neo4j | Relational reasoning across regulations — vector search alone can't map *how rules connect* |
| LLM | OpenAI API | GPT-4o for synthesis; embeddings for retrieval |
| API Layer | FastAPI | Async Python API — industry standard for ML/AI services |
| Deployment | Docker | Reproducible environment; Neo4j + API run as services |
| Frontend | Lovable | Generates React frontend, writes to GitHub |

---

## Key Design Decisions

**Why LangGraph over a simple chain?**
Compliance answers sometimes require conditional logic — if retrieval returns nothing useful, the graph agent needs to take a different path. LangGraph gives you explicit state management and conditional edges. A chain can't do that cleanly.

**Why Neo4j alongside RAG?**
Vector search finds *similar text*. It cannot tell you that GDPR Article 17 *legally supersedes* your internal data retention policy, or that a contract clause connects to three separate statutory obligations. The graph encodes those relationships explicitly.

**Why three agents instead of one big prompt?**
Debuggability. When the answer is wrong, you need to know *which stage* failed — retrieval, graph traversal, or synthesis. Monolithic prompts are black boxes. Agents are observable.

**Why FastAPI?**
It's the de facto standard for Python AI services. Async, fast, auto-generates OpenAPI docs. Every production AI system you'll encounter in enterprise uses it.

---

## Build Phases

| Phase | Goal | Deliverable |
|---|---|---|
| 1 | LangGraph fundamentals | Single-node workflow: question in → structured response out |
| 2 | RAG pipeline | Retrieval agent ingests and queries policy documents |
| 3 | Neo4j knowledge graph | Graph agent maps regulatory relationships, answers graph queries |
| 4 | Multi-agent orchestration | All three agents wired into LangGraph workflow |
| 5 | FastAPI layer | `/query` endpoint serving the full pipeline |
| 6 | Docker deployment | Compose file runs Neo4j + API as production services |
| 7 | Frontend integration | Lovable UI connects to the API |
| 8 | Hardening | Citations enforced, hallucination guardrails, confidence thresholds |

---

## Interview Defence Points

You must be able to answer these without hesitating:

- Why did you use LangGraph and not CrewAI or a plain LangChain chain?
- What is the trade-off between vector RAG and graph RAG — when does each fail?
- How does your state schema change as the query gets more complex?
- What happens when retrieval returns nothing relevant?
- How do you prevent the synthesis agent from hallucinating?
- How would you scale this to 10,000 concurrent enterprise users?
- Why is auditability a hard requirement in compliance, and how does your architecture enforce it?

---

## The Business Case (Why This Matters)

Companies like Capgemini and KPMG build systems like this and sell them to enterprise clients for hundreds of thousands of pounds. The manual alternative — a compliance team reading documents — costs the same in human hours every year.

This system doesn't replace compliance lawyers. It gives them a tool that does the first 80% of research instantly, with sources attached, so they can focus on judgment rather than retrieval.

That's the pitch. That's what you built.