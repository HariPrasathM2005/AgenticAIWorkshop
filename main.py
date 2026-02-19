import os
api_key=os.getenv("GRQ_API_KEY","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")
print(f"API Key: {api_key}")

#from langchain_groq import ChatGroq

def add(a,b):
    """Add two numbers"""
    return a+b

def subtract(a,b):
    """Subtract two numbers"""
    return a-b


'''llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=api_key,
)

if __name__ == "__main__":
    msg=input("I am AI: ")
    messages=[
    ("system","You arew a helpful assistant."),
    ("user",msg)
    ]'''
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

os.environ["GROQ_API_KEY"]=api_key


agent=create_agent("groq:llama-3.1-8b-instant",tools={add,subtract})
agent_response=agent.invoke({"messages":[
    HumanMessage(content="add 4,5 and subtract 10,2")]}
    )

print("Agent Response: ",agent_response["messages"][-1].content)