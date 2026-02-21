import re


def tokenize(text):
    '''
    Splits a string of text into individual words.

    Args:
        text (str): The text to be split into words.

    Returns:
        list: A list of individual words from the input text.
    '''
    return re.findall(r"\w+", text.lower())


def score_overlap(query_tokens, chunk_text):
    '''
    Calculate the overlap score of a query with a chunk of text.

    The overlap score is the number of words in the query that also appear in the chunk.

    Args:
        query_tokens (list): A list of words from a query.
        chunk_text (str): A chunk of text to score against the query.

    Returns:
        int: The overlap score of the query with the chunk of text.'''
    chunk_tokens = set(tokenize(chunk_text))
    return len(set(query_tokens).intersection(chunk_tokens))


def retrieve_top_k(query, chunks, k=5):
    '''
    Retrieve the top k scoring chunks of text based on overlap with a query.

    Args:
        query (str): The query to search for.
        chunks (list): A list of chunks of text to search through.
        k (int, optional): The number of chunks to return. Defaults to 5.

    Returns:
        list: A list of up to k chunks of text, sorted by score in descending order.
    '''
    query_tokens = tokenize(query)

    scored = []
    for chunk in chunks:
        score = score_overlap(query_tokens, chunk["text"])
        if score > 0:
            scored.append(
                {
                    "score": score,
                    "source": chunk["source"],
                    "chunk_id": chunk["chunk_id"],
                    "text": chunk["text"],
                }
            )

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:k]
