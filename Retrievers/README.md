
# Retrievers

## What are Retrievers?

In LangChain, **retrievers** are tools used to fetch relevant documents or data from a variety of sources in response to a user's query. These retrievers do not generate responses themselves; instead, they find and return the most useful content, which can then be passed to a language model for processing.

> All retrievers in LangChain are **Runnables**, which means they can be composed into chains or workflows using the LangChain Expression Language (LCEL).

---

## Types of Retrievers in LangChain

### 1. Data Source Retrievers
These retrievers fetch documents directly from external or embedded data sources.

- **WikipediaRetriever**  
- **VectorStoreRetriever**  
- **ArxivRetriever**

### 2. Search Strategy Retrievers
These retrievers apply advanced strategies to enhance retrieval quality by generating multiple queries or compressing results.

- **MMR (Maximal Marginal Relevance) Retriever**  
- **Multi-Query Retriever**  
- **Contextual Compression Retriever**

---

## Wikipedia Retriever

The `WikipediaRetriever` allows you to query Wikipedia and retrieve content relevant to a given question.

**Use Cases:**
- Research assistants
- General knowledge queries
- Educational bots

**Key Features:**
- Pulls information from a vast, free knowledge base
- Easy to use and integrate

---

## Vector Store Retriever

`VectorStoreRetriever` uses vector similarity search to retrieve documents based on semantic similarity.

**Use Cases:**
- Chat with documents
- Personalized content fetch
- Memory retrieval in agents

**Key Features:**
- Works with various vector stores (FAISS, Pinecone, Chroma, etc.)
- Embeds user query and finds closest matches

---

## ArxivRetriever

The `ArxivRetriever` fetches academic papers from [arXiv.org](https://arxiv.org), making it ideal for technical or research-intensive applications.

**Why ArxivRetriever?**
- Connects to one of the most authoritative open-access scientific databases.
- Ensures responses are backed by research-grade content.

**Use Cases:**
- Academic search agents
- Research assistants
- Answering technical queries

---

## Maximal Margin Relevance (MMR) Retriever

The `MMRRetriever` uses **Maximal Marginal Relevance** to balance relevance and diversity when retrieving documents.

### Why MMR?
Most vector searches return similar results, which may be redundant. MMR ensures you get not just relevant, but **non-repetitive and diverse** content.

### 📌 Benefits
- High relevance with reduced redundancy
- Better context building for LLMs
- Supports diverse perspectives in results

---

## Multi-Query Retriever

`MultiQueryRetriever` enhances retrieval by generating multiple queries for the same user question using an LLM.

### 📌 Benefits
- Boosts recall by covering different phrasings of the same question
- Captures a broader context of user intent

### 🛠️ Use Cases
- Complex queries with multiple interpretations
- Situations where one query might miss important results

---

## Contextual Compression Retriever

This retriever first gathers documents, then **compresses or filters** them to retain only the most relevant information using a language model or filters.

### 📌 Benefits
- Reduces noise by removing irrelevant chunks
- Increases focus on actionable or informative content
- Efficient for long documents or dense sources

### 🛠️ Use Cases
- Summarization tools
- Precision-focused agents
- Retrieval-augmented generation with limited token space

---

## Other Retrievers

LangChain offers many other retrievers, including:

- **TimeWeightedVectorStoreRetriever**
- **ParentDocumentRetriever**
- **TFIDFRetriever**
- **ElasticSearchBM25Retriever**
- **RemoteLangChainRetriever**
- ...and more!

🔗 **Official LangChain Retriever Documentation**:  
[https://python.langchain.com/docs/modules/data_connection/retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers)

