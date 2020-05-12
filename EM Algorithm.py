import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Dataset8.csv")
df.head()
x=df.iloc[:,1:-1].values
print("x[5]=",x[:5])
from sklearn.preprocessing import LabelEncoder
x[:,0]=LabelEncoder().fit_transform(x[:,0])
print("After Label Encoder:",x[:5])
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
em_cluster=GaussianMixture(n_components=5)
km_cluster=KMeans(n_clusters=5)
em_cluster.fit(x)
km_cluster.fit(x)
em_predictions=em_cluster.predict(x)
km_predictions=km_cluster.predict(x)
print("EM prediction:",em_predictions)
print("K-Means prediction:",km_predictions)
plt.scatter(x[:,1],x[:,2],c=em_predictions)
plt.show()
plt.scatter(x[:,1],x[:,2],c=km_predictions)
#plt.show()
