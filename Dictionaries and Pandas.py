
# coding: utf-8

# In[1]:

# Creating and Accessing dictionary

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
indger=countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[indger])

# From string in countries and capitals, create dictionary europe
europe = {
    'spain':'madrid',
    'france':'paris',
    'germany':'berlin',
    'norway':'oslo'
    }

# Print europe
print(europe)

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])


# In[2]:

# Dictionary Manipulation

# Add italy to europe
europe['italy']='rome'

# Print out italy in europe
print(europe['italy'])

# Add poland to europe
europe['poland']='warsaw'

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 
          'australia':'vienna' }

# Update capital of germany
europe['germany']='berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)


# In[3]:

# Dictionary of dictionaries

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
           
           
# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data={'capital':'rome',
      'population':'59.83'
      }

# Add data to europe under key 'italy'
europe['italy']=data

# Print europe
print(europe)


# In[1]:

# From Dictionary to DataFrame

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 
         'Egypt']
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

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index=row_labels

# Print cars again
print(cars)

#export DF cars to cars.csv file:
cars.to_csv('cars.csv')


# In[2]:

#CSV to DataFrame


# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars=pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)


# In[3]:

#Selecting data from Pandas DataFrame


# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])


# In[4]:

#slicing dataframes to get rows

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])


# In[5]:

#Selecting data using loc (lobel-based) and iloc(integer index based) commands


# Print out observation for Japan
print(cars.loc['JAP'])
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])
print(cars.iloc[[1,6]])

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])


# In[6]:

#Selecting data using loc (lobel-based) and iloc(integer index based) commands 2

# Print sub-DataFrame containing the observations for Russia  
# and Morocco and the columns country and drives_right
print(cars.loc[['RU','MOR'],['country','drives_right']])


# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,'drives_right'])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])


# In[ ]:



