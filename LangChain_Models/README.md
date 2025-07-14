# Models in LangChain

In **LangChain**, “models” refer to the core language models and related components that power the interactions, reasoning, and generation capabilities of your application. These models typically include:

1. LLMs (Large Language Models)  
2. Chat Models  
3. Embedding Models  

---

## Language Models

Language Models are AI systems designed to process, generate, and understand natural language text.

### 1. LLMs

LLMs (Large Language Models) are general-purpose models used for raw text generation.  
- **Input:** A string (plain text)  
- **Output:** A string (plain text)  
- These are traditionally older models and are less commonly used in modern applications compared to chat models.

### 2. Chat Models

Chat Models are a specialized type of LLMs designed for conversational tasks.  
- **Input:** A sequence of messages (e.g., a chat history)  
- **Output:** A structured chat message  
- These models are newer and are more commonly used in production environments.

### 3. Embedding Models

Embedding Models convert text into numerical vectors.  
- These vectors can be used for:
  - Similarity search  
  - Retrieval-Augmented Generation (RAG) pipelines  
  - Semantic comparisons  
- Common providers include OpenAI, Hugging Face, and Cohere.

---

>LangChain standardizes these models under a unified interface so they can be easily integrated and swapped in your applications.

