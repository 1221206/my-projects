# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 01:14:56 2023

@author: gnana
"""
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

loc = r"C:\Users\gnana\OneDrive - IIT Delhi\SALES.txt"

dataframe = pd.read_csv(loc, sep="\s+", header=None)

# Set display options to show all rows
"""pd.set_option('display.max_rows', None)
print(dataframe.head())  # gives all rows
# only df.head() gives only first five rows """

dataframe.columns = ["Sales", "Advertising"]

#print(dataframe.describe()) gives stats

X= dataframe['Sales'].values
Y= dataframe['Advertising'].values

# plot.scatter(X,Y, color='red', label='Scatter Plot')
# plot.title("sales and adv")
# plot.xlabel('Sales')
# plot.ylabel('Advertising')
# plot.show()

#print(X.shape) = (36,)

X=X.reshape(-1,1)   #-1 for saving exisiting value
Y=Y.reshape(-1,1)

from sklearn.model_selection import train_test_split
X_train, X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.33,random_state=50)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(X_test.shape)

from sklearn.linear_model import LinearRegression

l= LinearRegression()

l.fit(X_train,Y_train)

Y_predic = l.predict(X_test)

plot.scatter(X,Y, color='red', label='Scatter Plot')
plot.plot(X_test,Y_predic,color='blue',label='linear line')
plot.title("sales and adv")
plot.xlabel('Sales')
plot.ylabel('Advertising')
plot.show()
