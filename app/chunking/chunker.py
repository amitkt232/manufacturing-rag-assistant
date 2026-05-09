import json
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(json_path):

    with open(json_path, "r", encoding="utf-8") as f:

        return json.load(f)


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for page in documents:

        texts = splitter.split_text(page["text"])

        for chunk_id, text in enumerate(texts):

            chunk_data = {

                "document_name": page["document_name"],
                "page_number": page["page_number"],
                "chunk_id": chunk_id,
                "text": text,
                "is_scanned": page["is_scanned"]
            }

            chunks.append(chunk_data)

    return chunks


if __name__ == "__main__":

    documents = load_documents("data/processed/output.json")

    chunks = create_chunks(documents)

    with open("data/processed/chunks.json", "w", encoding="utf-8") as f:

        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Created {len(chunks)} chunks successfully!")