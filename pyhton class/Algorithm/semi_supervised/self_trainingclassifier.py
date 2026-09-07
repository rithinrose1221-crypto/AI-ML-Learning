import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix

iris = load_iris()

X = iris.data
y = iris.target

print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)

X_tain, X_test , y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

rng = np.random.RandomState(42)

y_train_semi = np.copy(y_train)

mask = rng.rand(len(y_train_semi)) < 0.70

y_train_semi[mask] = -1

print("Training Samples:", len(y_train))
print("Labeled Samples:", np.sum(y_train_semi != -1))
print("Unlabeled Samples:", np.sum(y_train_semi == -1))

base_classifier = DecisionTreeClassifier(random_state=42)
model = SelfTrainingClassifier(base_classifier)
model.fit(X_tain, y_train_semi)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy : {accuracy:.4f}")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

print(confusion_matrix(y_test, y_pred))


plt.figure(figsize=(7,5))
plt.scatter(
    X_test[:,0],
    X_test[:,1],
    c=y_pred,
    cmap='viridis',
    edgecolors='black'
)

plt.title("Self-Training Classification on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()