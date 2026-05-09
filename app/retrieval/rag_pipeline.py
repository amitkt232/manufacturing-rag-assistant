from sentence_transformers import SentenceTransformer
import chromadb

from app.llm.llm import llm


embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


client = chromadb.PersistentClient(
    path="data/vector_db"
)


collection = client.get_collection(
    name="manufacturing_docs"
)


def retrieve_chunks(query, k=3):

    query_embedding = embedding_model.encode(query)

    results = collection.query(

        query_embeddings=[
            query_embedding.tolist()
        ],

        n_results=k
    )

    return results


def build_context(results):

    contexts = results["documents"][0]

    return "\n\n".join(contexts)


def create_prompt(query, context):

    prompt = f"""

You are an expert manufacturing maintenance assistant.

Answer ONLY from the provided context.

If answer is not available in context, say:
"I could not find relevant information in the documents."

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt


def generate_response(query):

    retrieval_results = retrieve_chunks(query)

    context = build_context(retrieval_results)

    prompt = create_prompt(query, context)

    response = llm.invoke(prompt)

    return {

        "query": query,

        "answer": response.content,

        "retrieved_chunks":
        retrieval_results["documents"][0],

        "metadata":
        retrieval_results["metadatas"][0]
    }


if __name__ == "__main__":

    while True:

        query = input("\nEnter your query: ")

        if query.lower() == "exit":
            break

        result = generate_response(query)

        print("\nANSWER:\n")
        print(result["answer"])

        print("\nSOURCES:\n")

        for idx, meta in enumerate(result["metadata"]):

            print(f"\nSource {idx + 1}")

            print(meta)