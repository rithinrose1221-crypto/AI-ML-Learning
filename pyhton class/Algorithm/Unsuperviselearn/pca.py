import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

wine = load_wine()

X = wine.data
y = wine.target

print(wine.feature_names)
print(X.shape)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

pca = PCA(n_components = 2)
X_pca = pca.fit_transform(X_scaled)

print("Original Dataset shape:", X.shape)
print("Reduced Dataset Shape :", X_pca.shape)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_)*100)

plt.figure(figsize = (8,6))
scatter =  plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c = y,
    cmap="viridis",
    s = 80,
    edgecolors="black"
)

plt.title("PCA - WINE Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(
    handles = scatter.legend_elements()[0],
    labels = list(wine.target_names),
    title = "Wine Class"
)

plt.grid(True)
plt.show()

print("\nFirst 10 Reduced Data points\n")
for i in range(10):
    print(
        f"Sample{i+1:2d}:"
        f"PC1 = {X_pca[i,0]:8.3f}"
        f"PC2 = {X_pca[i,1]:8.3f}"

)

print("\nPCA Completed Successfully!")