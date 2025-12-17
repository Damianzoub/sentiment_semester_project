from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from models.reviewSentiment import ReviewIn , SentimentOut
from models.config import load_model

model = load_model() #base parameter model_name:str='svc.pkl' we can also put  nn.pkl

app = FastAPI(title="Simple analysis API")
templates = Jinja2Templates(directory='app/templates')
# not sure yet model = get_model() 
@app.get('/health')
def health_check():
    return {"status":"ok"}

@app.post('/predict')
def predict_sentiment(request:Request,review:str= Form(...)):
    try:
        
        pred= model.predict([review])[0] # or just make it return {"text":review}
        label_map = {0:"neg",1:"pos"}
        sentiment = label_map.get(pred,str(pred))
        return templates.TemplateResponse("index.html",{
            "request":request,
            "review":review,
            "sentiment":sentiment
        })
    except Exception as e:
        return {"error":str(e)}


@app.get('/')
def read_root():
    return templates.TemplateResponse('index.html', {'request': {}})

