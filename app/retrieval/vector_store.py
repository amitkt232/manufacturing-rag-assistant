import json
import chromadb


client = chromadb.PersistentClient(
    path="data/vector_db"
)

collection = client.get_or_create_collection(
    name="manufacturing_docs"
)


def load_embedded_chunks():

    with open(
        "data/processed/embedded_chunks.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def store_embeddings(chunks):

    for idx, chunk in enumerate(chunks):

        collection.add(

            ids=[str(idx)],

            embeddings=[chunk["embedding"]],

            documents=[chunk["text"]],

            metadatas=[{

                "document_name":
                chunk["document_name"],

                "page_number":
                chunk["page_number"],

                "chunk_id":
                chunk["chunk_id"]
            }]
        )


if __name__ == "__main__":

    chunks = load_embedded_chunks()

    store_embeddings(chunks)

    print("Embeddings stored in ChromaDB!")