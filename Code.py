# Program for demonstration of one hot encoding

# import libraries
import numpy as np
import pandas as pd

# import the data required
data = pd.read_csv('data/employee_data.csv')
print(data.head())



print(data['gender'].unique())
print(data['employment_status'].unique())

#Using pd.get_dummies() function from pandas to one-hot encode the categorical columns
one_hot_encoded_data = pd.get_dummies(data, columns = ['employment_status', 'gender'])
print(one_hot_encoded_data)
