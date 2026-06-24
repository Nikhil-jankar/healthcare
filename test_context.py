from app.rag import retrieve_context

question = "Can patients request medication refill through telehealth?"

context, docs = retrieve_context(question)

print(context)