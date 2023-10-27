import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
import re

# Download NLTK data for stopwords and lemmatization
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Read the text file
with open('sample_text.txt', 'r') as file:
    text = file.read()

# Tokenization (sentence and word)
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Stopword Removal
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# Regular Expressions
pattern = r'\b[A-Za-z]{4,}\b'  # Match words with 4 or more letters
regex_words = re.findall(pattern, text)

# Part-of-Speech (POS) Tagging
pos_tags = pos_tag(filtered_words)

# Print the results
print("Original Text:")
print(text)

print("\nTokenization (Sentences):")
print(sentences)

print("\nTokenization (Words):")
print(words)

print("\nStopword Removal:")
print(filtered_words)

print("\nStemming:")
print(stemmed_words)

print("\nLemmatization:")
print(lemmatized_words)

print("\nRegular Expressions:")
print(regex_words)

print("\nPart-of-Speech (POS) Tagging:")
print(pos_tags)

# Make sure to create a text file named 'sample_text.txt' containing the text you want to analyze. This program will perform the mentioned NLP tasks on the text and display the results.
