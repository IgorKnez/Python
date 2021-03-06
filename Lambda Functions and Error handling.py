
# coding: utf-8

# In[1]:

# first lambda function

# define lambda function add_bangs
add_bangs= (lambda a: a + '!!!')

# call lambda function add_bangs
add_bangs('hello')


# In[2]:

# lambda function with multiple variables

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)


# In[1]:

# lambda function and map()- applies lambda function on whole object

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list= list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)


# In[2]:

# lambda function and filter() for filtering elements from object

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 
              'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member)>6, fellowship)

# Convert result to a list: result_list
result_list= list(result)

# Convert result into a list and print it
print(result_list)


# In[3]:

# lambda function and reduce() - performs computations on objects and returns
# single value

# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use result() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1+item2, stark)

# Print the result
print(result)


# In[48]:

print('Types of Errors:')
print('\tValueError')
print('\tTypeError')
print('\tIndexError')
print('\tNameError')





# In[12]:

# Error handling with try-except

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''     

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")


# In[50]:

# Error handling by raising an error with raise ValueError()

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo<0:
        raise ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=-1)


# In[41]:

# Lambda functions exercise with tweeter data

# import pandas and tweets.csv
import pandas as pd
tweets_df= pd.read_csv('Tweets.csv')

# list of column names in tweets_df:
print(tweets_df.columns)

# select first 10 elements of text column: tweets
tweets= tweets_df.loc[:10,['text']]
print(tweets)

# Select retweets from the Twitter dataframe, 
# they have RT mark in text column: result
result = filter(lambda x: x[0:2]=='RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list=list(result)

# Print first 30 retweets in res_list
for tweet in res_list[0:30]:
    print(tweet)




# In[40]:

# Error handling with try-except with tweeter data

# import pandas and tweets.csv
import pandas as pd
tweets_df= pd.read_csv('Tweets.csv')


# Define count_entries()
def count_entries(df, col_name='candidate'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print(' The dataframe does not have a '+ col_name + ' coumn')
        
        
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'candidate')

print(result2)


# In[45]:

# Error handling by raising an error with raise ValueError() with tweeter data

# import pandas and tweets.csv
import pandas as pd
tweets_df= pd.read_csv('Tweets.csv')

# Define count_entries()
def count_entries(df, col_name='candidate'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The dataframe does not have a ' + col_name + ' column')

    # Initialize an empty dictionary: langs_count
    cols_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in dataframe
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
#result1 = count_entries(tweets_df, 'lang')

# Print result1
#print(result1)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'candidate')

print(result2)

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

