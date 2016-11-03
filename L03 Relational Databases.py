
# coding: utf-8

# The Chinook database contains information about a semi-fictional digital media store in which media data is real and customer, employee and sales data has been manually created.

# In[1]:

# Creating SQL a database engine

#Import the function create_engine from the module sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

#Create an engine to connect to the SQLite database 'Chinook.sqlite'  which is saved in local
# working directory and assign it to engine.
engine= create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Explore what tables are in this database

# Save the table names to a list: table_names
table_names= engine.table_names()

# Print the table names to the shell
print(table_names)


# Open engine connection: con
con= engine.connect()

# Perform query: rs
rs = con.execute('SELECT * FROM Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())


# In[2]:

# Querieng SQL database

# Creating SQL a database engine

#Import the function create_engine from the module sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

#Create an engine to connect to the SQLite database 'Chinook.sqlite'  which is saved in local
# working directory and assign it to engine.
engine= create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany())
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())


# In[3]:

# Filtering your database records using SQL's WHERE

# Create engine: engine
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId>=6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())


# In[4]:

# Ordering your SQL records with ORDER BY

#Import the function create_engine from the module sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns=rs.keys()


# Print head of DataFrame
print(df.head())


# In[8]:

# Pandas and The Hello World of SQL Queries!

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine= create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Execute query and store records in DataFrame: df
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager
# Perform query and save results to DataFrame: df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result: does df = df1 ?   
print(df.equals(df1))


# In[11]:

# Pandas for more complex querying

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine= create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Execute query and store records in DataFrame: df
df= pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId>=6 ORDER BY BirthDate',engine)

# Print head of DataFrame
print(df.head())


# In[16]:

# The power of SQL lies in relationships between tables: INNER JOIN

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine= create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs=con.execute('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID')
    df= pd.DataFrame(rs.fetchall())
    df.columns=rs.keys()

# Print head of DataFrame df
print(df.head())


# In[18]:

# Filtering your INNER JOIN

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine= create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Execute query and store records in DataFrame: df
df= pd.read_sql_query(
    'SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000',
    engine) 

# Print head of DataFrame
print(df.head())


# In[ ]:



