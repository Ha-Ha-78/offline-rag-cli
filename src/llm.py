import ollama


class LLM:

    def __init__(self, model):

        self.model = model


    def ask(self, question, context):

        prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, reply:

"I couldn't find that information in the indexed documents."

Do not make up facts.
Do not use outside knowledge.

---------------- CONTEXT ----------------

{context}

-----------------------------------------

Question:
{question}

Answer:
"""

        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]