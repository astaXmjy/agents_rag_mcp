from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model  = ChatMistralAI(model = "mistral-small")

chat_history = []

system_message = SystemMessage(content="You are my crush Deeksha.")
chat_history.append(system_message)

while True:
    query = input("Bol: ")
    if query.lower() == "soja":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)

    response = result.content
    chat_history.append(AIMessage(response))

    print(f"Deeksha(Crush): {response}")

print("....moon soja....")
print(chat_history)