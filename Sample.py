import os
api_key=os.getenv("GRQ_API_KEY","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")
print(f"API Key: {api_key}")

from langchain_groq import ChatGroq

def add(a,b):
    """Add two numbers"""
    return a+b

def subtract(a,b):
    """Subtract two numbers"""
    return a-b

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=api_key,
)

if __name__ == "__main__":
    msg=input("I am AI: ")
    messages=[
    ("system","You arew a helpful assistant."),
    ("user",msg)
    ]

    lim_with_tools=llm.bind_tools([add,subtract])
    response=llm.invoke(messages)
    print(response.content)
