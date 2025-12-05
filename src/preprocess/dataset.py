import pandas as pd 
from sklearn.model_selection import train_test_split
from preprocess_text import clean_html_tags
def train_val_split(df:pd.DataFrame,text_col:str='review',label_col:str='label',test_size=0.2,val_size=0.1,random_state=42):
    df = df.dropna(subset=[''])
    df[text_col] = df[text_col].apply(clean_html_tags)
    if "type" in df.columns:
        train_df = df[df['split']=='train']
        test_df = df[df['split']=='test']
        train_df, val_df = train_test_split(
            train_df,
            test_size=val_size,
            random_state=random_state,
            stratify=train_df[label_col]
        )
    else:
        train_df,test_df = train_test_split(
            df,test_size=test_size,random_state=random_state,stratify=df[label_col]
        )
        train_df,val_df = train_test_split(
            train_df,test_size=val_size,random_state=random_state,stratify=train_df[label_col]
        )
    
    return (
        train_df[text_col],val_df[text_col],test_df[text_col],
        train_df[label_col],val_df[label_col],test_df[label_col]    
    )