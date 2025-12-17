import os 
from pathlib import Path
from models.train import train_svc,train_mlp
import joblib
#CONST COLUMN NAMES
REVIEW_COL = "review"
LABEL_COL = "label"
VALID_LABELS = ("pos","neg")
PROCESSED_DIR = 'data/processed'
ARTIFACTS_DIR = "artifacts/models"

#NOT SURE YET
MODEL_CONFIG = {
    "test_size":0.2,
    "random_state":42,
    "max_features":5000,
    "ngram_range":(1,2)
}


def load_model(model_name:str='mlp.pkl'):
    model_path = Path(ARTIFACTS_DIR)/f"{model_name}"
    if not model_path:
        model_name = model_name.lower()
        if model_name =="svc.pkl":
            pass
            train_svc()
        elif model_name =="mlp.pkl":
            pass
            train_mlp()
        else:
            raise FileNotFoundError(f"Model file {model_name} not found in {ARTIFACTS_DIR}")
    return joblib.load(model_path)

