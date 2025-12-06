from pathlib import Path 
import pandas as pd 
from sklearn.model_selection import train_test_split
import joblib 

TEXT_COL = "review"
LABEL_COL ="label"
TEST_SIZE=0.2
RANDOM_STATE=42

def load_raw():
    df = pd.read_csv("",encoding='latin-1')
    df = df.drop(columns=['Unnamed: 0','file']).reset_index(drop=True)
    #for now i will not focus on nan values because we don't have 
    return df 

def make_split():
    pass 

def load_split():
    #maybe we can put this if we have in ram the data and we take them fast to make the process faster
    pass