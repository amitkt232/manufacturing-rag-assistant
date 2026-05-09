from sentence_transformers import CrossEncoder

from app.retrieval.retrieve import search


reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(query):

    results = search(query)

    chunks = results["documents"][0]

    pairs = [

        [query, chunk]

        for chunk in chunks
    ]

    scores = reranker.predict(pairs)

    reranked = sorted(

        zip(scores, chunks),

        key=lambda x: x[0],

        reverse=True
    )

    return reranked


if __name__ == "__main__":

    while True:

        query = input("\nEnter query: ")

        if query.lower() == "exit":
            break

        results = rerank(query)

        for idx, (score, chunk) in enumerate(results):

            print(f"\nResult {idx + 1}")

            print("-" * 50)

            print(f"Score: {score}")

            print(chunk[:500])