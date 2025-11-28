from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from models.reviewSentiment import ReviewIn , SentimentOut


app = FastAPI(title="Simple analysis API")
templates = Jinja2Templates(directory='app/templates')

@app.get('/health')
def health_check():
    return {"status":"ok"}

@app.post('/predict')
def predict_sentiment(request:ReviewIn)->SentimentOut:
    try:
        pass # Placeholder for sentiment analysis logic
    except Exception as e:
        return {"error":str(e)}


@app.get('/')
def read_root():
    return templates.TemplateResponse('index.html', {'request': {}})

