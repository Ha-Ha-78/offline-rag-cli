class Search:

    def __init__(self, database, embedder):

        self.database = database
        self.embedder = embedder


    def search(self, question, top_k):

        query_embedding = self.embedder.embed_text(question)

        results = self.database.search(
            query_embedding,
            top_k
        )

        output = []

        ids = results["ids"][0]
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for i in range(len(ids)):

            output.append({

                "id": ids[i],

                "text": documents[i],

                "distance": distances[i],

                "source": metadatas[i]["source"],

                "file_name": metadatas[i]["file_name"],

                "file_path": metadatas[i]["file_path"],

                "file_type": metadatas[i]["file_type"],

                "chunk_id": metadatas[i]["chunk_id"],

                "document_hash": metadatas[i]["document_hash"]

            })

        return output
    
    def build_context(self, results):

        context = ""

        for i, result in enumerate(results, start=1):

            context += f"========== Document {i} ==========\n"
            context += f"Source : {result['source']}\n\n"
            context += result["text"]
            context += "\n\n"

        return context