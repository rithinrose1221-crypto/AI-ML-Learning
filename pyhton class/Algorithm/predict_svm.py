import os
import cv2
import joblib
import numpy as np

MODEL_NAME = "dog_cat_model.pkl"

if not os.path.exists(MODEL_NAME):
    raise FileNotFoundError("Model not found!")

model = joblib.load(MODEL_NAME)

print("=" * 50)
print("CAT VS DOG PREDICTOR")
print("=" * 50)

image_path = input("Enter Image Path : ")

if not os.path.exists(image_path):
    raise FileNotFoundError("Image not found!")

image = cv2.imread(image_path)

if image is None:
    raise Exception("Cannot read image!")

# Keep original for display
display = image.copy()

# Resize image
image = cv2.resize(image, (64,64))

# Convert to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Normalize
image = image.astype(np.float32) / 255.0

# Flatten
image = image.reshape(1,-1)

prediction = model.predict(image)[0]

print("\nPrediction :", prediction)

cv2.imshow("Uploaded Image", display)
cv2.waitKey(0)
cv2.destroyAllWindows()