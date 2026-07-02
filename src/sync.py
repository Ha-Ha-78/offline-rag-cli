import json
from pathlib import Path
from tqdm import tqdm


class Sync:

    def __init__(
        self,
        scanner,
        parser,
        chunker,
        embedder,
        database,
        metadata_file
    ):

        self.scanner = scanner
        self.parser = parser
        self.chunker = chunker
        self.embedder = embedder
        self.database = database

        self.metadata_file = Path(metadata_file)

        self.metadata = self.load_metadata()


    def load_metadata(self):

        if not self.metadata_file.exists():
            return {}

        with open(self.metadata_file, "r") as file:
            return json.load(file)


    def save_metadata(self):

        self.metadata_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(self.metadata_file, "w") as file:
            json.dump(
                self.metadata,
                file,
                indent=4
            )

    def synchronize(self):

        print("\nSynchronizing documents...\n")

        files = self.scanner.scan()

        current_files = set()

        for file in files:

            document = self.parser.parse(file)

            path = document["file_path"]

            current_files.add(path)

            old_hash = self.metadata.get(path)

            new_hash = document["document_hash"]


            if old_hash is None:

                print(f"[NEW] {document['file_name']}")

                self.index_document(document)

                self.metadata[path] = new_hash

                continue


            if old_hash != new_hash:

                print(f"[UPDATED] {document['file_name']}")

                self.database.delete_document(old_hash)

                self.index_document(document)

                self.metadata[path] = new_hash


        stored_files = list(self.metadata.keys())

        for path in stored_files:

            if path not in current_files:

                print(f"[REMOVED] {Path(path).name}")

                self.database.delete_document(
                    self.metadata[path]
                )

                del self.metadata[path]

        self.save_metadata()

        print("\nSynchronization Complete.\n")


    def index_document(self, document):

        chunks = self.chunker.chunk(document)

        total_chunks = len(chunks)

        print(f"Total Chunks : {total_chunks}")

        BATCH_SIZE = 32

        for i in tqdm(
            range(0, total_chunks, BATCH_SIZE),
            desc=f"Indexing {document['file_name']}",
            unit="batch"
        ):

            batch = chunks[i:i + BATCH_SIZE]

            batch = self.embedder.embed_chunks(batch)

            for chunk in batch:

                self.database.add(chunk)