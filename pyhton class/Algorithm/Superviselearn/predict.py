import os
import cv2
import joblib
import numpy as np
import matplotlib.pyplot as plt

MODEL_NAME = "mnist_svm.pkl"
IMAGE_SIZE = 28

print("=" * 60)
print("    MNIST DIGIT PREDICTOR")
print("=" * 60)

if not os.path.exists(MODEL_NAME):
    raise FileNotFoundError("mnist_svm.pkl not found!")

model = joblib.load(MODEL_NAME)
print("Model Loaded Successfully!")

print("\nExample:")
print("digit.png")

image_path = input("\nEnter Image Path: ").strip()

if not os.path.exists(image_path):
    raise FileNotFoundError("Image not found!")

image = cv2.imread(image_path)

if not os.path.exists(image_path):
    raise Exception("Cannot read image.")

display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (5,5), 0)

_, binary = cv2.threshold(
gray,
0,
255,
cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

kernel = np.ones((3,3), np.uint8)
binary = cv2.morphologyEx(
binary,
cv2.MORPH_CLOSE,
kernel,
iterations=2
)


contours, _ = cv2.findContours(
binary,
cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE
)

if len(contours) == 0:
    raise Exception("No digit detected!")

largest = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest)
digit = binary[y:y+h, x:x+w]


size = max(w, h)
canvas = np.zeros((size, size), dtype=np.uint8)
x_offset = (size - w) // 2
y_offset = (size - h) // 2
canvas[y_offset:y_offset+h, x_offset:x_offset+w] = digit

h, w = canvas.shape

if h > w:
    new_h = 20
    new_w = int(w * 20 / h)
else:
    new_w = 20
    new_h = int(h * 20 / w)
    
canvas = cv2.resize(canvas, (new_w, new_h))

final = np.zeros((28,28), dtype=np.uint8)
x = (28 - new_w) // 2
y = (28 - new_h) // 2
final[y:y+new_h, x:x+new_w] = canvas

moments = cv2.moments(final)

if moments["m00"] != 0:
    cx = int(moments["m10"] / moments["m00"])
    cy = int(moments["m01"] / moments["m00"])
    shift_x = 14 - cx
    shift_y = 14 - cy
    M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    final = cv2.warpAffine(final, M, (28, 28), borderValue=0)
    
sample = final.astype(np.float32)
sample /= 255.0
sample = sample.reshape(1, -1)

prediction = model.predict(sample)[0]

decision = model.decision_function(sample)
if decision.ndim == 1:
    confidence = 100 / (1 + np.exp(-abs(decision[0])))
else:
    confidence = 100 / (1 + np.exp(-np.max(decision)))
    
print("\nPrediction :", prediction)
print("Confidence : {:.2f}%".format(confidence))

count = 1
while os.path.exists(f"predicted_img_{count}.png"):
    count += 1
save_name = f"predicted_img_{count}.png"

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(display_image)
plt.title("Uploaded Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(final, cmap="gray")
plt.title(f"Processed MNIST Image\nPrediction : {prediction}")
plt.axis("off")

plt.tight_layout()
plt.savefig(save_name, dpi=300)
plt.show()

print("\nSaved :", save_name)
print("=" * 60)
print("Prediction Completed Successfully!")
print("=" * 60)
print("Predicted Digit :", prediction)
print("Confidence : {:.2f}%".format(confidence))
print("Saved Image :", save_name)
print("=" * 60)