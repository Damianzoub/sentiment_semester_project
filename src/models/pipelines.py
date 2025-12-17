from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC 
from sklearn.neural_network import MLPClassifier
from models.preprocess_text import TextCleaner

def build_tfidf_svc():
    return Pipeline([(
        "cleaner",TextCleaner(),
    ),(
        "tfidf",TfidfVectorizer(
            ngram_range=(1,2),
            max_features=40000,
            stop_words="english"
        )
    ),(
        "svc",SVC()
    )])

def build_tfidf_mlp():
    return Pipeline([(
        "cleaner",TextCleaner()
    ),(
        "tfidf",TfidfVectorizer(
            ngram_range=(1,2),
            max_features=40000,
            stop_words="english"
        )
    ),("mlp",MLPClassifier(
        hidden_layer_sizes=(256,128,64),
        activation='relu',
        solver='adam',
        learning_rate='adaptive',
        alpha=1e-3,
        batch_size=64,
        max_iter=50,
        random_state=42
    ))])