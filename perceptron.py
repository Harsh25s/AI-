import numpy as np

# Define the training data (features X1 and X2) and corresponding labels (0 or 1)
X = np.array([[1, 2], [2, 3], [2, 1], [3, 4], [4, 3], [3, 1]])
y = np.array([0, 0, 0, 1, 1, 1])

# Define the perceptron class
class Perceptron:
    def __init__(self, num_features):
        self.weights = np.zeros(num_features + 1)  # Weights for features + bias
        self.learning_rate = 0.1

    def predict(self, inputs):
        # Activation function (Step function)
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0

    def train(self, training_data, labels, epochs):
        for _ in range(epochs):
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Create a perceptron with two input features
perceptron = Perceptron(num_features=2)

# Train the perceptron on the training data for a specified number of epochs
perceptron.train(X, y, epochs=100)

# Test the perceptron with new data
test_data = np.array([[1, 1], [5, 5], [2, 3], [3, 2]])
for data_point in test_data:
    prediction = perceptron.predict(data_point)
    print(f"Input: {data_point}, Prediction: {prediction}")

# In this program, we define a simple Perceptron class with methods for prediction and training. The train method updates the weights based on the provided training data. After training, we use the perceptron to make predictions on new data points.

# This example demonstrates a basic binary classification problem using a perceptron. You can modify the training data and test data to solve other classification tasks.
