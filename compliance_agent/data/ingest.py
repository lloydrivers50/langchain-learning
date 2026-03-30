from pathlib import Path
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document

# -----------------------------------------------------------------------------
# load_markdown_directory
# -----------------------------------------------------------------------------
# PURPOSE:
#   Recursively load all Markdown files from a directory and convert them into
#   LangChain Document objects, enriched with useful metadata.
#
# WHY THIS MATTERS:
#   - RAG pipelines depend heavily on metadata for filtering, ranking, and
#     debugging retrieval.
#   - File-level metadata (filename, path, timestamps) is essential for
#     traceability and observability.
#   - Using Pathlib ensures OS-agnostic, reliable filesystem operations.
#
# BEST PRACTICES APPLIED:
#   - Validate directory existence early.
#   - Use rglob for recursive matching.
#   - Wrap each file load in try/except so one bad file doesn't kill ingestion.
#   - Add consistent metadata to every Document.
#   - Preserve relative paths for multi-tenant or multi-root ingestion.
# -----------------------------------------------------------------------------

def load_markdown_directory(directory_path: str):
    directory = Path(directory_path)

    # Validate directory early to fail fast and clearly.
    if not directory.is_dir():
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    documents = []

    # Recursively find all Markdown files (*.md)
    for file_path in directory.rglob("*.md"):
        try:
            # UnstructuredMarkdownLoader parses markdown into structured text.
            # It may return 1 or multiple Document objects depending on content.
            loader = UnstructuredMarkdownLoader(str(file_path))
            docs = loader.load()

            # Enrich each Document with consistent metadata.
            for d in docs:
                d.metadata.update({
                    "filename": file_path.name,                     # e.g. "intro.md"
                    "path": str(file_path),                         # absolute path
                    "relative_path": str(file_path.relative_to(directory)),  # relative to root
                    "last_modified": file_path.stat().st_mtime,     # UNIX timestamp
                })

                documents.append(d)

        except Exception as e:
            # Never let a single corrupt file break ingestion.
            print(f"[WARN] Failed to load {file_path}: {e}")

    return documents
