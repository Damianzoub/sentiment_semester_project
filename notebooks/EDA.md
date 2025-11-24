Exploratory Data Analysis for IMDB Review Sentiment Project
 Overview

This EDA explores the IMDB movie review dataset, which contains:

review text

sentiment label: positive, negative, unsup

type: train, test

The goal is to understand the structure, distribution, and linguistic characteristics of the data before building sentiment-classification models (SVM and neural networks).

## 1. Dataset Structure & Basic Checks
### 1.1 Missing Values

Checking for missing reviews or labels ensures model training is reliable and no corrupted rows exist.

### 1.2 Duplicate Reviews

Duplicate text can bias the model by repeating the same content multiple times.
Removing duplicates helps maintain balanced, clean training data.

### 1.3 Type & Label Distribution

I examined the distribution of:

train vs test samples

positive vs negative vs unsup labels

This shows how balanced the dataset is, which affects model fairness and performance.

## 2. Review Length Analysis
### 2.1 Character and Word Length Distribution

I computed:

number of characters per review

number of words per review

Why this matters

Very long reviews may contain multi-topic content → noisy for classification

Very short reviews may lack clear sentiment

Models like SVM, TF-IDF, or neural networks are sensitive to extreme lengths

Helps choose preprocessing strategies (truncation, padding)

### 2.2 Outlier Detection

Long reviews (6000–7000+ characters) were identified as outliers.

I kept them instead of removing them because:

they still contain meaningful opinion text

removing 7–8% of data would reduce training diversity

models can handle long sequences after preprocessing (truncation or max_length setting)

## 3. N-gram Analysis (Unigrams, Bigrams, Trigrams)

N-grams are sequences of words:

unigram = 1 word

bigram = 2 words

trigram = 3 words

### ✔️ 3.1 What I extracted

Most frequent unigrams overall

Most frequent bigrams & trigrams

Most frequent n-grams per class (positive vs negative)

### ✔️ Why I did this

Sentiment often appears in phrases, not single words

Patterns like “not good”, “waste of time”, “highly recommended” reveal true sentiment

N-grams highlight context, negation, sarcasm, and common expressions

Helps understand which phrases strongly discriminate between positive and negative reviews

Useful for future model features (TF-IDF + n-grams)

## 4. Word Cloud Visualization

I generated word clouds for:

positive reviews

negative reviews

### Why I did this

Word clouds give an instant visual understanding of:

the most frequent opinion-bearing words

differences between positive and negative vocabulary

whether preprocessing is working (stopwords, HTML tags, punctuation)

dominant thematic expressions in each label

This step provides a quick linguistic snapshot of sentiment patterns.

## 5. Part-of-Speech (POS) Analysis

Using POS tagging, I analyzed:

adjectives (ADJ)

adverbs (ADV)

verbs (VERB)

nouns (NOUN)

### Why I did this

Sentiment is heavily expressed through:

adjectives (great, terrible, boring, amazing)

adverbs (extremely, very, barely)

opinion verbs (love, hate, enjoy, dislike)

Understanding POS patterns helps reveal:

how positive vs negative reviews differ in linguistic style

which types of words dominate emotionally

features that may improve model performance (e.g., adjective counts)

## 6. Comparative Analysis Between Positive and Negative Reviews

I compared:

 6.1 Average review length per label

Positive and negative reviews often differ in verbosity.

 6.2 Discriminative Words

Using TF-IDF and frequency ratios to find words strongly associated with each sentiment class.

 6.3 Sentiment-Lexicon Counts

Using opinion lexicons, I counted positive and negative sentiment words inside each review.

Why this matters

Highlights the core vocabulary that signals each sentiment

Confirms dataset behaves as expected (positive reviews should contain more positive words, etc.)

Helps guide feature engineering and preprocessing

## 7. Summary of Insights

The EDA revealed:

The dataset is mostly balanced between positive and negative labels.

Review length varies widely; long reviews should be truncated for modeling.

Positive reviews frequently use praise-related adjectives; negative reviews use complaint-based verbs and strong negative adjectives.

N-gram patterns clearly differentiate sentiment (“not good”, “waste of time” vs “highly recommend”, “very enjoyable”).

Word clouds visually confirmed sentiment vocabulary.

POS analysis showed adjectives/adverbs are key sentiment carriers.

## 8. How This EDA Helps the Modeling Stage

The EDA directly informs the next steps:

TF-IDF with n-grams is useful for SVM

Sequence length decisions for NN models

Removing noise (HTML, symbols, long punctuation)

Feature selection guided by POS and discriminative words

Detection of common sentiment phrases for improved preprocessing

This analysis provides a strong foundation for building robust sentiment classification models.
