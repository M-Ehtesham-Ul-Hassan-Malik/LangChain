# Text Splitters in LangChain

This repository demonstrates various **text splitting techniques** using LangChain. Text splitting is a foundational step in building scalable, context-aware applications powered by Large Language Models (LLMs).

---

## What is Text Splitting?

**Text Splitting** refers to the process of dividing large documents or long blocks of text into smaller, manageable chunks. These chunks can then be processed more effectively by LLMs for tasks like summarization, semantic search, question answering, and document retrieval.

---

## Why is Text Splitting Needed for LLM-Powered Applications?

LLMs like GPT-4, Claude, and Gemini have **context window limits** (e.g., 8K, 32K, 128K tokens), which restrict how much input they can process in one go. Text splitting helps address several key challenges:

### 1. Overcoming Model Limitations
- LLMs can't process entire books, PDFs, or long articles at once.
- Splitting text ensures that all relevant information is passed in chunks that fit within the model's context window.

### 2. Enabling Downstream Tasks
- Tasks like retrieval-augmented generation (RAG), summarization, or answering questions require documents to be chunked for precise search and response.
- Splitting improves **accuracy**, **latency**, and **relevance** of downstream tasks.

### 3. Optimizing Computational Resources
- Smaller chunks reduce token usage and cost.
- Increases throughput for parallel processing or caching.

---

## 1. Length-Based Splitting

This is the most basic form of splitting where text is divided by a fixed number of characters.

### ✅ Benefits
- Easy to implement.
- Fast and language-agnostic.
- Useful for uniform-sized documents (e.g., logs, transcripts).

### ❌ Limitations
- May break sentences or paragraphs mid-way.
- Can lead to context loss or incoherent chunks.
- Not structure-aware.

---

## 2. Text-Structured Based Splitting

This approach uses LangChain's **RecursiveCharacterTextSplitter** to chunk text by intelligently preserving structure.

### Recursive Character Text Splitter
- Attempts to split at larger structural boundaries first (e.g., paragraphs → sentences → words).
- Falls back to smaller separators when needed.

### ✅ Benefits
- Preserves meaning better than simple length-based splitting.
- Ideal for prose, blog posts, and stories.
- More readable and natural chunks.

### ❌ Limitations
- Not suitable for structured code or data files.
- Might still split mid-sentence if structure is weak.

---

## 3. Document-Based Splitting

This approach splits input by **logical documents** (like pages or sections) using document loaders (e.g., PDFs, Word, Markdown files).

### ✅ Benefits
- Preserves document integrity.
- Works well with loaders like `PyPDFLoader` for PDFs or `DirectoryLoader` for file systems.
- Suitable for chunking multi-page reports, forms, books.

### ❌ Limitations
- Might result in uneven chunk sizes.
- Page boundaries may not align with logical content boundaries.

---

## 4. Semantic Meaning-Based Splitting

This advanced method uses **embeddings** to split based on semantic meaning, rather than structure or length. Implemented via `SemanticChunker` in `langchain_experimental`.

### ✅ Benefits
- Chunks are meaning-aware.
- Highly effective for deep search, semantic retrieval, and Q&A systems.
- Preserves coherence and intent of each section.

### ❌ Limitations
- Slower and more resource-intensive.
- Requires high-quality embeddings (e.g., Google Generative AI).
- Results may not be satisfying at this stage. Experimental and may improve with LangChain updates.

---

## Summary Table

| Splitter Type              | Benefits                                              | Limitations                                                    |
|---------------------------|-------------------------------------------------------|----------------------------------------------------------------|
| Length-Based              | Fast, simple                                          | Can cut mid-sentence, poor context preservation                |
| Text-Structured (Recursive) | Structure-aware, readable chunks                    | May not work well with unstructured text or code               |
| Document-Based            | Maintains page/section integrity                      | May have inconsistent chunk sizes                              |
| Semantic-Based            | Meaning-aware, ideal for RAG/Q&A                      | Slower, experimental, not always accurate                      |

---

## Final Notes

Text splitting is not one-size-fits-all. The **choice of splitter depends on your use case**:
- Use **Length-Based** for simple tasks and uniform documents.
- Use **Recursive** for blogs or stories.
- Use **Document-Based** for multi-page inputs.
- Use **Semantic Splitting** when meaning and coherence matter most.

This repository contains examples of all the above splitters to help you evaluate and choose the right one for your LangChain projects.
