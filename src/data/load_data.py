import pandas as pd 
import numpy as np

def read_csv_fallback(file_path:str):
    try:
        

def load_data(file_path:str)->pd.DataFrame:
    try:
        data = pd.read_csv(file_path,encoding='utf-8')
        return data 
    except Exception as e:
        print(f"Error loading data: {e}")
        raise ValueError("Failed to load data from the specified file path.")