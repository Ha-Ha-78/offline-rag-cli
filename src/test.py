from config import Config
from scanner import Scanner
from parser import Parser
from chunker import Chunker

config = Config()

scanner = Scanner(config.get("documents_path"))

parser = Parser()

files = scanner.scan()

chunker = Chunker(
    config.get("chunk_size"),
    config.get("chunk_overlap")
)


for file in files:

    text = parser.parse(file)

    chunks = chunker.chunk(text)

    print(f"\n{text['file_name']}")

    print(f"Total Chunks : {len(chunks)}")

    print("\nFirst Chunk:\n")

    print(chunks[0]["text"][:10])