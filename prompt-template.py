from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Instantiate Model
llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo-1106",
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI chef. Create a unique recipe based on the follow main ingredient."),
        ("human", "{input}")
    ]
)

# Create LLM Chain
chain = prompt | llm

response = chain.invoke({"input" : "tomatoes"})
print(response)
