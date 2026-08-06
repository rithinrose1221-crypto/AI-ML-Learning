import os
import cv2
import joblib
import numpy as np
import time

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


TRAIN_PATH = "dataset/train"
TEST_PATH = "dataset/test"

MODEL_NAME = "dog_cat_model.pkl"


if not os.path.exists(TRAIN_PATH):
    raise FileNotFoundError(f"Training folder not found: {TRAIN_PATH}")

if not os.path.exists(TEST_PATH):
    raise FileNotFoundError(f"Testing folder not found: {TEST_PATH}")


def load_images(folder):

    images = []
    labels = []

    for label in os.listdir(folder):

        class_folder = os.path.join(folder, label)

        if not os.path.isdir(class_folder):
            continue

        print(f"Loading {label} images...")

        for file in os.listdir(class_folder):

            if not file.lower().endswith((".jpg", ".jpeg", ".png")):
                continue

            image_path = os.path.join(class_folder, file)

            image = cv2.imread(image_path)

            if image is None:
                continue

            # Resize image
            image = cv2.resize(image, (64, 64))

            # Convert to grayscale
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Normalize
            image = image.astype(np.float32) / 255.0

            # Flatten image
            image = image.flatten()

            images.append(image)
            labels.append(label)

    return np.array(images), np.array(labels)


print("=" * 60)
print("Loading Cat vs Dog Dataset...")
print("=" * 60)

X_train, y_train = load_images(TRAIN_PATH)
X_test, y_test = load_images(TEST_PATH)

print("\nTraining Images :", len(X_train))
print("Testing Images  :", len(X_test))

print("\nTraining SVM Model...")
print("Please wait...\n")

start = time.time()

model = SVC(
    kernel="rbf",
    C=10,
    gamma=0.001
)

model.fit(X_train, y_train)

end = time.time()

print("Training Completed!")
print(f"Training Time : {end-start:.2f} seconds")


print("\nTesting Model...")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy : {:.2f}%".format(accuracy * 100))

print("\nClassification Report\n")
print(classification_report(y_test, predictions))


joblib.dump(model, MODEL_NAME)

print("\nModel Saved Successfully!")
print("Model Name :", MODEL_NAME)

print("=" * 60)
print("Training Finished Successfully!")
print("=" * 60)