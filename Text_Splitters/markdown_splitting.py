from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
# 🌐 Personal Website Starter

Welcome to your personal website project! This repository helps you build and deploy a **basic personal website** using **HTML**, **CSS**, and **GitHub Pages** — no frameworks or backend needed.

---

## 📌 Features

- Fully responsive layout (basic)
- Sections for:
  - About Me
  - Projects
  - Contact
- Hosted for free with GitHub Pages
- Easy to customize

---

## 🧰 Tech Stack

- **HTML5**
- **CSS3**
- **GitHub Pages** (for hosting)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/yourusername.github.io
cd yourusername.github.io
```

## 2. Project Structure
personal-website/
│
├── index.html      # Main HTML file
├── style.css       # Styling file
└── README.md       # You’re reading this!

##  Deploy on GitHub Pages
### 1. Push your code to GitHub:
```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/yourusername.github.io
git push -u origin main
```

"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=500,
    # chunk_overlap=200, 
)

result = splitter.split_text(text)

print(result)
print()
print(len(result))
print()
print(result[2])


