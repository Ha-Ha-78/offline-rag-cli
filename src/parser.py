import fitz
import hashlib
from pathlib import Path


class Parser:

    def __init__(self):
        pass

    def parse(self, file_path):

        file_path = Path(file_path)

        extension = file_path.suffix.lower()

        if extension == ".txt":
            text = self.read_txt(file_path)

        elif extension == ".pdf":
            text = self.read_pdf(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

        # Hash the file CONTENTS (not the path)
        document_hash = self.calculate_hash(file_path)

        return {

            "document_hash": document_hash,

            "file_name": file_path.name,

            "file_path": str(file_path),

            "file_type": extension,

            "text": text

        }


    def calculate_hash(self, file_path):

        sha = hashlib.sha256()

        with open(file_path, "rb") as file:

            while True:

                chunk = file.read(8192)

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()


    def read_txt(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()


    def read_pdf(self, file_path):

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text