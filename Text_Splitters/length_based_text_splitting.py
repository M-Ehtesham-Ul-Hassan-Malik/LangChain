from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text = """
# Six months ago, I met a shopkeeper in Karachi — Rafiq Bhai.
# He had been running his small retail store for over 15 years.

# One evening, while having chai outside his shop, he said to me,
# “Beta, I have an idea… an app that could help me manage my stock, maybe even sell online. But I don’t know how to explain it. Developer walay technical baatain samajhtay hain… main sirf soch sakta hoon.”

# He had spoken to three different developers.
# Each one asked for a scope document, wireframes, technical requirements…
# But he had none of that. Just a vision.
# He tried.
# He waited.
# But eventually… he gave up.

# That day, I realized — he’s not alone.

# There are thousands of Rafiq Bhai’s across Pakistan.
# People with ideas that could become real businesses.
# Ideas that could improve lives.
# Ideas that could grow Pakistan’s tech ecosystem.

# But they don’t have the words developers need.
# And that gap... kills potential.

# That’s why we built Nexovate.

# Nexovate starts with simple questions — just like a friend would.
# Then, it gives the user a space to describe their idea, in their own words.
# Our AI reads it, understands it, and generates a complete scope document —
# A blueprint developers can use to start building.

# The best part?
# That scope document is completely free.

# And if the user wants to go further, Nexovate connects them with verified Pakistani developers — to build their mobile app, website, or custom software.

# Nexovate isn’t just a platform.
# It’s a voice for the unheard.
# It’s a bridge —
# Between dreamers and builders,
# Between ideas and action.

# Our vision is simple:
# To empower every Pakistani with an idea to become a creator — not just a consumer.

# Because the next great product might not come from Silicon Valley...
# It might come from someone like Rafiq Bhai.
# It might come from a small shop in Korangi,
# From a woman in Gilgit,
# From a student in Sialkot...

# If only we give them the tools to speak tech.

# All they need is a way to be heard.
# And that... is what Nexovate does.
# """



loader = PyPDFLoader('Java Interview Questions.pdf')

docs = loader.lazy_load()

splitter = CharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=0,
    separator=''
)

# result = splitter.split_text(text)
result = splitter.split_documents(docs)

# print(result)
print()
print(result[11].page_content)


