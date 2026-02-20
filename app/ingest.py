def discover_doc_files(data_dir):
    """Discover all .md and .txt files in data_dir and its subdirectories.


    Returns a sorted list of all discovered files.
    """
    txt_files = list(data_dir.rglob('*.md'))
    md_files = list(data_dir.rglob('*.txt'))

    files = md_files + txt_files

    return sorted(files)


def load_documents(file_paths):
    """
    Load documents from a list of file paths.


    Args:
        file_paths: A list of file paths to load.


    Returns:
        A list of dictionaries, where each dictionary contains the source
        path and text of a document.
    """
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
