import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.metrics import *
from sklearn.preprocessing import *
from sklearn.model_selection import *
from sklearn.metrics import *
from sklearn.linear_model import *

from tensorflow import keras

df1=pd.read_csv("Churn_Modelling.csv")

print(df1.head())
label=LabelEncoder()
df1['Geography']=label.fit_transform(df1['Geography'])
df1['Gender']=label.fit_transform(df1['Gender'])
df1=df1.drop(['RowNumber','Surname'],axis=1)
print(df1.head())

x=df1.drop(['Exited'],axis=1)
y=df1['Exited']

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.2)
model=keras.Sequential(
    [
        keras.layers.Dense(units=25,activation="relu"),
        keras.layers.Dense(units=10,activation="relu"),
        keras.layers.Dense(units=1,activation="sigmoid")
    ]

)
model.compile(loss="binary_crossentropy")
model.fit(x_train,y_train,epochs=100)
model.evaluate(x_test,y_test)
y_preds=model.predict(x_test)
y=[]

for i in y_preds:
    if i>0.5:
        y.append(1)
    else:
        y.append(0)
print(classification_report(y_test,y))
acc_score=accuracy_score(y_test,y)
print("Accuracy score=",acc_score)