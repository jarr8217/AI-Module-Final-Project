def chunk_text(text, chunk_size=1000, overlap=200):
    """
    Splits a string of text into overlapping chunks of a specified size.


    Args:
        text (str): The text to be split into chunks.
        chunk_size (int, optional): The size of each chunk. Defaults to 1000.
        overlap (int, optional): The amount of overlap between chunks. Defaults to 200.


    Returns:
        list: A list of overlapping chunks of text. Each chunk is a string.


    """
    chunks = []

    if len(text) <= chunk_size:
        return [text]
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        # Moves start forward, but keeps overlap so we don't lose context between chunks
        start = end - overlap

        if start < 0:
            start = 0

    return chunks


def chunk_docs(documents, chunk_size=1000, overlap=200):
    """
    Splits a list of documents into overlapping chunks of text.


    Args:
        documents (list): A list of documents. Each document is a dict with
            'source' and 'text' keys.
        chunk_size (int, optional): The size of each chunk. Defaults to 1000.
        overlap (int, optional): The amount of overlap between chunks. Defaults to 200.


    Returns:
        list: A list of overlapping chunks of text. Each chunk is a dict with
            'source', 'chunk_id', and 'text' keys.
    """
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
