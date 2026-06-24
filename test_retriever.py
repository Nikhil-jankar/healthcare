from app.rag import get_retriever

retriever = get_retriever()

question = "Can patients request medication refill through telehealth?"

docs = retriever.invoke(question)

print(f"Found {len(docs)} docs\n")

for i, doc in enumerate(docs, start=1):

    print("="*60)

    print(f"Document {i}")

    print()

    print(doc.page_content)

    print()

    print(doc.metadata)