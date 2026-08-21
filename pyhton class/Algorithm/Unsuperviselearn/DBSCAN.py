import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

dataset = sns.load_dataset("penguins")

dataset = dataset.dropna()

print(dataset.head())
print(dataset.shape)
print(dataset.info())
print(dataset.describe())

X = dataset[
    [
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g"
    ]
]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

dbscan = DBSCAN(
    eps=0.7,
    min_samples=5
)

clusters = dbscan.fit_predict(X_scaled)

dataset["Cluster"] = clusters
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
plt.figure(figsize=(8,6))
plt.scatter(
    X_pca[:,0],X_pca[:,1],
    c=clusters,cmap="rainbow",
    s=80,
    edgecolors="black"
)

print(
    dataset[[
        "species","bill_length_mm",
        "bill_depth_mm","flipper_length_mm",
        "body_mass_g","Cluster"
    ]
].head(10)
)
print("\nDBSCAN Cluster Completed Successfully!")
plt.title("DBMSCAN Clustering - Penguins Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.grid(True)
plt.show()

print(dataset["Cluster"].value_counts().sort_index())

num_clusters = len(set(clusters)) - (1 if - 1 in clusters else 0)
noise_points = list(clusters).count(-1)

print("Number of Cluster :", num_clusters)
print("Number of Noise Point :", noise_points)