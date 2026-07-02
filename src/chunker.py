from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunker:

    def __init__(self, chunk_size, chunk_overlap):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=chunk_size,

            chunk_overlap=chunk_overlap

        )

    def chunk(self, document):

        chunks = self.splitter.split_text(

            document["text"]

        )

        chunk_list = []

        for i, text in enumerate(chunks):

            chunk = {

                "id": f"{document['document_hash']}_{i}",

                "document_hash": document["document_hash"],

                "chunk_id": i,

                "source": document["file_name"],

                "file_name": document["file_name"],

                "file_path": document["file_path"],

                "file_type": document["file_type"],

                "text": text

            }

            chunk_list.append(chunk)

        return chunk_list