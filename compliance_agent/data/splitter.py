from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Create a splitter function that takes in the documents and returns the chunked documents
def text_splitter(documents):
    # 1. Create a text splitter
    splitter = RecursiveCharacterTextSplitter(
        # chunk_size: The maximum size of a chunk, where size is determined by the length_function.
        chunk_size=800,
        # chunk_overlap: Target overlap between chunks. Overlapping chunks helps to mitigate loss of information when context is divided between chunks.
        chunk_overlap=200,
        # length_function: Function determining the chunk size.
        length_function=len,
    )

    # 2. Split the loaded documents
    chunked_docs = splitter.split_documents(documents)

    print(f"Loaded {len(documents)} docs")
    print(f"Chunked into {len(chunked_docs)} chunks")

    return chunked_docs

  