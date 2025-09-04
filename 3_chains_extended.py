from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain.schema.runnable import RunnableLambda,RunnableSequence
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatMistralAI(model ="mistral-small")

prompt_template  = ChatPromptTemplate.from_messages(
    [
        ("system","Tell me about this country {x} in short."),
        ("human","Tell me about {count} points."),
    ]
)

uppercase_output = RunnableLambda(lambda x: x.upper())
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words

result = chain.invoke({"x":"Nepal","count":5})

print(result)