from app.llm import generate_answer

question = {
                "Can patients request medication refill through telehealth?"
}

result = generate_answer(question)

print("\nANSWER:\n")
print(result["answer"])

print("\nSOURCES:\n")
print(result["sources"])

print("\nCONFIDENCE:\n")
print(result["confidence"])