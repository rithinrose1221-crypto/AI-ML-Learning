import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# ==============================
# Load Dataset
# ==============================
dataset = pd.read_csv("Mall_Customers.csv")

print("First 5 Rows:")
print(dataset.head())

# ==============================
# Select Features
# ==============================
X = dataset.iloc[:, [3, 4]].values

# ==============================
# Create Dendrogram
# ==============================
plt.figure(figsize=(12, 6))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distance")

dendrogram(linkage(X, method="ward"))

plt.show()

# ==============================
# Apply Hierarchical Clustering
# ==============================
hc = AgglomerativeClustering(
    n_clusters=5,
    metric="euclidean",
    linkage="ward"
)

y_pred = hc.fit_predict(X)

# ==============================
# Store Cluster Numbers
# ==============================
dataset["Cluster"] = y_pred

# ==============================
# Find Average Income & Spending
# ==============================
cluster_summary = dataset.groupby("Cluster")[["Annual Income (k$)", "Spending Score (1-100)"]].mean()

print("\nAverage Values for Each Cluster")
print(cluster_summary)

# ==============================
# Create Meaningful Labels
# ==============================
cluster_labels = {}

for cluster in cluster_summary.index:

    income = cluster_summary.loc[cluster, "Annual Income (k$)"]
    spending = cluster_summary.loc[cluster, "Spending Score (1-100)"]

    if income >= 70 and spending >= 60:
        label = "High Income, High Spending"

    elif income >= 70 and spending < 40:
        label = "High Income, Low Spending"

    elif income < 40 and spending >= 60:
        label = "Low Income, High Spending"

    elif income < 40 and spending < 40:
        label = "Low Income, Low Spending"

    else:
        label = "Average Income, Average Spending"

    cluster_labels[cluster] = label

# Add labels to dataset
dataset["Customer Type"] = dataset["Cluster"].map(cluster_labels)

# Convert cluster numbering from 0-4 to 1-5
dataset["Cluster"] = dataset["Cluster"] + 1

# ==============================
# Print Cluster Information
# ==============================
print("\nCluster Labels")

for i in sorted(cluster_labels.keys()):
    print(f"Cluster {i+1}: {cluster_labels[i]}")

# ==============================
# Plot Clusters
# ==============================
colors = ["red", "blue", "green", "cyan", "magenta"]

plt.figure(figsize=(10, 7))

for i in range(5):
    plt.scatter(
        X[y_pred == i, 0],
        X[y_pred == i, 1],
        s=80,
        color=colors[i],
        label=cluster_labels[i]
    )

plt.title("Hierarchical Clustering of Mall Customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.grid(True)
plt.show()

# ==============================
# Display Results
# ==============================
print("\nFirst 20 Customers with Cluster Labels")
print(dataset.head(20))

# ==============================
# Save Results
# ==============================
output_file = "Mall_Customers_Hierarchical_Result.csv"
dataset.to_csv(output_file, index=False)

print(f"\nResults saved as '{output_file}'")