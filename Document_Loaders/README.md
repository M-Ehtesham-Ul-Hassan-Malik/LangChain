# Document_Loaders – LangChain

This repository explores various **document loaders** in [LangChain](https://www.langchain.com/), which are essential tools for loading, parsing, and structuring external data into a format that language models can work with.
```
Document_Loaders/
│
├── .env                  # Environment variables (e.g., API keys if needed)
├── .gitignore            # Ignoring system/cache files and .env
│
├── CSVLoader.py          # Loads documents from CSV files
├── DirectoryLoader.py    # Loads multiple files from a directory
├── text_loader.py        # Loads plain text files
├── PyPDFLoader.py        # Loads data from PDF documents
├── WebBaseLoader.py      # Loads content from web URLs
```

---

## Document Loaders in LangChain

Document loaders transform content from different sources (files, URLs, directories, etc.) into `Document` objects. These objects can then be passed into LangChain chains, retrievers, or agents for further processing.

### Load vs Lazy Load

- **Load**: Eagerly loads all documents at once.
- **Lazy Load**: Loads documents one by one as needed. Useful when handling large directories or working with streaming pipelines.

---

## TextLoaders

Text loaders are designed to handle plain `.txt` files. These are ideal for simple, unstructured textual content, offering a fast and straightforward way to load data.

---

## PyPDFLoader

This is LangChain’s default loader for handling PDF files. It works well for extracting simple text from each page and is easy to integrate into pipelines.

---

## PDF Loaders Comparison

Different types of PDFs (scanned documents, structured layouts, etc.) require different loaders. Below is a comparison of available PDF loaders in LangChain:

| Loader                    | Best For                          | Notes                                                   |
|---------------------------|-----------------------------------|----------------------------------------------------------|
| `PyPDFLoader`             | Simple text extraction            | Default choice; fast and easy to use                     |
| `PDFPlumberLoader`        | Tables, multi-column layouts      | More accurate layout parsing                             |
| `PyMuPDFLoader`           | Performance and better formatting | Fast, good for preserving text structure                 |
| `UnstructuredPDFLoader`   | Complex documents with formatting | Most powerful, but requires extra setup                  |
| `AmazonTextractPDFLoader` | Scanned/image-based PDFs          | Uses AWS Textract for OCR; ideal for forms and invoices  |

---

## DirectoryLoader

`DirectoryLoader` loads all supported document files within a directory. It is helpful when working with large collections of files for batch processing.

---

## WebBaseLoader

This loader fetches and parses webpage content. It is helpful when you want to extract real-time or static content from URLs, such as blogs, articles, or documentation.

---

## CSVLoader

This loader is designed for `.csv` files. It reads tabular data and converts each row into a document. Ideal for handling structured data like datasets, records, or form submissions.

---

## Limitations

While LangChain document loaders are powerful, they each come with certain limitations:

- **TextLoaders**: Cannot handle formatting, metadata, or embedded content. Best for simple `.txt` files only.
- **PyPDFLoader**: May struggle with complex layouts (e.g., tables or multi-columns) and ignores scanned images.
- **PDFPlumberLoader**: Better for layout-heavy PDFs but slower and less robust for plain text extraction.
- **PyMuPDFLoader**: Preserves layout well but may require tuning for performance and memory usage.
- **UnstructuredPDFLoader**: Requires additional dependencies and setup; best for complex formatting, but heavier to run.
- **AmazonTextractPDFLoader**: Requires AWS credentials and setup. Works only with scanned/image-based PDFs and may incur costs.
- **DirectoryLoader**: Can consume memory quickly in eager loading mode with many large files.
- **WebBaseLoader**: Depends on the structure of the target website. May break if HTML structure changes. Some sites may block scraping.
- **CSVLoader**: Assumes a well-formatted CSV file. Might require schema adaptation for inconsistent rows or missing headers.

