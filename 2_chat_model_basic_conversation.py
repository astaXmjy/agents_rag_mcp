from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small")

# messages =  [
#     SystemMessage(content="Solve the following math problem"),
#     HumanMessage(content="What is 81 divided by 9"),
# ]

# result = model.invoke(messages)
# print(f"Answer from AI: {result.content}")

messages = [
    SystemMessage(content="Solve the following math problem"),
    HumanMessage(content="What is 81 divided by 9"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?")
]

result  = model.invoke(messages)

print(f"Answer from AI: {result.content}")