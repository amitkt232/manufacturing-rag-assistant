from app.retrieval.retrieve import search
from app.retrieval.bm25_retriever import bm25_search


def hybrid_search(query):

    vector_results = search(query)

    bm25_results = bm25_search(query)

    return {

        "vector_results": vector_results,

        "bm25_results": bm25_results
    }


if __name__ == "__main__":

    while True:

        query = input("\nEnter query: ")

        if query.lower() == "exit":
            break

        results = hybrid_search(query)

        print("\nVECTOR SEARCH RESULTS\n")
        print("=" * 60)

        for idx, doc in enumerate(
            results["vector_results"]["documents"][0]
        ):

            print(f"\nVector Result {idx + 1}")
            print("-" * 50)

            print(doc[:500])

        print("\nBM25 RESULTS\n")
        print("=" * 60)

        for idx, result in enumerate(
            results["bm25_results"]
        ):

            print(f"\nBM25 Result {idx + 1}")
            print("-" * 50)

            print(result["chunk"]["text"][:500])