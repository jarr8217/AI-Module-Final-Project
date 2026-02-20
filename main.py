from pathlib import Path

from app.paths import ensure_project_dirs
from app.ingest import discover_doc_files, load_documents
from app.chunking import chunk_docs
from app.retrieve import retrieve_top_k


def main():
    project_root = Path(".").resolve()
    data_dir, storage_dir = ensure_project_dirs(project_root)

    files = discover_doc_files(data_dir)
    documents = load_documents(files)
    chunks = chunk_docs(documents, chunk_size=1000, overlap=200)

    print("Docs found:", len(files))
    print("Docs loaded:", len(documents))
    print("Chunks created:", len(chunks))

    query = input("\nAsk a question: ").strip()
    results = retrieve_top_k(query, chunks, k=5)

    print("\nTop results:")
    if not results:
        print("No matches found.")
        return

    for r in results:
        print("\nScore:", r["score"])
        print("Source:", r["source"])
        print("Chunk ID:", r["chunk_id"])
        print("Text preview:", r["text"][:200])


if __name__ == "__main__":
    main()
