import chromadb


if __name__ == "__main__":
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name="test")

    collection.add(
        documents=["This is a document", "This is another document"],
        metadatas=[{"source": "my_source"}, {"source": "my_source"}],
        ids=["id1", "id2"]
    )

    # peeked_documents = collection.peek()
    # print(peeked_documents.keys())

    # print(len(peeked_documents["ids"]))
    # print(len(peeked_documents["documents"]))
    # print(len(peeked_documents["metadatas"]))
    # print(len(peeked_documents["embeddings"]))

