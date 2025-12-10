from sklearn.base import BaseEstimator,TransformerMixin
import re 
class TextCleaner(BaseEstimator,TransformerMixin):
    def fit(self,X,y=None):
        return self 
    
    def transform(self,X):
        return [self._clean(t) for t in X]

    def _clean(self,text:str)->str:
        text = re.sub(r'<br\s*/?>',' ',text)
        text = re.sub(r'<.*?>',' ',text)
        text = re.sub(r'\s+',' ',text).lower().strip()
        return text