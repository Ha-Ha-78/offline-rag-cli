import ollama


class Embedding:

    def __init__(self, model):
        self.model = model


    def embed_chunks(self, chunks):

        texts = [chunk["text"] for chunk in chunks]

        response = ollama.embed(
            model=self.model,
            input=texts
        )

        embeddings = response["embeddings"]

        for chunk, embedding in zip(chunks, embeddings):
            chunk["embedding"] = embedding

        return chunks


    def embed_text(self, text):

        response = ollama.embed(
            model=self.model,
            input=text
        )

        return response["embeddings"][0]