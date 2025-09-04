from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

load_dotenv()

model  = ChatMistralAI(model = "mistral-small")

template = "Tell me joke about {topic}"
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic":"cats"})

result = model.invoke(prompt)

print(result.content)