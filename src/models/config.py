import os 
from pathlib import Path

MODEL_CONFIG = {
    "test_size":0.2,
    "random_state":42,
    "max_features":5000,
    "ngram_range":(1,2)
}


def load_model():
    model_path = "models/pretrained_model.pkl"
    if not model_path:
        raise ValueError("Model path is not specified.")
    return model_path