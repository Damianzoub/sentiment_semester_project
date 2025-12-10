from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from models.reviewSentiment import ReviewIn , SentimentOut


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
        pred = model.predict(review)
        label_map = {0:'neg',1:'pos'}

        return SentimentOut(sentiment,score) # or just make it return {"text":review}
    except Exception as e:
        return {"error":str(e)}


@app.get('/')
def read_root():
    return templates.TemplateResponse('index.html', {'request': {}})

