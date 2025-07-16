# LangChain Structured Output

This repository demonstrates multiple methods to generate structured outputs using LangChain with OpenAI and Gemini models. It includes examples using `TypedDict`, `Pydantic`, and raw `JSON Schema`.

---

## What is Structured Output?

Structured output refers to extracting information in a **defined, machine-readable format** such as a dictionary, JSON object, or data model instead of plain text. It ensures predictable responses that can be parsed, displayed, or stored programmatically.

---

## Why Do We Need Structured Output ?

- ✅ To make LLM outputs **easy to parse and use**
- ✅ To enforce **consistent formats**
- ✅ To reduce **ambiguity** for downstream logic
- ✅ To enable **direct integration** with databases, APIs, or UI components

---

## 🛠️ Ways to Get Structured Output

LangChain supports structured output via:

1. **TypedDict** — Native Python type hints
2. **Pydantic** — Python models with validation
3. **JSON Schema** — Schema definitions in JSON
4. **`with_structured_output()`** — LangChain’s utility to bind any of the above to LLM output

---

## 🔧 `with_structured_output`

This LangChain method links a schema (TypedDict, Pydantic, or JSON Schema) with a model so that the output follows the defined structure. It simplifies post-processing by returning model outputs in a predictable format.

---

## TypedDict

Python’s `TypedDict` is used to define the structure of dictionaries. In LangChain, it works well with OpenAI models to represent lightweight schemas.

- ✅ Easy to use
- ❌ No runtime validation
- ✅ Supports basic descriptions with `Annotated`

---

## Pydantic

`Pydantic` provides robust data validation using Python type hints. It's ideal when you need field validation (like ranges, enums, optional fields).

- ✅ Type and format validation
- ✅ Supports descriptive metadata
- ❌ Not supported with Gemini models

---

## JSON Schema

JSON Schema defines structure in a language-agnostic way. It's required for models like **Gemini** that don't support Python typing natively.

- ✅ Required for Google models (e.g., Gemini)
- ✅ Portable and flexible
- ❌ More verbose and manual to write

---

## When to Use What?

| Use Case                        | Recommended Schema |
|---------------------------------|--------------------|
| OpenAI with simple schemas      | `TypedDict`        |
| OpenAI with validation needs    | `Pydantic`         |
| Gemini or Google models         | `JSON Schema`      |
| Want field descriptions         | `Annotated` + `TypedDict` or `Pydantic` |

---

## ⚠️ Few Things to Remember

- `TypedDict` and `Pydantic` only work with **OpenAI** models.
- Use **JSON Schema** when working with **Gemini**.
- `with_structured_output()` requires proper model compatibility.
- Use `Annotated[...]` or `Field(...)` to guide LLMs more effectively.
- Always test your schema on real input for best results.

---

Example files in this repo:
- `pydantic_demo.py`: Pydantic model usage
- `typeddict_demo.py`: TypedDict structure
- `with_structured_output_json.py`: Gemini with JSON Schema
- `with_structured_output_pydantic.py`: OpenAI with Pydantic
- `with_structured_output_typedDict.py`: OpenAI with TypedDict
- `with_structured_output_annotated.py`: Annotated TypedDict

---

Feel free to contribute or explore different structured output methods with your preferred models!
