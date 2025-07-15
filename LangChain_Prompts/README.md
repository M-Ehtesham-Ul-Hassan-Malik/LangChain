# LangChain Prompts Overview

This repository serves as a conceptual guide to **prompts in LangChain**, one of the most critical components in building intelligent applications using large language models (LLMs). It outlines key ideas around prompt design, structure, and message management in LangChain.

---

## What Are Prompts?

Prompts are the inputs or instructions given to a language model to guide its output. They define what the model should do, such as answering a question, translating text, summarizing a document, or engaging in a conversation. In LangChain, prompts are modular and reusable, making them easy to manage in both simple and complex applications.

---

## 📌 Static vs Dynamic Prompts

LangChain supports two types of prompts:

- **Static Prompts** are hardcoded and unchanging. They are useful for fixed queries or when the input doesn’t vary across sessions.

- **Dynamic Prompts** use placeholders that are filled in at runtime. These prompts are flexible and scalable, making them ideal for applications where the input changes based on user interaction or context.

---

## 🧩 Prompt Template

A **Prompt Template** is a structured way of creating prompts using variables. Instead of writing out the full prompt every time, a template allows you to define a reusable structure where values can be injected dynamically. This improves modularity and consistency, especially in applications that require varied user inputs or task instructions.

---

## Messages

LangChain uses a message-based format to communicate with chat models like OpenAI’s GPT-3.5/4 or Google’s Gemini. Each message has a specific role, such as:

- **System Message**: Sets the behavior or personality of the model.
- **Human Message**: Represents the user's input.
- **AI Message**: Represents the model's response.

This structure supports multi-turn conversations, enabling the model to maintain context across interactions.

---

## ChatPromptTemplate

The **ChatPromptTemplate** is designed for chat-based language models. It allows you to create structured prompts consisting of multiple message types (system, human, AI). This makes it easier to build contextual and conversational AI agents that respond accurately based on previous exchanges.

The template supports variable injection, allowing you to customize messages for different users or domains while maintaining a consistent structure.

---

## Message Placeholder

A **Message Placeholder** is used to insert previous conversation history or dynamic content into a prompt at runtime. This is especially useful for chatbots and assistants that need to remember past interactions to generate coherent and context-aware responses. It ensures that the model has access to relevant background information while responding to new inputs.

---

## Summary

LangChain’s prompt system offers a robust framework for building powerful LLM applications. By using prompt templates, structured messages, and placeholders, developers can craft precise, dynamic, and context-aware prompts that improve the performance and reliability of language models.

---

Feel free to explore this repository to understand how these concepts are implemented and used in practice.
