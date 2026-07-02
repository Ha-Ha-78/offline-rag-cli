import chromadb


class Database:

    def __init__(self, database_path):

        self.client = chromadb.PersistentClient(path=database_path)

        self.collection = self.client.get_or_create_collection(
            name="semantic_search"
        )


    def exists(self, chunk_id):

        result = self.collection.get(
            ids=[chunk_id]
        )

        return len(result["ids"]) > 0


    def add(self, chunk):

        if self.exists(chunk["id"]):

            print(f"Skipping : {chunk['source']} (Chunk {chunk['chunk_id']})")

            return

        metadata = {

            "document_hash": chunk["document_hash"],

            "source": chunk["source"],

            "file_name": chunk["file_name"],

            "file_path": chunk["file_path"],

            "file_type": chunk["file_type"],

            "chunk_id": chunk["chunk_id"]

        }

        self.collection.add(

            ids=[chunk["id"]],

            documents=[chunk["text"]],

            embeddings=[chunk["embedding"]],

            metadatas=[metadata]

        )


    def update(self, chunk):

        metadata = {

            "document_hash": chunk["document_hash"],

            "source": chunk["source"],

            "file_name": chunk["file_name"],

            "file_path": chunk["file_path"],

            "file_type": chunk["file_type"],

            "chunk_id": chunk["chunk_id"]

        }

        self.collection.update(

            ids=[chunk["id"]],

            documents=[chunk["text"]],

            embeddings=[chunk["embedding"]],

            metadatas=[metadata]

        )


    def delete_document(self, document_hash):

        self.collection.delete(

            where={

                "document_hash": document_hash

            }

        )


    def search(self, embedding, top_k):

        results = self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k

        )

        return results


    def count(self):

        return self.collection.count()


    def reset(self):

        self.client.delete_collection("semantic_search")

        self.collection = self.client.get_or_create_collection(
            name="semantic_search"
        )