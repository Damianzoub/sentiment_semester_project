import pandas as pd
import numpy as np 
#for now we let it like this 

def clean_dataset(dataset:pd.DataFrame,review_col:str='review',label_col:str="label",valid_labels=("pos","neg"),min_words:int=3):
    dataset = dataset.copy()
    dataset = dataset[[review_col,label_col]]
    dataset = dataset.dropna(subset=[review_col,label_col])
    dataset[review_col] = dataset[review_col].astype(str)
    dataset[label_col] = dataset[label_col].astype(str).str.strip().str.lower() #making the labels the same
    dataset = dataset[dataset[label_col]].isin(valid_labels)
    text = dataset[review_col].str.strip()
    dataset = dataset[dataset[review_col].str.split().str.len() >= min_words]

    dataset = dataset.drop_duplicates(subset=[review_col])
    return dataset.reset_index(drop=True)