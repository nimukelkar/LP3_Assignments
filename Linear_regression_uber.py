
import pandas as pd
import numpy as np
from math import *
from sklearn.metrics import *
from sklearn.preprocessing import *
from sklearn.model_selection import *
from sklearn.linear_model import *


df=pd.read_csv("uber.csv")
print(df.head())

df=df.drop(['Unnamed: 0','key'],axis=1)
print(df.head())

def distance_transform(long1,lat1,long2,lat2):
    travel_dist=[]
    for pos in range(len(long1)):
        lo1,la1,lo2,la2=map(radians,[long1[pos],lat1[pos],long2[pos],lat2[pos]])
        dist_long=lo2-lo1
        dist_lat=la2-la1
        c=dist_long**2+dist_lat**2
        travel_dist.append(c)
    return travel_dist
df['dist_travel_km']=distance_transform(df['pickup_longitude'].to_numpy(),df['pickup_latitude'].to_numpy(),df['dropoff_longitude'].to_numpy()
                                        ,df['dropoff_latitude'].to_numpy())
df=df.dropna(axis=0)
df=df.drop('pickup_datetime',axis=1)

x=df.drop('fare_amount',axis=1)
y=df["fare_amount"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
lrmodel=LinearRegression()
lrmodel.fit(x_train,y_train)
predictedvalues=lrmodel.predict(x_test)
rmse=np.sqrt(mean_squared_error(predictedvalues,y_test))
r2=r2_score(y_test,predictedvalues)
print("r2=",r2)
print("rmse=",rmse)



