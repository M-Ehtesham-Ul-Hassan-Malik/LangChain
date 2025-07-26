# AI Agent in LangChain

This repository contains conceptual and practical implementations of **AI Agents using LangChain**, including an example **Weather Agent**. The purpose of this documentation is to provide a **comprehensive, conceptual understanding** of LangChain’s Agent ecosystem.

> For practical code implementations, refer to the Jupyter notebooks included in this repository or consult the [Official LangChain Documentation](https://docs.langchain.com/).

---

## What is an AI Agent?

An **AI Agent** is a system capable of **reasoning, planning, and acting autonomously** to achieve a specific goal. Unlike simple LLM chains, agents can **use tools**, maintain context, and adapt over time.

### Key Characteristics:
- **Goal-Driven**: Operates with a clear task or objective.
- **Autonomous Planning**: Capable of multistep reasoning.
- **Tool-Using**: Can invoke external APIs or tools as needed.
- **Context Awareness**: Maintains a scratchpad or memory to track progress.
- **Adaptive**: Adjusts behavior based on intermediate results or observations.

---

## ReAct Design Pattern

LangChain commonly uses the **ReAct (Reasoning + Acting)** pattern to power agent behavior.

### What is ReAct?

ReAct enables agents to interleave **thoughts** (reasoning) with **actions** (tool use), allowing for more intelligent decision-making.

### ReAct Loop:
```
Thought → Action → Observation → Thought → ... → Final Answer
```


### Benefits:
- Enables dynamic tool usage and reasoning.
- Makes the agent process more transparent and interpretable.
- Supports multi-step problem-solving tasks.

### Reference:
**"Synergizing Reasoning and Acting in Language Models"** (ReAct Paper)

---

## Agent and Agent Executor

LangChain provides the following abstractions for building agents:

### Agent

The **Agent** contains the logic to:
- Interpret user input and context.
- Decide the next action (e.g., call a tool or finish).

### Agent Executor

The **AgentExecutor** handles the full execution lifecycle:
- Receives the user query.
- Routes the agent’s decisions.
- Executes tools and collects results.
- Updates the scratchpad and continues the loop.
- Returns the final output when complete.

Together, they form the **reason-act-observe cycle** in LangChain.

---

## LangChain Hub

**LangChain Hub** is a centralized platform to:
- Share and load prebuilt agents, prompts, and chains.
- Promote reuse and standardization of agent components.

It enables developers to **collaborate** and **rapidly prototype** using curated templates and logic.

---

## Agent Execution Flow in LangChain

The internal lifecycle of an agent execution in LangChain looks like:
```
User Query 
   ↓
Agent Executor 
   ↓
Loop:
   → Pass (User Query + Scratchpad) to Agent
   → Agent Response (Thought, Action)
   → Action Executed via Tool
   → Observation Collected
   → Scratchpad Updated
   → Repeat
Until:
   → Agent decides to finish
   → Return Final Answer
```
This flow illustrates how LangChain allows dynamic reasoning and real-time interaction with external tools, producing a more intelligent and context-aware agent behavior.

---

## Important: LangChain Deprecation of Traditional Agents

LangChain has officially **deprecated** the traditional agent construction APIs and recommends using **LangGraph** for modern, scalable agent development.

### Why LangGraph?
- Enables **stateful, graph-based workflows**.
- Supports **complex multi-agent systems** and branching logic.
- Offers **better performance, observability, and maintainability**.

>  **Note**: This repo uses the older agent approach for learning purposes. For production-ready systems, consider using **LangGraph**.

---

## Included Example

The included Jupyter notebook demonstrates:
- A practical implementation of LangChain Agent.
- A simple **Weather Agent** example that uses external tools to fetch weather data.

Explore the notebook to see how the concepts from this documentation come together in practice.

---

## Resources

- [LangChain Docs](https://docs.langchain.com/)
- [LangChain Hub](https://smith.langchain.com/hub)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [LangGraph](https://docs.langchain.com/langgraph/)

---

## Final Notes

This documentation is intended to offer a clear conceptual roadmap to AI Agents in LangChain. Whether you're a beginner exploring the agent ecosystem or a practitioner looking to understand agent workflows, this resource provides the foundational knowledge you need.

For real-world use cases and experimentation, refer to:
- The included notebook(s) in this repo
- LangChain’s growing ecosystem including LangGraph and LangChain Hub

Happy Building! 