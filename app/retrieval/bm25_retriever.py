import json
import re

from rank_bm25 import BM25Okapi


def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    return text.split()


def load_chunks():

    with open(
        "data/processed/chunks.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


chunks = load_chunks()


tokenized_chunks = [

    clean_text(chunk["text"])

    for chunk in chunks
]


bm25 = BM25Okapi(tokenized_chunks)


def bm25_search(query, top_k=3):

    tokenized_query = clean_text(query)

    scores = bm25.get_scores(tokenized_query)

    ranked_indices = sorted(

        range(len(scores)),

        key=lambda i: scores[i],

        reverse=True

    )[:top_k]

    results = []

    for idx in ranked_indices:

        results.append({

            "score": scores[idx],

            "chunk": chunks[idx]
        })

    return results


if __name__ == "__main__":

    while True:

        query = input("\nEnter query: ")

        if query.lower() == "exit":
            break

        results = bm25_search(query)

        for idx, result in enumerate(results):

            print(f"\nResult {idx + 1}")

            print("-" * 50)

            print(result["chunk"]["text"][:500])

            print("\nScore:")
            print(result["score"])