import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import LabelPropagation
from sklearn.metrics import accuracy_score, classification_report

digits = load_digits()

X = digits.data
y = digits.target

print("Number of Samples:",len(X))
print("Number of Features:", X.shape[1])
print("Target Classes :", digits.target_names)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

rng = np.random.RandomState(42)
y_train_semi = np.copy(y_train)
mask = rng.rand(len(y_train)) < 0.70
y_train_semi[mask] = -1

print("Training Samples :", len(y_train))
print("Labeled Samples :", np.sum(y_train_semi !=-1))
print("Unlabeled Samples :", np.sum(y_train_semi !=-1))

model = LabelPropagation(
    kernel='knn',
    n_neighbors=7
)
model.fit(X_train, y_train_semi)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print(classification_report(
    y_test,
    y_pred
))

plt.figure(figsize=(8,6))

plt.scatter(
    X_test[:,0],
    X_test[:,1],
    c=y_pred,
    cmap='tab10',
    edgecolors='black'
)
plt.title("Label Propagation on Digits Dataset")
plt.xlabel("Pixel Feature 1")
plt.ylabel("Pixel Feature 2")
plt.show()
