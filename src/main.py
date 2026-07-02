from config import Config
from scanner import Scanner
from parser import Parser
from chunker import Chunker
from embedding import Embedding
from database import Database
from search import Search
from llm import LLM
from sync import Sync


def main():

    print("\n========== Local Semantic Search ==========\n")

    config = Config()


    scanner = Scanner(
        config.get("documents_path")
    )

    parser = Parser()

    chunker = Chunker(
        config.get("chunk_size"),
        config.get("chunk_overlap")
    )

    embedder = Embedding(
        config.get("embedding_model")
    )

    database = Database(
        config.get("database_path")
    )

    search = Search(
        database,
        embedder
    )

    llm = LLM(
        config.get("chat_model")
    )

    sync = Sync(
        scanner,
        parser,
        chunker,
        embedder,
        database,
        config.get("metadata_file")
    )


    sync.synchronize()


    while True:

        print("\n===================================")
        print("1. Ask Question")
        print("2. Synchronize Documents")
        print("3. Show Database Statistics")
        print("4. Reset Database")
        print("5. Exit")
        print("===================================\n")

        choice = input("Enter choice : ").strip()

        # ----------------------------------

        if choice == "1":

            question = input("\nQuestion : ").strip()

            if not question:
                continue

            results = search.search(
                question,
                config.get("top_k")
            )

            if len(results) == 0:

                print("\nNo relevant documents found.\n")
                continue

            context = search.build_context(results)

            answer = llm.ask(
                question,
                context
            )

            print("\n-----------------------------------\n")
            print(answer)
            print("\n-----------------------------------\n")


        elif choice == "2":

            sync.synchronize()


        elif choice == "3":

            print()

            print(f"Indexed Chunks : {database.count()}")

            print()


        elif choice == "4":

            confirm = input(
                "\nAre you sure? (y/n) : "
            )

            if confirm.lower() == "y":

                database.reset()

                # Clear metadata file
                sync.metadata = {}
                sync.save_metadata()

                print("\nDatabase Reset Successfully.\n")


        elif choice == "5":

            print("\nGoodbye!\n")
            break


        else:

            print("\nInvalid Choice.\n")


if __name__ == "__main__":
    main()