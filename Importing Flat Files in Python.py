
# coding: utf-8

# In[2]:

# Exploring working directory

get_ipython().system('ls')


# In[3]:

# Importing entire text files

# Open a file: file
file = open('moby_dick.txt', 'r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)


# In[1]:

# Importing text files line by line

# Read & print the first 5 lines
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())


# In[1]:

# The Zen of Python

import this

