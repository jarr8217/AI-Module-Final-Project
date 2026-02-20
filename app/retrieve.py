import re


def tokenize(text):
    return re.findall(r'\w+', text.lower())


def score_overlap(query_tokens, chunk_text):
    chunk_tokens = set(tokenize(chunk_text))
    return len(set(query_tokens).intersection(chunk_tokens))


def retrieve_top_k(query, chunks, k=5):
    query_tokens = tokenize(query)
    scored = []

    for chunk in chunks:
        score = score_overlap(query_tokens, chunk['text'])
        if score > 0:
            scored.append(
                {
                    'score': score,
                    'source': chunk['source'],
                    'chunk_id': chunk['chunk_id'],
                    'text': chunk['text'],
                }
            )

    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:k]
