def route_query(question):

    question = question.lower()

    if "appointment" in question:
        return "tool"

    return "rag"