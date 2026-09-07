import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA

dataset = pd.read_csv('Wholesale customers data.csv')
print("=" * 60)
print("Wholesale Customers Dataset")
print("=" * 60)
print("\nFirst 5 Record\n")
print(dataset.head())

print("\nDataset Shape :",dataset.shape)

X = dataset[
    [
        "Fresh",
        "Milk",
        "Grocery",
        "Frozen",
        "Detergents_Paper",
        "Delicassen"
    ]
]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = IsolationForest(
    contamination = 0.05,
    random_state=42
)

dataset["Outlier"] = model.fit_predict(X_scaled)

print("\nOutlier Distribution\n")

print(dataset["Outlier"].value_counts())

normal = (dataset["Outlier"] == 1).sum()
outliers = (dataset["Outlier"] == -1).sum()

print("\nNormal Customers :", normal)
print("Outlier Customer :", outliers)

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10,7))

plt.scatter(
    X_pca[dataset["Outlier"] == 1,0],
    X_pca[dataset["Outlier"] == 1,1],
    color = "dodgerblue",
    s = 45,
    alpha = 0.7,
    label = "Normal Customer"
)

print("\nIsolation Forest Completed")


plt.scatter(
     X_pca[dataset["Outlier"] == -1,0],
        X_pca[dataset["Outlier"] == -1,1],
        color = "red",
        s = 120,
        marker = "X",
        edgecolors = "black",
        label = "Outlier Customer"
)

plt.title("Isolation Forest - Outlier Detection")
plt.xlabel("Principal Component 1")
plt.ylabel("principal Component 2")


plt.legend()
plt.grid(True, linestyle="--", alpha = 0.5)
plt.show()
print("\nFrist 10 Customers\n")
print(
    dataset[
        [
            "Fresh",
            "Milk",
            "Grocery",
            "Frozen",
            "Detergents_Paper",
            "Delicassen",
            "Outlier"
        ]
    ].head(10)
)