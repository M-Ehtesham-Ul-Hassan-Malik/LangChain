from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model
# model = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     temperature=0
# )

# Initialize the Google Generative AI model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0
)

st.header("Research Tool")
st.write("This tool allows you to interact with a research assistant powered by OpenAI's language model.")


paper_input = st.selectbox(
    "Select a research paper",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners", "RoBERTa: A Robustly Optimized BERT Pretraining Approach", "Diffusion Models Beat GANs on Image Synthesis", "DALL-E: Creating Images from Text", "CLIP: Connecting Text and Images", "AlphaFold: Using AI for Protein Folding", "Reformer: The Efficient Transformer", "T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"],
)

style_input = st.selectbox(
    "Select a style for the response",
    ["Formal", "Informal","Code-Oriented", "Technical", "Conversational"],
)

length_input = st.selectbox(
    "Select the length of the response",
    ["Short", "Medium", "Long"],
)

# template
# template = PromptTemplate(
# template=""" 
# Please summarize the research paper titled "{paper_input}" with the following
# specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1. Mathematical Details:
# - Include relevant mathematical equations if present in the paper.
# - Explain the mathematical concepts using simple, intuitive code snippets
# where applicable.
# 2. Analogies:
# - Use relatable analogies to simplify complex ideas.
# If certain information is not available in the paper, respond with: "Insufficient
# information available" instead of guessing.
# Ensure the summary is clear, accurate, and aligned with the provided style and
# length.
# """,
# input_variables=["paper_input", "style_input", "length_input"],
# validation_template=True
# )


# Load the prompt template from the saved JSON file
template = load_prompt("research_paper_prompt_template.json")

# fill the placeholders with user input
prompt = template.invoke(
    {
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
    }
)

if st.button("Generate Summary"):
    st.text("Processing your request...")
    result = model.invoke(prompt)
    st.success("Response:")
    st.write(result.content)
else:
    st.text("Click the button to generate a summary based on your selections.")