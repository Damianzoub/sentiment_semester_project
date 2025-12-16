from pydantic import BaseModel

class ReviewIn(BaseModel):
    review:str

@dataclass
class SentimentOut(BaseModel):
    review:str
    sentiment:str