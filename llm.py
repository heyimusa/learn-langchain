from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=1,
    max_tokens=1000,
)

response = llm.stream(["Write a poem about ai"])

# Corrected variable name from 'chuck' to 'chunk'
for chunk in response:
    print(chunk.content, end="", flush=True)
