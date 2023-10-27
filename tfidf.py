import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the text data from a CSV file
data = pd.read_csv('text_data.csv')  # Replace with your own CSV file

# Split the data into features (text) and target (labels)
X = data['text']
y = data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a CountVectorizer
count_vectorizer = CountVectorizer()
X_train_count = count_vectorizer.fit_transform(X_train)
X_test_count = count_vectorizer.transform(X_test)

# Create a TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Create a Naïve Bayes classifier
naive_bayes_count = MultinomialNB()
naive_bayes_tfidf = MultinomialNB()

# Train the Naïve Bayes classifiers
naive_bayes_count.fit(X_train_count, y_train)
naive_bayes_tfidf.fit(X_train_tfidf, y_train)

# Make predictions on the test data
y_pred_count = naive_bayes_count.predict(X_test_count)
y_pred_tfidf = naive_bayes_tfidf.predict(X_test_tfidf)

# Calculate accuracy for CountVectorizer and TFidfVectorizer
accuracy_count = accuracy_score(y_test, y_pred_count)
accuracy_tfidf = accuracy_score(y_test, y_pred_tfidf)

print("Accuracy (CountVectorizer):", accuracy_count)
print("Accuracy (TfidfVectorizer):", accuracy_tfidf)

# Make sure to replace 'text_data.csv' with the path to your own CSV file containing text data and labels. This program loads the data, splits it into training and testing sets, applies CountVectorizer and TfidfVectorizer to convert text into numerical features, creates Naïve Bayes classifiers, trains them on the vectorized data, and calculates the accuracy for both vectorization methods.
