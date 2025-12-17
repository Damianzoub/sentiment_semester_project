import joblib 
from data.load_data import load_split
import time 
from metrics.return_metrics import calculate_training_time
from models.pipelines import build_tfidf_svc , build_tfidf_mlp

REVIEW_COL = "review"
LABEL_COL = "label"
VALID_LABELS = ("pos","neg")
PROCESSED_DIR = 'data/processed'
ARTIFACTS_DIR = "artifacts/models"

def train_svc(dataset_name:str='imdb_reviews',model_name:str='svc.pkl',return_time = False):
    train_df, _ = load_split(dataset_name)
    X_train = train_df[REVIEW_COL].astype(str).tolist()
    y_train = train_df[LABEL_COL].astype(str).tolist()
    start_time = time.time()
    build_tfidf_svc.fit(X_train,y_train)
    end_time = time.time()
    model_path = _save_model(build_tfidf_svc,model_name)
    if return_time:
        training_time = calculate_training_time(start_time,end_time)
        return model_path,training_time
    else:
        return model_path

def train_mlp(dataset_name:str='imdb_reviews',model_name:str='mlp.pkl',return_time = False):
    train_df, _ = load_split(dataset_name)
    X_train = train_df[REVIEW_COL].astype(str).tolist()
    y_train = train_df[LABEL_COL].astype(str).tolist()
    start_time = time.time()
    build_tfidf_mlp.fit(X_train,y_train)
    end_time = time.time()
    model_path = _save_model(build_tfidf_mlp,model_name)
    if return_time:
        training_time = calculate_training_time(start_time,end_time)
        return model_path,training_time
    else:
        return model_path


def _save_model(model,model_name:str):
    Path(ARTIFACTS_DIR).mkdir(parents=True,exist_ok=True)
    model_path = Path(ARTIFACTS_DIR)/model_name
    joblib.dump(model,model_path)
    return model_path