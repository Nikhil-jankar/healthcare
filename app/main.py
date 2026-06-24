from fastapi import FastAPI

from app.schemas import QuestionRequest

from app.rag import ingest_documents

from app.llm import generate_answer
from app.router import route_query
from app.tools import check_appointment_slots


app = FastAPI(
    title="Healthcare AI Assistant"
)

@app.get("/health")
def health_check():

    return {

        "status":"healthy"

    }
    
@app.post("/ingest")
def ingest():

    ingest_documents()

    return {

        "message":
        "Documents indexed successfully"

    }
@app.post("/ask")
def ask_question(request: QuestionRequest):

    route = route_query(
        request.question
    )

    if route == "tool":

        department = "cardiology"

        if "neurology" in request.question.lower():
            department = "neurology"

        elif "orthopedics" in request.question.lower():
            department = "orthopedics"

        return check_appointment_slots(
            department
        )

    return generate_answer(
        request.question
    )