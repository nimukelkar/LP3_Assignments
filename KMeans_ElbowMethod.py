
import pandas as pd
from sklearn.metrics import *
from sklearn.preprocessing import *
from sklearn.cluster import *
import seaborn as sns
import matplotlib.pyplot as plt

df1=pd.read_csv('sales_data_sample.csv',encoding="latin1")
print(df1.head())

#Get required columns only
df1=df1[["PRICEEACH","QUANTITYORDERED"]]
print(df1.head())


sc=StandardScaler()

scaled=sc.fit_transform(df1)


inertia=[]

for i in range(1,11):
    model=KMeans(n_clusters=i,init="k-means++")
    model.fit(scaled)
    inertia.append(model.inertia_)
ks=[1,2,3,4,5,6,7,8,9,10]
sns.lineplot(x=ks,y=inertia)
plt.show()