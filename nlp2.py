# -*- coding: utf-8 -*-
"""nlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mEiY3PjCzY0fAL44BT9Ml_QCEcgcrw0I
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, RegexpParser

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Read the text from a file
with open('sample_text.txt', 'r') as file:
    text = file.read()

# Tokenization
tokens = word_tokenize(text)

# Stopword removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Regular Expression (Regex) matching
pattern = r'\b[A-Z][a-z]*\b'  # Match proper nouns (words starting with a capital letter)
regex_matches = nltk.regexp_tokenize(text, pattern)

# Part-of-Speech (POS) Tagging
pos_tags = pos_tag(filtered_tokens)

# POS Chunking
grammar = r'''
    NP: {<DT>?<JJ>*<NN>}  # Chunk Noun Phrases
    VP: {<VB.*><NP|PP|CLAUSE>+$}  # Chunk Verb Phrases
'''
chunk_parser = RegexpParser(grammar)
chunked_text = chunk_parser.parse(pos_tags)

# Display the results
print("Original Text:\n", text)
print("\nTokenization:\n", tokens)
print("\nStopword Removal:\n", filtered_tokens)
print("\nStemming:\n", stemmed_tokens)
print("\nLemmatization:\n", lemmatized_tokens)
print("\nRegex Matching (Proper Nouns):\n", regex_matches)
print("\nPOS Tagging:\n", pos_tags)
print("\nPOS Chunking:\n", chunked_text)
