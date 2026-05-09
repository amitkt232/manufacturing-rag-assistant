from sentence_transformers import (
    SentenceTransformer
)

import chromadb


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


client = chromadb.PersistentClient(
    path="data/vector_db"
)


collection = client.get_collection(
    name="manufacturing_docs"
)


def search(query, top_k=10):

    query_embedding = model.encode(query)

    results = collection.query(

        query_embeddings=[
            query_embedding.tolist()
        ],

        n_results=top_k
    )

    return results


if __name__ == "__main__":

    while True:

        query = input("\nEnter your query: ")

        if query.lower() == "exit":
            break

        results = search(query)

        print("\nRetrieved Results:\n")

        for idx, doc in enumerate(
            results["documents"][0]
        ):

            print(f"\nResult {idx + 1}")

            print("-" * 50)

            print(doc[:700])

            print("\nMetadata:")

            print(
                results["metadatas"][0][idx]
            )