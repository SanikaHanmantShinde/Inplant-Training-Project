# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:04:15 2024

@author: Admin
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data=pd.read_csv(r'C:\Users\Admin\heart.csv')

#print(heart_data.hist())
#print(heart_data.head())

#print(last five rows of the dataset)
#heart_data.tail()

#number of rows and columns in the dataset
#heart_data.shape

#getting some info about the data
#heart_data.info()

#checking for missing values
heart_data.isnull().sum()

#statistical measures about the data
heart_data.describe()

#checking the distribution of target variable
heart_data['target'].value_counts()

X=heart_data.drop(columns='target',axis=1)            #store features
Y=heart_data['target']                                #target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,
                                               test_size=0.2,stratify=Y
                                               ,random_state=2)
#proportion of dataset to include in testing split   random state=(split will besame every time)

model=LogisticRegression()

model.fit(X_train,Y_train)

#accuracy on training data
X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

#print('Accuracy on training data:',trining_data_accuracy)

#accuracy on Test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

# print('accuracy on test data:',test_data_accuracy)

input_data = (63,1,3,145,233,1,0,150,0,2.3,0,0,1)

# #change the input data to an numpy array
input_data_as_numpy_array = np.asarray(input_data)

# # Reshape the numpy array as we are predicting for only an instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0] == 0):
   print('The person does not heart disease')
else:
   print('The person has heart disease')



 