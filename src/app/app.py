from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from src.models.reviewSentiment import ReviewIn , SentimentOut
from src.models.config import load_model

model = load_model()

app = FastAPI(title="Simple analysis API")
templates = Jinja2Templates(directory='app/templates')
# not sure yet model = get_model() 
@app.get('/health')
def health_check():
    return {"status":"ok"}

@app.post('/predict')
def predict_sentiment(request:ReviewIn)->SentimentOut:
    try:
        
        review = request['review'] #from textarea name in index.html
        pred = model.predict(review)[0]
        label_map = {0:'neg',1:'pos'}
        sentiment = label_map[pred]
        return SentimentOut(review,sentiment) # or just make it return {"text":review}
    except Exception as e:
        return {"error":str(e)}


@app.get('/')
def read_root():
    return templates.TemplateResponse('index.html', {'request': {}})

