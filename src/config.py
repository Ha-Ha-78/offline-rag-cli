import json
import subprocess
from pathlib import Path


class Config:

    def __init__(self):

        self.config_file = Path("config/config.json")

        self.config_file.parent.mkdir(exist_ok=True)

        if self.config_file.exists():
            self.load()
        else:
            self.setup()


    def load(self):

        with open(self.config_file, "r") as file:
            self.data = json.load(file)


    def save(self):

        with open(self.config_file, "w") as file:
            json.dump(self.data, file, indent=4)


    def setup(self):

        print("\n========== First Time Setup ==========\n")


        while True:

            folder = input("Documents Folder : ").strip()

            path = Path(folder).expanduser()

            if path.exists() and path.is_dir():
                break

            print("Invalid folder.\n")


        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                check=True
            )
            print(result)

        except Exception:

            print("\nOllama is not installed.")
            print("Install Ollama first.\n")
            exit()


        models = []

        lines = result.stdout.splitlines()

        for line in lines[1:]:

            if line.strip():

                models.append(line.split()[0])

        if len(models) == 0:

            print("No Ollama models installed.")
            exit()


        print("\nAvailable Models\n")

        for i, model in enumerate(models):

            print(f"{i+1}. {model}")

        while True:

            try:

                choice = int(input("\nEmbedding Model : "))

                if 1 <= choice <= len(models):
                    embedding_model = models[choice - 1]
                    break

            except:
                pass

            print("Invalid Choice.")


        while True:

            try:

                choice = int(input("\nChat Model : "))

                if 1 <= choice <= len(models):
                    chat_model = models[choice - 1]
                    break

            except:
                pass

            print("Invalid Choice.")
        
        print("\nChunk Size Guide")
        print("----------------")
        print("300  - Small chunks (higher precision)")
        print("500  - Balanced (recommended)")
        print("1000 - Large chunks (better context, slower search)")

        while True:

            try:

                chunk_size = int(input("\nChunk Size (Recommended: 500): "))

                if chunk_size > 0:
                    break

            except:
                pass

            print("Please enter a positive integer.")


        while True:

            try:

                chunk_overlap = int(input("\nChunk Overlap (Recommended: 100): "))

                if 0 <= chunk_overlap < chunk_size:
                    break

            except:
                pass

            print("Chunk overlap must be between 0 and Chunk Size - 1.")


        print("\n" + "=" * 45)
        print("        Configuration Summary")
        print("=" * 45)

        print(f"Documents Folder : {path.resolve()}")
        print(f"Embedding Model  : {embedding_model}")
        print(f"Chat Model       : {chat_model}")
        print(f"Chunk Size       : {chunk_size}")
        print(f"Chunk Overlap    : {chunk_overlap}")
        print(f"Database Path    : database/chroma")
        print(f"Metadata File    : data/indexed_files.json")

        print("=" * 45)

        while True:

            choice = input("\nSave this configuration? (y/n): ").strip().lower()

            if choice in ("y", "yes"):
                break

            if choice in ("n", "no"):
                print("\nSetup cancelled.")
                exit()

            print("Please enter y or n.")


        self.data = {

            "documents_path": str(path.resolve()),

            "database_path": "database/chroma",

            "embedding_model": embedding_model,

            "chat_model": chat_model,

            "chunk_size": chunk_size,

            "chunk_overlap": chunk_overlap,

            "top_k": 5,

            "metadata_file": "data/indexed_files.json"

        }

        self.save()

        print("\nConfiguration Saved Successfully.\n")

    def get(self , key):
        return self.data.get(key)