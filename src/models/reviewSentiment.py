from pydantic import BaseModel

class ReviewIn(BaseModel):
    review:str

class SentimentOut(BaseModel):
    review:str
    sentiment:str