#Import the necessary libraries
import numpy as np
import pandas as pd

#Import the data set
baby_names = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv")

#drop the columns
baby_names.drop(['Unnamed: 0', 'Id'], axis = 1)

#male and female counts
counts_Gender=baby_names.Gender.value_counts()

#groub by names
Name=baby_names.groupby('Name').sum()

#Different
uq_Name=baby_names.groupby('Name').nunique()

#most name occurance
# Group by Name and sum the counts
name_counts = baby_names.groupby('Name')['Count'].sum()
print(name_counts)

# Find the least occurrence count
least_occurrence = name_counts.min()
print(least_occurrence)

# Count how many names have the least occurrence
num_least_common_names = (name_counts == least_occurrence).sum()

# What is the median name occurrence?
name_median =baby_names.groupby('Name')['Count'].sum().median()
print(name_median)

#What is the standard deviation of names
name_st_dev =baby_names.groupby('Name')['Count'].sum().std()
print(name_st_dev)


#Get a summary with the mean, min, max, std and quartiles
des=baby_names.describe()
print(des)

                               
                   
                    
                                   
