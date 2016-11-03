
# coding: utf-8

# In[11]:

#Logic, Control Flow and Filtering

#Comparision Operators (equal and not equal)

# Comparison of booleans
print(True==False)

# Comparison of integers
print(-5*15!=75)

# Comparison of strings
print('pyscript'=='PyScript')

# Compare a boolean with an integer
print(True==1)


# In[5]:

# Comparision Operators (less and greater)

# Comparison of integers
x = -3 * 6
print(x>=-10)

# Comparison of strings
y = "test"
print('test'<=y)

# Comparison of booleans
print(True>False)


# In[7]:

import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
#it compares every element of array with 18
print(my_house>=18)

# my_house less than your_house
# first element compares with first element of second array and so one
print(my_house<your_house)


# In[8]:

# Boolean Operators (and, or, not)

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen>10 and my_kitchen<18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen<14 or my_kitchen>17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2 <my_kitchen*3)


# In[10]:

# Boolean Operators (and, or, not)

# not has a higher priority than and and or, it is executed first.
x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10))


# In[12]:

# Boolean operators with Numpy
# np.logical_and(), np.logical_or() and np.logical_not()

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house>18.5, my_house<10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11, your_house<11))


# In[13]:

# Conditional statments (if, elif, else)

area = 10.0

if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")


# In[16]:

# Conditional statments (if, elif, else)

# Define variables
room = "kit"
area = 14.0

# if-else statement for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else statement for area
if area>15:
    print('big place!')
else:
    print('pretty small.')


# In[17]:

# Conditional statments (if, elif, else)

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area>10:
    print('medium size, nice!')
else :
    print("pretty small.")


# In[40]:

# Creating DataFrame cars from dictionary and saving it to .csv

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names,
         'drives_right':dr,
         'cars_per_cap':cpc
         }


# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

# Add row labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
cars.index=row_labels

#save Cars DataFrame to csv
cars.to_csv('Auti.csv')


# In[42]:

# Filtering pandas using boolean conditional statments

# Import pandas
# Import Auti data
import pandas as pd

#this we use if we import file from CWD
auti = pd.read_csv('Auti.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr=auti['drives_right']
print(type(dr))

# Use dr to subset auti: sel
# It will select only those that are true
sel= auti[dr]

# Print sel
print(sel)


# In[44]:

# Filtering pandas using boolean conditional statments

#Import pandas
#Import auti data

import pandas as pd
auti = pd.read_csv('Auti.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc=auti['cars_per_cap']
many_cars=cpc>500
car_maniac=auti[many_cars]

# Print car_maniac
print(car_maniac)


# In[47]:

#Filtering pandas using numpy boolean operators

# Import auti data and pandas
import pandas as pd
auti = pd.read_csv('Auti.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc=auti['cars_per_cap']
between= np.logical_and(cpc>100, cpc<500)
medium= auti[between]

# Print medium
print(medium)

