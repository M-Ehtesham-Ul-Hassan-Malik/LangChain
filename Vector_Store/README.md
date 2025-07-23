# Vector Stores in LangChain

---

This repository explores **Vector Stores** in the context of modern AI-powered applications, particularly using **LangChain**. It includes implementation and documentation for popular vector stores such as **Chroma**, **FAISS**, **Qdrant**, and **Pinecone**.

---

## 📌 Table of Contents

- [What Are Vector Stores?](#what-are-vector-stores)
- [Indexing Techniques Explained](#-indexing-techniques-explained)
- [Why Vector Stores?](#why-vector-stores)
- [Vector Store vs Vector Database](#vector-store-vs-vector-database)
- [Vector Stores in LangChain](#vector-stores-in-langchain)
- [Supported Vector Stores](#supported-vector-stores)
  - [Chroma](#chroma)
  - [FAISS](#faiss)
  - [Qdrant](#qdrant)
  - [Pinecone](#pinecone)

---

## What Are Vector Stores?

Vector stores are specialized storage systems designed to **store and retrieve vector embeddings** i.e: numerical representations of text, images, or other data modalities used in machine learning and AI tasks.

### Key Features

- **Storage**  
  - In-Memory (useful for quick prototyping)  
  - On-Disk (suitable for large-scale, persistent storage)

- **Indexing**  
  Efficient data structures like  HNSW (Hierarchical Navigable Small World), IVF (Inverted File Index), or Flat Index (Brute-force Search) indices for fast retrieval.

- **Similarity Search**  
  Finds vectors that are closest in distance (cosine, Euclidean, dot product) to a given query vector.

- **CRUD Operations**  
  Add, update, delete, and retrieve vector embeddings as needed.

### Use Cases

- Semantic Search (text, code, legal documents)  
- Recommendation Engines  
- Question Answering (QA) Systems  
- Context Retrieval for LLMs (RAG architecture)  
- Image or Audio Matching  

---
## Indexing Techniques Explained

Efficient indexing is crucial for fast vector retrieval, especially when working with large datasets. Common strategies include:

---

###  Flat Index (Brute-force Search)

Compares the query vector with **every stored vector** using a distance metric (e.g., cosine or Euclidean).

-  100% accurate  
-  Slow with large datasets  
-  **Used in**: FAISS (`IndexFlatL2`), Chroma (default)

---

### IVF (Inverted File Index)

Partitions vectors into clusters (e.g., using KMeans). During search, only a few relevant clusters are scanned.

-  Much faster than Flat  
-  Approximate results  
-  **Used in**: FAISS (`IndexIVFFlat`, `IndexIVFPQ`)

---

### HNSW (Hierarchical Navigable Small World)

Builds a **multi-layer graph** where each vector (node) connects to nearby vectors. Uses a greedy search from top to bottom layers for fast and scalable navigation.

-  Very fast  
-  High recall and scalable  
-  **Used in**: FAISS, Qdrant, Milvus

---


## Why Vector Stores❓ 

Modern LLM-based systems require relevant context to generate accurate, grounded outputs. However, LLMs have input size limits and can't "remember" everything. This is where **vector stores** solve critical challenges.

### Challenges Solved

- **Efficient Context Retrieval**: Pull relevant chunks of data when needed  
- **Scalability**: Handle millions of documents with fast access  
- **Low Latency**: Real-time or near-real-time results  
- **Search Beyond Keywords**: Semantic understanding instead of lexical matches  

---

## Vector Store vs Vector Database

| Aspect               | Vector Store                                      | Vector Database                                      |
|----------------------|---------------------------------------------------|------------------------------------------------------|
| **Definition**        | In-memory or simple persistent store for vectors | Full-fledged database for storing and querying vectors |
| **Persistence**       | Optional                                          | Always persistent with durability and backup         |
| **Scaling**           | Limited (in-memory or local file)                | Distributed, scalable architecture                   |
| **Advanced Features** | Basic CRUD, simple search                        | Metadata filtering, hybrid search, replication       |

### Examples

- **Vector Stores**: FAISS, Annoy, Chroma  
- **Vector Databases**: Qdrant, Pinecone, Weaviate, Milvus  

### Use Cases

- **Vector Store**: Prototyping, local testing, small-scale apps  
- **Vector DB**: Production systems, large-scale data, real-time apps  

---

## Vector Stores in LangChain

LangChain provides an abstraction over various vector stores with a **common interface**, making it easy to swap implementations.

### 🔗 Supported Stores

Some popular vector stores supported in LangChain include:

- **Chroma**
- **FAISS**
- **Qdrant**
- **Pinecone**
- **Weaviate**
- **Redis**
- **Milvus**

###  Common Interface

All vector stores in LangChain support core methods like:

- `add_documents(docs)`  
- `similarity_search(query)`  
- `similarity_search_with_score(query)`  
- `delete(ids)`  
- `as_retriever()`

### 📎 Metadata Handling

LangChain allows attaching **metadata** to each document, which can later be used for:

- Filtering results  
- Improving context relevance  
- Custom ranking  

---

## Supported Vector Stores

### 🟩 Chroma

- **Type**: Local or in-memory vector store  
- **Features**:  
  - Fast prototyping  
  - Simple to use with LangChain  
  - Good for small to medium-scale applications  
- **Use Cases**: LLM apps, RAG, and semantic search demos  

---

### 🔵 FAISS (Facebook AI Similarity Search)

- **Type**: In-memory or disk-based  
- **Features**:  
  - High-performance similarity search  
  - Multiple indexing strategies (Flat, IVF, HNSW)  
  - Supports clustering and ANN (Approx. Nearest Neighbor)  
- **Use Cases**: Large-scale vector matching, offline similarity search  

---

### 🟣 Qdrant

- **Type**: Vector Database  
- **Features**:  
  - Persistent storage  
  - REST and gRPC API support  
  - Metadata-based filtering  
  - Hybrid search (text + vector)  
- **Use Cases**: AI assistants, real-time recommendation, RAG systems  

---

### 🔶 Pinecone

- **Type**: Fully managed vector database  
- **Features**:  
  - Scalable, serverless architecture  
  - Built-in replication and automatic indexing  
  - Metadata filtering and namespace support  
- **Use Cases**: Enterprise-grade LLM apps, semantic search APIs, production-ready RAG systems  

---

## Repository Structure

```
Vector_Stores/
│
├── LangChain_chroma.ipynb # Example using Chroma with LangChain
└── README.md # Documentation
```


---

## Contributions

Feel free to open issues or pull requests if you'd like to add more vector stores or examples. This is an open resource for exploring the landscape of vector search with LangChain.

---

