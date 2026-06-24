from pathlib import Path

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from app.rag import retrieve_context
from app.logger import logger
from app.config import MODEL_NAME


llm = ChatOllama(
    model=MODEL_NAME,
    temperature=0,
    base_url="http://host.docker.internal:11434"
)


prompt = PromptTemplate(
    template="""
You are a healthcare AI assistant.

Rules:

1. Answer ONLY using the provided context.
2. Never guess information.
3. If the answer is unavailable, reply:

"I could not find this information in the provided documents."

4. Do not provide medical diagnosis or treatment advice.
5. Keep responses professional.

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)


def generate_answer(question):

    logger.info(f"Question received: {question}")

    context, docs = retrieve_context(question)

    logger.info(f"Retrieved {len(docs)} docs")

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)

    answer = response.content.strip()

    logger.info("Answer generated")

    if "I could not find" in answer:

        return {
            "answer": answer,
            "sources": [],
            "confidence": "low"
        }

    sources = []

    for doc in docs:

        source = Path(doc.metadata["source"]).name

        if source not in sources:
            sources.append(source)

    if len(sources) == 1:
        confidence = "high"

    elif len(sources) == 2:
        confidence = "medium"

    else:
        confidence = "low"

    return {
        "answer": answer,
        "sources": sources,
        "confidence": confidence
    }