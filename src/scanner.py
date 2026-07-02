from pathlib import Path


class Scanner:

    def __init__(self, documents_path):

        self.documents_path = Path(documents_path)

        self.supported_extensions = [
            ".pdf",
            ".txt"
        ]

    def scan(self):

        files = []

        for file in self.documents_path.rglob("*"):

            if file.is_file() and file.suffix.lower() in self.supported_extensions:
                files.append(file)

        return files

    def display(self):

        files = self.scan()

        if len(files) == 0:
            print("\nNo supported files found.\n")
            return

        print(f"\nFound {len(files)} file(s):\n")

        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        print()