

import pandas as pd

from sklearn.metrics import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import *
from sklearn.linear_model import *
from sklearn.model_selection import *
from sklearn import svm

df1=pd.read_csv('emails.csv')
print(df1.head())
x=df1.drop(['Email No.','Prediction'],axis=1)
y=df1['Prediction']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
ss=StandardScaler()
x_train=ss.fit_transform(x_train)
x_test=ss.fit_transform(x_test)

model=svm.SVC()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print(confusion_matrix(y_test,y_pred))
print("Accuracy is",accuracy_score(y_test,y_pred))

# KNN
k1=KNeighborsClassifier(9)
k1.fit(x_train,y_train)
# Predicting
y_predk=k1.predict(x_test)

#Make cm
print("Confusion matrix=",confusion_matrix(y_test,y_predk))
print("Accuracy=",accuracy_score(y_test,y_predk))