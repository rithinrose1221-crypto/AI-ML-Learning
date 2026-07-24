
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



from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 

wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
print(df.info())
# df["class"] = wine.target

# X = df.drop("class", axis=1)
# y = df["class"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     train_size=0.2,
#     random_state=42
# )

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)

# print("Enter Wine: ")

# alcohol=float(input("alcohol:"))
# malic_acid=float(input("malic acid:"))
# proline=float(input("proline:"))
# color_intensity=float(input("color intensity:"))

# user_data = pd.DataFrame(
#     [[alcohol,malic_acid,proline,color_intensity]],
#     columns=wine.feature_names
# )

# prediction = model.predict(user_data)
# species = wine.target_names[prediction[0]]

# print("\nPrediction")
# print("wine chemical:", 'class')