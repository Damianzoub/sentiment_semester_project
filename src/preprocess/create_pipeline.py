from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC 
from sklearn.neural_network import MLPClassifier
from metrics.return_metrics import return_metrics,calculate_inference_time,calculate_training_time
from sklearn.metrics import classification_report

class PipelineCreation:
    def __init__(self,model_type:str='mlp',random_state:int=42):
        self.model_type = model_type
        self.random_state = random_state
        self.pipeline = self._build_pipeline()
    def _build_pipeline(self):
        if self.model_type == "svm":
            clf = SVC()
        elif self.model_type== "mlp":
            clf = MLPClassifier()
        else:
            raise ValueError("Wrong Model Type")

        pipe = Pipeline([("tfidf",TfidfVectorizer(
            max_features=40000,ngram_range=(1,2),stop_words="english"
        )),(
            "clf",clf
        )])

        return pipe 

    def fit(self,x_train,y_train):
        self.pipeline.fit(x_train,y_train)
        return self
    
    def evaluate(self,x_test,y_test,verbose=True):
        pass

    