# Tools in LangChain

This repository explores **LangChain Tools**, both built-in and custom, and explains how they integrate into the **agent ecosystem**. It is designed to serve as an **interview prep resource**, a reference guide, and a practical notebook.

---

## What is a Tool?

In LangChain, a **Tool** is a wrapper around a function (or external utility) that an LLM (Large Language Model) can **call** during execution. Tools enable LLMs to interact with the outside world and overcome their inherent limitations.

### What LLMs Can Do

- Reason over a given prompt using in-context knowledge.
- Generate human-like text, answer questions, summarize documents.
- Perform math, logic, and code generation *within limits*.
- Use their "language reasoning" to plan steps.

### ❌ What LLMs Can't Do (Alone)

- Access real-time information (e.g., weather, stock data, search).
- Interact with external APIs or databases.
- Execute code, access the file system, or run shell commands.
- Retain persistent memory across sessions.

### How Tools Fit into the Agent Ecosystem

In **LangChain Agents**, the LLM doesn't just generate text — it decides **which tool to use** based on the prompt and current context. This creates a dynamic loop of:

> User Query → Agent (LLM) → Chooses Tool → Executes Tool → Observes Output → Decides Next Step

This architecture allows the agent to **reason and act**, rather than just respond.

---

## Built-in Tools in LangChain

LangChain provides several **ready-to-use tools** to enable agents to perform common tasks:

### Web & Search Tools

- `DuckDuckGoSearchRun`: Real-time web search.
- `WikipediaQueryRun`: Lookup Wikipedia articles.

### System Tools

- `ShellTool`: Run shell commands (with caution).
- `TerminalTool`: Shell access with prompt safety.

### Data Tools

- `PythonREPLTool`: Execute Python code.
- `SQLDatabaseToolkit`: Interact with SQL databases.

### Utility Tools

- `HumanInputRun`: Ask for human input during execution.
- `RequestsGet/RequestsPost`: Make HTTP requests.
- `VectorStoreQATool`: Query a vector database like FAISS or Chroma.

> 🔗 These can be plugged into agents as-is without custom coding.

---

## Custom Tools

### When to Use Custom Tools

Use a custom tool when:

- You need to **wrap your own business logic** (e.g., querying your API).
- You're interfacing with **private data** (databases, files, models).
- You require **structured input/output validation**.
- You want to build **domain-specific agents**.

Custom tools allow you to define **exact behaviors** that LLMs can invoke in a controlled, testable way.

---

## Ways to Create Custom Tools

LangChain offers **3 primary approaches** to define tools:

---

### 1. `@tool` Decorator

#### Best For:

- Simple functions
- Fast prototyping

#### How it Works:

You decorate any Python function with `@tool`. LangChain extracts the function name, description, input arguments, and wraps it as a callable Tool object.

#### Example Use Case:

```python
@tool
def get_weather(city: str) -> str:
    "Fetches weather information for a city"
    return weather_api(city)
```
### 2. StructuredTool + Pydantic

#### Best For:
Input validation

Clear API contracts

Medium-complexity use cases

#### How it Works:
You define the input schema using Pydantic, and then wrap your function using StructuredTool. This ensures input types are strictly enforced and well-documented.

#### Example Use
```python
class WeatherInput(BaseModel):
    city: str
    units: Optional[str] = "metric"

def get_weather(data: WeatherInput) -> str:
    return fetch_weather(data.city, data.units)

weather_tool = StructuredTool.from_function(fn=get_weather)
```
This tool can now be used safely in environments requiring input sanitation or validation.


### 3. Inheriting from BaseTool Class
#### Best For:
Advanced control

Custom validation, formatting, or async handling

#### How it Works:
You create a class that inherits from BaseTool and implement the name, description, and _run() method (or _arun() for async).

#### Example Use

```python
class CustomWeatherTool(BaseTool):
    name = "custom_weather"
    description = "Fetches detailed weather forecast"

    def _run(self, query: str) -> str:
        return custom_weather_logic(query)
```
This allows full flexibility, including error handling, retries, throttling, etc.

---

## Toolkits
A Toolkit is a collection of tools grouped together for a specific purpose or domain.

### Benefits of Toolkits
Modular: Add/remove tools easily.

Reusable: Share the same set of tools across multiple agents.

Organized: Keep your domain logic clean and composable.

### Common Toolkit Use Cases
| Toolkit              | Purpose                                    |
| -------------------- | ------------------------------------------ |
| `SQLDatabaseToolkit` | For querying relational databases          |
| `VectorStoreToolkit` | For semantic search with vector embeddings |
| `ZapierToolkit`      | Automate actions via Zapier                |
| `BrowserToolkit`     | Automate browsing (experimental)           |
| `JiraToolkit`        | Interact with Jira tickets and workflows   |
| `SlackToolkit`       | Send messages, manage Slack channels       |



#### Real-World Example:
A Customer Support Agent might use:

PythonREPLTool: To calculate billing.

VectorStoreQATool: To fetch internal documentation.

RequestsTool: To access the CRM API.

---

## Custom Toolkits in LangChain

### What is a Custom Toolkit?
A Toolkit in LangChain is a collection of tools grouped together to serve a specific purpose. While LangChain provides built-in toolkits (like SQLDatabaseToolkit), you can also create custom toolkits to package your own tools — especially helpful when you're building domain-specific agents.

`Think of a custom toolkit as a "toolbox" where each tool is tailored to your business or app logic, yet exposed cleanly to your agent.`

### Why Create a Custom Toolkit? 

Custom toolkits are useful when:
- You have multiple related tools (e.g., HR tools, finance tools, e-commerce tools).
- You want to reuse these tools across different agents.
- You want to keep your code modular, maintainable, and scalable.
- You’re building a multi-agent system with role-specific capabilities.

### Real-World Use Cases for Custom Toolkits
| Toolkit Name       | Purpose                                                |
| ------------------ | ------------------------------------------------------ |
| `HRToolkit`        | Fetch employee info, generate payslips, approve leaves |
| `EcommerceToolkit` | Check inventory, update orders, generate invoices      |
| `DevOpsToolkit`    | Trigger builds, deploy services, monitor logs          |
| `ResearchToolkit`  | Search papers, summarize PDFs, extract key insights    |
| `LegalToolkit`     | Draft contracts, search case law, validate clauses     |


---