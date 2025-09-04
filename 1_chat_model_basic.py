from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-small")

result  = model.invoke("What is 61 divided by 5")

print("Full result:")
print(result)
print("Content only:")
print(result.content)