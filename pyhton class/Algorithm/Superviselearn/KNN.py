
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# import pandas as pd

# iris = load_iris()

# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df.head())
# print(df.info())
# print(df.describe())
# df["species"] = iris.target

# X = df.drop("species",axis = 1)
# y = df["species"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)

# print("\nEnter Flower Details\n")

# sepal_length=float(input("sepal length(cm):"))
# sepal_width=float(input("sepal width(cm):"))
# petal_length=float(input("petal length(cm):"))
# petal_width=float(input("petal width(cm):"))

# user_data = pd.DataFrame(
#     [[sepal_length,sepal_width,petal_length,petal_width]],
#     columns=iris.feature_names
# )

# prediction = model.predict(user_data)
# species = iris.target_names[prediction[0]]

# print("\nPrediction")
# print("flower Species:", species)



# import pandas as pd

# from sklearn.datasets import load_wine
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# # Load dataset
# wine = load_wine()

# X = wine.data
# y = wine.target

# # Split dataset
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42
# )

# # Feature Scaling
# scaler = StandardScaler()

# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train KNN
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, y_train)

# # Evaluate
# y_pred = knn.predict(X_test)

# print("Accuracy:", accuracy_score(y_test, y_pred))

# # ===========================
# # Predict New Wine
# # ===========================

# print("\nEnter the following wine details:")

# new_data = []

# for feature in wine.feature_names:
#     value = float(input(f"{feature}: "))
#     new_data.append(value)

# # Scale the input
# new_data = scaler.transform([new_data])

# # Predict
# prediction = knn.predict(new_data)

# print("\nPredicted Category:", prediction[0])
# print("Class Name:", wine.target_names[prediction[0]])



import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# -----------------------------
# Load Dataset
# -----------------------------
df = sns.load_dataset("titanic")

# -----------------------------
# Handle Missing Values
# -----------------------------
df["age"] = df["age"].fillna(df["age"].median())
df["fare"] = df["fare"].fillna(df["fare"].median())

# -----------------------------
# Encode Gender
# male = 1
# female = 0
# -----------------------------
df["sex"] = df["sex"].map({
    "male": 1,
    "female": 0
})

# -----------------------------
# Select Features
# -----------------------------
X = df[["sex", "age", "fare"]]

# Target
y = df["survived"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Create & Train Model
# -----------------------------
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# -----------------------------
# User Input
# -----------------------------
print("\n===== Titanic Survival Prediction =====")

sex = int(input("Enter Gender (Male=1, Female=0): "))
age = int(input("Enter Age: "))
fare = float(input("Enter Fare: "))

# -----------------------------
# Create DataFrame
# -----------------------------
user_data = pd.DataFrame(
    [[sex, age, fare]],
    columns=["sex", "age", "fare"]
)

# -----------------------------
# Prediction
# -----------------------------
prediction = knn.predict(user_data)

print("\n========== Result ==========")

if prediction[0] == 1:
    print("✅ Passenger Survived")
else:
    print("❌ Passenger Did Not Survive")


# import pandas as pd
# import seaborn as sns

# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import LabelEncoder

# # Load Titanic dataset
# df = sns.load_dataset("titanic")

# # Handle missing values
# df["age"] = df["age"].fillna(df["age"].median())
# df["fare"] = df["fare"].fillna(df["fare"].median())
# df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# # Encode categorical columns
# le = LabelEncoder()

# for col in df.columns:
#     if df[col].dtype == "object" or str(df[col].dtype) == "category":
#         df[col] = le.fit_transform(df[col].astype(str))

# # Select Features
# X = df[["sex", "age", "fare"]]

# # Target
# y = df["survived"]

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# # Train Model
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, y_train)

# # User Input
# print("\nEnter Passenger Details")

# sex = int(input("Gender (Male=1 Female=0): "))
# age = int(input("Age: "))
# fare = float(input("Fare: "))

# user_data = pd.DataFrame(
#     [[sex, age, fare]],
#     columns=X.columns
# )

# prediction = knn.predict(user_data)

# print("\nPrediction")

# if prediction[0] == 1:
#     print("Passenger Survived")
# else:
#     print("Passenger Did Not Survive")

