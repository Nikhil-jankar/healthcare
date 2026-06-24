from app.llm import llm

response = llm.invoke("What is AI?")

print(response.content)