from pydantic import BaseModel #feild


class QuestionRequest(BaseModel):

    question: str
    #question: str = Field(...,strict=True)