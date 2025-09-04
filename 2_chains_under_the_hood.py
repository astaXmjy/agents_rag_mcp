from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain.schema.runnable import RunnableLambda,RunnableSequence

load_dotenv()

model = ChatMistralAI(model ="mistral-small")

prompt_template  = ChatPromptTemplate.from_messages(
    [
        ("system","Tell me about this country {x} in short."),
        ("human","Tell me about {count} points."),
    ]
)

format_prompt = RunnableLambda(lambda x:prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x:model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x:x.content)

chain = RunnableSequence(first=format_prompt,middle=[invoke_model],last=parse_output)

response = chain.invoke({"x":"china","count":4})

print(response)