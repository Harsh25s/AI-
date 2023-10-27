import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the numeric data from the CSV file
data = pd.read_csv('numeric_data.csv')

# Split the data into features (X) and target (y)
X = data.drop('Target', axis=1)
y = data['Target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the Decision Tree model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Replace 'numeric_data.csv' with the path to your own data file. This program loads the data, splits it into training and testing sets, creates a Decision Tree classifier, trains it on the training data, makes predictions on the test data, and calculates the accuracy of the model.
