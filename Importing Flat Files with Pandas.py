
# coding: utf-8

# In[1]:

# Using pandas to import flat files as DataFrames

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())


# In[3]:

# Using pandas to import flat files as DataFrames and building NumPy arrays

#import packages
import pandas as pd
import numpy as np

# Assign the filename: file
file = 'digits.txt'

# Read the first 5 rows of the file into a DataFrame: data
data= pd.read_table(file, nrows=5,header=None)

# Build a numpy array from the DataFrame: data_array
data_array=data.values

# Print the datatype of data_array to the shell
print(type(data_array))

# print first 5 columns
print(data.head)


# In[2]:

# Customizing your pandas import

# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic.csv'

# Import file: data
data = pd.read_csv(file, sep=',', comment='#', na_values=['Nothing','NA','NaN'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()


# In[ ]:



