# Data Processing Overview

This folder handles **dataset preparation** for text classification models.

The goal is to transform raw text data into **clean, reproducible train/test splits**
that can be reused by different models (SVC, NN, etc.).

---

## End-to-End Flow

Raw Dataset -> Dataset-level cleaning -> train/test split -> save to data/processed -> loaded by model training


---

## Step 1: Dataset-level preprocessing (`preprocessing.py`)

This step fixes **data quality issues** only.

What happens here:
- keep required columns (text + label)
- drop missing values
- normalize labels
- remove invalid labels
- remove empty or very short texts
- remove duplicate reviews

⚠️ No NLP feature engineering is done here.

---

## Step 2: Train / Test split (`load_data.py`)

After cleaning, the dataset is split once and saved to disk:


The split is:
- stratified by label
- reproducible (fixed random seed)

This prevents data leakage and ensures consistent evaluation.

---

## Step 3: Model usage

Training scripts load the prepared splits:

```python
train_df, test_df = load_split("dataset_name")
