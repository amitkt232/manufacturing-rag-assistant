import json
from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def load_chunks():

    with open(
        "data/processed/chunks.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def generate_embeddings(chunks):

    for chunk in chunks:

        embedding = model.encode(chunk["text"])

        chunk["embedding"] = embedding.tolist()

    return chunks


if __name__ == "__main__":

    chunks = load_chunks()

    embedded_chunks = generate_embeddings(chunks)

    with open(
        "data/processed/embedded_chunks.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            embedded_chunks,
            f,
            indent=2,
            ensure_ascii=False
        )

    print("Embeddings generated successfully!")