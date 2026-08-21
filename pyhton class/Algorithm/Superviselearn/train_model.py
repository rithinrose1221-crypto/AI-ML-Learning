import os
import joblib
import pandas as pd 
import numpy as np

from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split



TRAIN_CSV ="mnist_train.csv"
TEST_CSV ="mnist_test.csv"

MODEL_NAME ="mnist_svm.pkl"

if not os.path.exists(TRAIN_CSV):
    raise FileNotFoundError(f"{TRAIN_CSV} not found!")

if not os.path.exists(TRAIN_CSV):
    raise FileNotFoundError(f"{TEST_CSV} not found!")

print("=" * 60)
print("Loading MNIST Dataset...")
print("=" * 60)

train_df = pd.read_csv(TRAIN_CSV)
test_df = pd.read_csv(TEST_CSV)

print("Training Image :", len (train_df))
print("Testing Image :", len (test_df))

X_train = train_df.iloc[:, 1:].values.astype(np.float32)
y_train = train_df.iloc[:, 0].values
X_test = test_df.iloc[:, 1:].values.astype(np.float32)
y_test = test_df.iloc[:, 0].values

X_train = X_train.astype(np.float32)/255.0
X_test = X_test.astype(np.float32)/255.0

print("\nTraing RBF SVM...")
print("This may take several minutes...")

model = SVC(
    kernel = "rbf",
    C=10,
    gamma=0.001
)

model.fit(X_train, y_train)
print("\nTraining Completed!")

print("\nTesting Model...")
predictons = model.predict(X_test)
accuracy = accuracy_score(y_test, predictons)

print("\nAccuracy : {:.2f}%".format(accuracy * 100))
print("\nClassification Report\n")
print(classification_report(y_test,predictons))

joblib.dump(model, MODEL_NAME)

print("=" * 60)
print("Model Saved Successfully!")
print("Saved As :", MODEL_NAME)
print("=" * 60)

