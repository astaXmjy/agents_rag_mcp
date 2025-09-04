from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model = "mistral-small")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a comedian who tell jokes about {topic}"),
        ("human","Tell me {joke_count} jokes."),
    ]
)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic":"lawyers","joke_count":3})

print(result)