from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document

from .splitter import split_documents
from .embeddings import build_vector_store


def load_markdown_directory(directory_path: str):
    directory = Path(directory_path)

    if not directory.is_dir():
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    documents = []

    for file_path in directory.rglob("*.md"):
        try:
            loader = UnstructuredMarkdownLoader(str(file_path))
            docs = loader.load()

            for d in docs:
                d.metadata.update({
                    "filename": file_path.name,                     # e.g. "intro.md"
                    "path": str(file_path),                         # absolute path
                    "relative_path": str(file_path.relative_to(directory)),  # relative to root
                    "last_modified": file_path.stat().st_mtime,     # UNIX timestamp
                })

                documents.append(d)

        except Exception as e:
            print(f"[WARN] Failed to load {file_path}: {e}")

    return documents

if __name__ == "__main__":                                                                                           
      policies_dir = Path(__file__).parent / "policies"
      data = load_markdown_directory(str(policies_dir))
      chunks = split_documents(data)
      vector_store = build_vector_store(chunks)

