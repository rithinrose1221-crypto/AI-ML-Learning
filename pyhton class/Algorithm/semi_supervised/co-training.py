import numpy as np

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


wine = load_wine()

X = wine.data
y = wine.target

print("Feature Names:")
print(wine.feature_names)

print("\nTarget Names:")
print(wine.target_names)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


X_train_view1 = X_train[:, :6]
X_train_view2 = X_train[:, 6:]

X_test_view1 = X_test[:, :6]
X_test_view2 = X_test[:, 6:]

rng = np.random.RandomState(42)
ytrain_semi = np.copy(y_train)
mask = rng.rand(len(ytrain_semi)) < 0.70
ytrain_semi[mask] = -1


print("\nTraining Samples:", len(y_train))
print("Labeled Samples :", np.sum(ytrain_semi != -1))
print("Unlabeled Samples :", np.sum(ytrain_semi == -1))


clf1 = DecisionTreeClassifier(random_state=42)
clf2 = DecisionTreeClassifier(random_state=42)


for iteration in range(5):

    print(f"\nIteration {iteration + 1}")

    labeled = ytrain_semi != -1
    unlabeled = ytrain_semi == -1

    clf1.fit(
        X_train_view1[labeled],
        ytrain_semi[labeled]
    )

    clf2.fit(
        X_train_view2[labeled],
        ytrain_semi[labeled]
    )

    if not np.any(unlabeled):
        break

    unlabeled_indices = np.where(unlabeled)[0]

    prob1 = clf1.predict_proba(
        X_train_view1[unlabeled]
    )

    prob2 = clf2.predict_proba(
        X_train_view2[unlabeled]
    )

    conf1 = np.max(prob1, axis=1)
    conf2 = np.max(prob2, axis=1)

    for idx, confidence in zip(unlabeled_indices, conf1):
        if confidence > 0.90 and ytrain_semi[idx] == -1:

            prediction = clf1.predict(
                X_train_view1[idx].reshape(1, -1)
            )[0]

            ytrain_semi[idx] = prediction

    labeled = ytrain_semi != -1
    unlabeled = ytrain_semi == -1

    if np.any(unlabeled):
        unlabeled_indices = np.where(unlabeled)[0]

        for idx, confidence in zip(unlabeled_indices, conf2):
            if confidence > 0.90:

                prediction = clf2.predict(
                    X_train_view2[idx].reshape(1, -1)
                )[0]

                ytrain_semi[idx] = prediction


pred1 = clf1.predict(X_test_view1)
pred2 = clf2.predict(X_test_view2)


final_prediction = []

for p1, p2 in zip(pred1, pred2):

    if p1 == p2:
        final_prediction.append(p1)
    else:
        final_prediction.append(p1)
        
final_prediction = np.array(final_prediction)


accuracy = accuracy_score(
    y_test,
    final_prediction
)

print("\nAccuracy: {:.4f}".format(accuracy))

print("\nClassification Report:\n")

print(classification_report(
        y_test,
        final_prediction,
        target_names=wine.target_names
))