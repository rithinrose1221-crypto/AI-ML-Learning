import numpy as np 

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

data = load_breast_cancer()

X = data.data
y = data.target

print("Feature Names:")
print("data.feature_names")

print("Target Names:")
print(data.target_names)

X_train, X_test, y_train, y_test = train_test_split(
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

labeled = y_train_semi != -1
unlabeled = y_train_semi == -1

clf1 = DecisionTreeClassifier(random_state=1)
clf2 = DecisionTreeClassifier(random_state=2)
clf3 = DecisionTreeClassifier(random_state=3)

for iteration in range(5):
    
    clf1.fit(X_train[labeled], y_train[labeled])
    clf2.fit(X_train[labeled], y_train[labeled])
    clf3.fit(X_train[labeled], y_train[labeled])
    
    if np.sum(unlabeled) == 0:
        break
    
unlabeled_indices = np.where(unlabeled)[0]

pred1 = clf1.predict(X_train[unlabeled])
pred2 = clf2.predict(X_train[unlabeled])
pred3 = clf3.predict(X_train[unlabeled])

for i, idx in enumerate(unlabeled_indices):
    if pred1[i] == pred2[i]:
        y_train[idx] = pred1[i]
        labeled[idx] = True
        unlabeled[idx] = False
    elif pred1[i] == pred3[i]:
        y_train[idx] = pred1[i]
        labeled[idx] = True
        unlabeled[idx] = False
    elif pred2[i] == pred3[i]:
        y_train[idx] = pred1[i]
        labeled[idx] = True
        unlabeled[idx] = False
        
pred1 = clf1.predict(X_test)
pred2 = clf2.predict(X_test)
pred3 = clf3.predict(X_test)
final_prediction = []
for p1, p2, p3 in zip(pred1, pred2, pred3):
    
    if p1 == p2 or p1 == p3:
        final_prediction.append(p1) 
    else:
        final_prediction.append(p2)
final_prediction = np.array (final_prediction)

accuracy = accuracy_score(y_test, final_prediction)

print(f"Accuracy: {accuracy:.4f}")
print(classification_report(
    y_test, 
    final_prediction,
    target_names=data.target_names
))