# Step 1: Import necessary libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 2: Load and split the iris dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42)

# Step 3: Create a decision tree classifier with entropy criterion
clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)

# Step 4: Train the classifier
clf_entropy.fit(X_train, y_train)

# Step 5: Make predictions and evaluate accuracy
y_pred_en = clf_entropy.predict(X_test)
print("Predicted Labels (y_pred_en):")
print(y_pred_en)

accuracy = accuracy_score(y_test, y_pred_en)
print("Accuracy:", accuracy)
