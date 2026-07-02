# 🚀 Offline RAG CLI

A fully offline Retrieval-Augmented Generation (RAG) command-line application that performs semantic search over **PDF** and **TXT** documents using **ChromaDB** and **Ollama**.

Instead of sending your documents to cloud APIs, everything runs **locally** on your machine, ensuring complete privacy while providing fast semantic search and question answering.

---

## ✨ Features

- 📄 PDF & TXT document support
- 🧠 Semantic search using vector embeddings
- 🤖 Local LLM powered by Ollama
- 💾 ChromaDB vector database
- 🔄 Automatic synchronization of documents
- 📂 Detects newly added, updated, and deleted files
- ✂️ Configurable chunk size & chunk overlap
- 📊 Batch embedding generation for faster indexing
- 🔍 Shows source documents used to generate answers
- 💻 Simple terminal-based interface
- 🔒 100% Offline (No API Keys Required)

---

# 🏗️ Architecture

```
                   Documents Folder
                  (PDF / TXT Files)
                          │
                          ▼
                     File Scanner
                          │
                          ▼
                    Document Parser
                          │
                          ▼
                 Recursive Text Splitter
                          │
                          ▼
                Ollama Embedding Model
                          │
                          ▼
                     ChromaDB Storage
                          │
                          ▼
                  Semantic Similarity Search
                          │
                          ▼
                     Context Builder
                          │
                          ▼
                   Ollama Chat Model
                          │
                          ▼
                      Final Answer
```

---

# 📁 Project Structure

```
offline-rag-cli/

├── src/
│   ├── main.py
│   ├── config.py
│   ├── scanner.py
│   ├── parser.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── database.py
│   ├── search.py
│   ├── llm.py
│   └── sync.py
│
├── config/
├── data/
├── database/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Requirements

- Python 3.10+
- Ollama
- ChromaDB

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Ha-Ha-78/offline-rag-cli.git
```

```bash
cd offline-rag-cli
```

Create a virtual environment

```bash
python -m venv my_venv
```

Linux/macOS

```bash
source my_venv/bin/activate
```

Windows

```bash
my_venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Install Ollama

Download Ollama

https://ollama.com/download

Pull an embedding model

```bash
ollama pull mxbai-embed-large
```

Pull a chat model

```bash
ollama pull qwen3.5:0.8b
```

You may use any Ollama-supported embedding model and chat model.

---

# ▶️ Running the Project

```bash
cd src
```

```bash
python main.py
```

---

# ⚙️ First Time Setup

The application will ask for:

- Documents folder
- Embedding model
- Chat model
- Chunk size
- Chunk overlap

Example

```
========== First Time Setup ==========

Documents Folder:
/home/user/Documents

Embedding Model:
mxbai-embed-large

Chat Model:
qwen3.5:0.8b

Chunk Size:
500

Chunk Overlap:
100
```

The configuration is stored locally and reused in future runs.

---

# 🔄 Document Synchronization

Every time the application starts, it automatically

- Detects newly added files
- Detects updated files
- Detects deleted files
- Updates ChromaDB automatically

No manual indexing required.

---

# 💬 Example

```
========== Offline RAG CLI ==========

1. Ask Question
2. Synchronize Documents
3. Show Database Statistics
4. Reset Database
5. Exit
```

Question

```
What is Reinforcement Learning?
```

Output

```
Reinforcement Learning is a machine learning paradigm
where an agent learns by interacting with an environment
and receives rewards or penalties for its actions...
```

Sources

```
Hands-On Machine Learning.pdf

ReinforcementLearningNotes.txt
```

---

# 🧠 Technologies Used

- Python
- Ollama
- ChromaDB
- PyMuPDF
- LangChain Text Splitter
- tqdm

---

# 🚀 Future Improvements

- DOCX Support
- CSV Support
- Excel Support
- Markdown Support
- OCR for Images
- Streaming LLM Responses
- Hybrid Search (Keyword + Semantic)
- Cross Encoder Re-ranking
- Automatic File Watching
- Multi-threaded Indexing
- GUI Version

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project, feel free to fork the repository and submit a pull request.

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub!

It helps others discover the project and motivates future development.
