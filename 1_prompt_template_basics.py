from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# template = "Tell me a joke about {topic}"
# prompt_tmeplate = ChatPromptTemplate.from_template(template)

messages = [
    ("system","You are a comedian who tells jokes about {topic}."),
    ("human","Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"lawyers","joke_count": 3})
print("----Prompt with system and human messsages (Tuple)-----")
print(prompt)