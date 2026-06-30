import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

df = pd.read_csv('Mall_Customers.csv')

print("dataframe shape:", df.shape )
print("dataframe head:", df.head(10) )

x = df[['Annual Income (k$)','Spending Score (1-100)']]

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

kmeans = KMeans(n_clusters=3, random_state=42)

clusters = kmeans.fit_predict(x_scaled)

df['Cluster'] = clusters

plt.scatter(x.iloc[:,0], x.iloc[:,1], c=clusters, cmap='viridis')

plt.xlabel('Annual Income ')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation using K-Means Clustering')

plt.show()

def customertype(score):

    if score >=85:
        return 'Platinum'
    elif score>=70:
        return 'Gold'
    elif score>=45:
        return 'Silver'
    else:
        return 'Normal'

df['customer_type'] = df['Spending Score (1-100)'].apply(customertype)

print("dataframe with customer type:", df.head(50) )

plt.figure(figsize=(8,5))
sns.countplot(x='customer_type',data=df)
plt.title("customer type Distribution")

plt.xlabel('cutomer type')
plt.ylabel('count')

plt.show()

