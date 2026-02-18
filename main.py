from pathlib import Path


def ensure_project_dirs(project_root):
    """
    Ensures that the project's data and storage directories exist.

    Args:
        project_root: The path to the root directory of the project.

    Returns:
        A tuple containing the paths to the project's data and storage directories.
    """
    data_dir = project_root / 'data'
    storage_dir = project_root / 'storage'

    data_dir.mkdir(exist_ok=True)
    storage_dir.mkdir(exist_ok=True)

    return data_dir, storage_dir


def discover_doc_files(data_dir):
    """Discover all .md and .txt files in data_dir and its subdirectories.

    Returns a sorted list of all discovered files.
    """
    txt_files = list(data_dir.rglob('*.md'))
    md_files = list(data_dir.rglob('*.txt'))

    files = md_files + txt_files

    return sorted(files)


def load_documents(file_paths):
    documents = []

    for path in file_paths:
        try:
            text = path.read_text(encoding='utf-8', errors='ignore').strip()
        except Exception as e:
            print('Skipping unreadable file:', path, '| Error:', e)
            continue
        documents.append(
            {
                'source': str(path),
                'text': text,
            }
        )

    return documents


def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []

    if len(text) <= chunk_size:
        return [text]
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        # Moves start forwarward, but keeps overlap so we don't lose context between chunks
        start = end - overlap

        if start < 0:
            start = 0

    return chunks


def chunk_docs(documents, chunk_size=1000, overlap=200):
    all_chunks = []

    for doc in documents:
        pieces = chunk_text(doc['text'], chunk_size, overlap=overlap)

        for i, piece in enumerate(pieces):
            all_chunks.append(
                {
                    'source': doc['source'],
                    'chunk_id': i,
                    'text': piece,
                }
            )

    return all_chunks


def main():

    project_root = Path('.').resolve()  # absolute path to current folder
    data_dir, storage_dir = ensure_project_dirs(project_root)

    files = discover_doc_files(data_dir)
    documents = load_documents(files)

    chunks = chunk_docs(documents, chunk_size=1000, overlap=200)

    print('Project root:', project_root)
    print('Data directory:', data_dir)
    print('Storage directory:', storage_dir)
    print('Docs found:', len(files))
    print('Docs loaded:', len(documents))

    '''if documents:
        print('\nPreview of first doc source:', documents[0]['source'])
        print('Preview of first doc text (first 500 chars):')
        print(documents[0]['text'][:500])'''

    if chunks:
        print("\nPreview chunk:")
        print("Source:", chunks[0]["source"])
        print("Chunk ID:", chunks[0]["chunk_id"])
        print("Text (first 200 chars):")
        print(chunks[0]["text"][:200])


if __name__ == '__main__':
    main()
