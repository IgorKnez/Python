
# coding: utf-8

# In[1]:

# User-defined function without parameter

# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word='congratulations'+'!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()


# In[1]:

# Single parameter function

# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')


# In[2]:

# Functions that return single values

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word=word + '!!!'

    # Replace print with return
    return (shout_word)

# Pass 'congratulations' to shout: yell
yell= shout('congratulations')

# Print yell
print(yell)


# In[3]:

# Functions with multiple parameters

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1=word1+'!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+'!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout=shout1 +shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell=shout('congratulations','you')

# Print yell
print(yell)


# In[4]:

# Tuples

# create tuple nums
nums=(3,4,6)


# Unpack nums into num1, num2, and num3
num1,num2,num3=nums

# Construct even_nums tuple with elements from nums
even_nums=(2,num2,num3)

print(num1)
print(num2)
print(num3)
print(nums)
print(type(even_nums))


# In[5]:

# Function that return multiple values

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1= word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2= word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words=(shout1,shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2= shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)


# In[1]:

# Analyzing tweeter data

# Import pandas
import pandas as pd

# Import Twitter data as dataframe: df
df = pd.read_csv('Tweets.csv')

# Initialize an empty dictionary: candidate_count
candidate_count = {}

# Extract column from DataFrame: col
col = df['candidate']

# Iterate over lang column in df
for entry in col:

    # If the language is in langs_count, add 1
    if entry in candidate_count.keys():
        candidate_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        candidate_count[entry]=1

# Print the populated dictionary
print(candidate_count)


# In[2]:

# Analayzing how candidates are writen about on tweeter

#import pandas as pd
import pandas as pd
#Import tweets.csv: tweets_df
tweets_df= pd.read_csv('Tweets.csv')

# Define count_entries()
def count_entries(df,col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    cand_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in dataframe
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in cand_count.keys():
            cand_count[entry]+=1
        # Else add the language to langs_count, set the value to 1
        else:
            cand_count[entry]=1

    # Return the langs_count dictionary
    return cand_count

# Call count_entries(): result
result=count_entries(tweets_df,'candidate')

# Print the result
print(result)


# In[ ]:



