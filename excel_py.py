# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:50:06 2019

@author: ychiu

# read from csv file and print it 

"""

import pandas as pd

file ="example.csv"
cars = pd.read_csv(file,index_col=0)

print(cars)

#print(cars[['Country','Cars_per_cap']])

# print out 2nd one
print(cars.iloc[1])

# print out for japan
print(cars.loc[['JAP']])


car = pd.read_csv(file)

print(car)

#print(cars[['Country','Cars_per_cap']])

# print out 2nd one
print(car.iloc[2])


