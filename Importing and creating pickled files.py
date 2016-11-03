
# coding: utf-8

# In[2]:

# Exploring working directory with library os

import os
wd= os.getcwd()
os.listdir(wd)


# In[1]:

# Creating pickled file

# Create dictionary
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

#import package
import pickle

# Save dictionary to pickle file
pickle.dump( europe, open( "europe.pkl", "wb" ) )


# In[3]:

# Loading a pickled file

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('europe.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

