
# coding: utf-8

# In[ ]:

# Importing SAS file with SAS7BDAT module

#import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas= file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()


# In[4]:

# Importing SAS file with Pandas

#import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_sas('sales.sas7bdat')

df_sas= pd.DataFrame(file)

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()


# In[8]:

# Importing Stata file with Pandas

# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df= pd.read_stata('Survey.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['hhsize2']])
plt.xlabel('House size')
plt.ylabel('count')
#plt.show()

