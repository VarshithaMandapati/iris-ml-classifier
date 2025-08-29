# iris_classifier.py
# Machine Learning with scikit-learn (Iris Dataset)
# Author: Your Name
# Description: Trains a Decision Tree on the Iris dataset, prints accuracy,
#              predicts a sample, and saves results to iris_output.txt.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    # 1. Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # 2. Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Initialize and train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # 4. Predictions
    y_pred = model.predict(X_test)

    # 5. Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Model Accuracy:", round(accuracy, 4))

    # 6. Test with sample input
    sample = [[5.1, 3.5, 1.4, 0.2]]  # Example measurements
    prediction = model.predict(sample)
    predicted_species = iris.target_names[prediction][0]

    print("Predicted species:", predicted_species)

    # 7. Save output to text file
    with open("iris_output.txt", "w") as f:
        f.write(f"Model Accuracy: {accuracy:.4f}\n")
        f.write(f"Predicted species: {predicted_species}\n")

if __name__ == "__main__":
    main()
