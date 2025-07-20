# LangChain Runnables 

This repository provides a structured exploration of LangChain's `Runnable` architecture. It demonstrates the use of task-specific and primitive runnables to build modular, flexible, and composable chains, including examples that utilize LangChain Expression Language (LCEL).

---

## 📘 Runnables

In LangChain, a `Runnable` is an abstraction that represents a unit of computation. It standardizes how different components (such as prompt templates, LLMs, output parsers, and custom functions) can be composed and reused in a pipeline.

---

## ❓ Why Are Runnables Used?

Runnables provide a unified interface for chaining, transforming, branching, and combining logic across various components in LangChain. They enable:

- Composable workflows
- Task-agnostic pipeline building
- Support for synchronous and asynchronous execution
- Debugging and introspection of intermediate steps
- Parallel, sequential, and conditional logic handling

---

## Task-Specific Runnables

These are Runnables built for particular roles in a chain. They often wrap around foundational components like:

- Prompt templates
- Language models (LLMs)
- Output parsers
- Embedding models
- Tool invokers

They help modularize complex agent or chain logic by encapsulating domain-specific behavior.

---

## Runnable Primitives

LangChain provides primitive Runnables to handle different patterns of execution:

1. **Runnable Sequence**  
   Used to execute multiple steps in order, passing the output of one as the input to the next.

2. **Runnable Parallel**  
   Executes multiple runnables concurrently and gathers their outputs as a dictionary.

3. **Runnable Passthrough**  
   Acts as a no-op identity transform — useful as a placeholder or when debugging.

4. **Runnable Lambda**  
   Wraps a simple function into a Runnable-compatible format.

5. **Runnable Branch**  
   Directs execution down different paths based on conditions or input values.

---

## LangChain Expression Language (LCEL)

LCEL is a declarative way to define chains using operator overloading. It simplifies the syntax for composing Runnables into pipelines. LCEL allows clean, intuitive flow construction and supports complex nesting, branching, and error handling.

This repo includes an example using LCEL to demonstrate how it compares with traditional imperative chaining.

---

## Contents of the Repository

- `langchain_aam_zindagi.ipynb` – An approachable walkthrough of `Runnable` concepts using fully custom classes.
- `langchain_pro_zindagi.ipynb` – A deeper look into chaining, conditional logic, and abstractions, still using custom-built components.
- `runnable_branch.py` – Demonstrates conditional routing using `RunnableBranch`.
- `runnable_lambda.py` – Shows functional wrapping via `RunnableLambda`.
- `runnable_parallel.py` – Runs multiple Runnables in parallel.
- `runnable_passthrough.py` – No-op identity runnable.
- `runnable_sequence.py` – Sequential chain of runnable components.
- `runnable_sequence_using_LCEL.py` – Sequence chaining using LangChain Expression Language.
- `.env` – Environment variables for API keys (excluded via `.gitignore`).
- `.gitignore` – Git configuration for ignoring temporary and sensitive files.

---

This repository serves as a hands-on walkthrough for developers learning how to use Runnables effectively in LangChain-powered applications.
