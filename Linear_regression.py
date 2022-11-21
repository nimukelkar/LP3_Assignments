from math import radians

import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import *
from sklearn.metrics import *
from sklearn.model_selection import *
from sklearn.preprocessing import *
from sklearn.cluster import *
from sklearn.linear_model import *
from sklearn.ensemble import *


df=pd.read_csv("uber.csv")
#print(df.head())
df=df.drop(['Unnamed: 0','key'],axis=1)
print(df.head())

def dist_transform(longitude1,latitude1,longitude2,latitude2):
    dist=[]
    for i in range(len(longitude1)):
        long1,lati1,long2,lati2=map(radians,[longitude1[i],latitude1[i],longitude2[i],latitude2[i]])
        delta_long=long2-long1
        delta_lati=lati2-lati1
        c=delta_long**2+delta_lati**2
        dist.append(c)
    return dist
df['dist_travel_km']=dist_transform(df['pickup_longitude'].to_numpy(),df['pickup_latitude'].to_numpy(),df['dropoff_longitude'].to_numpy(),
                          df['dropoff_latitude'].to_numpy())
df=df.dropna(axis=0)
df=df.drop('pickup_datetime',axis=1)
print(df.head())

x=df.drop('fare_amount',axis=1)
y=df['fare_amount']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
l=LinearRegression()
l.fit(x_train,y_train)
ypred=l.predict(x_test)
rmse=np.sqrt(mean_squared_error(ypred,y_test))
print("rmse=",rmse)

rfreg=RandomForestRegressor(n_estimators=10)
y_train=y_train.to_numpy()
rfreg.fit(x_train,y_train)
y_pred=rfreg.predict(x_test)

print("r2=",rfreg.score(x_test,y_test))
rfreg_rmse=np.sqrt(metrics.mean_squared_error(y_test,y_pred))
print("Root mean squared error=",rfreg_rmse)