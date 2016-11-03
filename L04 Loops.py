
# coding: utf-8

# In[1]:

# While Loops

# as long as the condition is True, code is executed
x = 1
while x < 4 :
    print(x)
    x = x + 1


# In[2]:

# While Loops

# Initialize offset
offset=8

# reverted pendelum - while offset is not 0, code will run until becomes 0
# Code the while loop
while offset!=0:
    print('correcting..')
    offset=offset-1
    print(offset)


# In[3]:

# While loops with conditionals

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0:
        offset=offset-1
    else:
        offset=offset+1
    print(offset)


# In[4]:

# For loops

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for item in areas:
    print(item)


# In[8]:

# For loops using enumerate
# enumerate returns indices and value at that index

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate()
for index, a in enumerate(areas) :
    print('room '+str(index+1)+': '+ str(a))


# In[9]:

# Loop over list of lists

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch

for x in house:
    print('the '+x[0]+' is '+str(x[1])+ ' sqm')


# In[1]:

#Loop over dictionary

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 
          'australia':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print('the capital of '+key+' is '+value)


# In[2]:

#Loop over Numpy array

# Import numpy as np
import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D Numpy array from baseball: np_baseball
np_baseball=np.array(baseball)
np_weight=np_baseball[:,1]
np_height=np_baseball[:,0]
print(np_height)

# For loop over np_height
for x in np.nditer(np_height):
    print(str(x)+' centimeters')

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)


# In[3]:

# Loop over DataFrame

# Import cars data
import pandas as pd
cars = pd.read_csv('Auti.csv', index_col = 0)

# Iterate over rows of cars
for label, row in cars.iterrows():
    print(label)
    print(row)


# In[4]:

# Loop over DataFrame (2)

# Import cars data
import pandas as pd
cars = pd.read_csv('Auti.csv', index_col = 0)

# Iterate over rows of cars
for label, row in cars.iterrows():
    print(label+' : '+str(row['cars_per_cap']))


# In[5]:

# Adding columns in Data Frame using For loop 

# Import cars data
import pandas as pd
cars = pd.read_csv('Auti.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for label, row in cars.iterrows():
    cars.loc[label, 'COUNTRY'] = row['country'].upper()


# Print cars
print(cars)


# In[6]:

# apply method for DataFrames

# Import cars data
import pandas as pd
cars = pd.read_csv('Auti.csv', index_col = 0)

# Use .apply(str.upper)
cars['COUNTRY']= cars['country'].apply(str.upper)

print(cars)


# In[ ]:



