import pandas as pd 
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from pathlib import Path
from src.data.preprocess import clean_dataset

def read_csv_fallback(file_path:str):
    try:
        return pd.read_csv(file_path,encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(file_path,encoding='latin-1')

def load_data(file_path:str)->pd.DataFrame:
    try:
        data = read_csv_fallback(file_path=file_path)
        data = data.drop(columns=['Unnamed: 0','file']).reset_index(drop=True)
        return data 
    except Exception as e:
        print(f"Error loading data: {e}")
        raise ValueError("Failed to load data from the specified file path.")
#not sure for this function    

def make_and_save_split(df:pd.DataFrame,dataset_name:str,review_col:str='review',label_col:str='label',valid_labels=("pos","neg"),test_size:float=0.2,seed:int=42,min_words:int=3):
    df = clean_dataset(
        df,
        review_col=review_col,
        label_col=label_col,
        valid_labels=valid_labels,
        min_words=min_words
    )
    df = df[[review_col,label_col]].copy()
    df = df[label_col].isin(valid_labels)
    train_df ,test_df = train_test_split(df,test_size=test_size,random_state=seed,stratify=df[label_col])

    base = Path("data/processed")/dataset_name
    (base/"train").mkdir(parents=True,exist_ok=True)
    (base/"test").mkdir(parents=True,exist_ok=True)

    train_df.to_csv(base/"train"/"train.csv",index=False)
    test_df.to_csv(base/"test"/"test.csv",index=False)

def load_split(dataset_name:str):
    base = Path('data/processed')/dataset_name
    train_df = pd.read_csv(base/"train"/"train.csv")
    test_df = pd.read_csv(base/"test"/"test.csv")
    return train_df,test_df