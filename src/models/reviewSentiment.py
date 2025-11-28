from pydantic import BaseModel

class ReviewIn(BaseModel):
    review:str

class SentimentOut(BaseModel):
    sentiment:str
    score:float