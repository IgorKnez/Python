
# coding: utf-8

# In[ ]:

# Listing sheets of Excel spreadsheets with pandas

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'd.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)


# In[ ]:

# Importing sheets of Excel spreadsheets with pandas

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'd.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2.Q 2015')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())


# In[ ]:

# Customizing your Excel spreadsheet import with pandas

# Import pandas
import pandas as pd
pd.set_option("display.max_rows",999)

# Assign spreadsheet filename: file
file = 'd.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Quarterly', 'Anual'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the first sheet and rename the column: df2
df2 = xl.parse(0, parse_cols=[0], skiprows=[0], names=['Kvartal'])

# Print the head of the DataFrame df2
print(df2.head())

