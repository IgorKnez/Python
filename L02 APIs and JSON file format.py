
# coding: utf-8

# In[1]:

# APIs and JSON (JavaScript Object Notation) file format

#Loading and exploring a JSON
import json

# Load JSON: json_data
with open("facebook.json") as json_file:
    json_data=json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k] )


# In[ ]:

# Exploring API data

# API requests

# Import requests package
import requests

# pull some data about movie social network from omdb
# Assign URL to variable: url
url='http://www.omdbapi.com/?t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)


# In[ ]:

# JSON- from the web to Python

# Import package
import requests
import json

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=social+network'

# Package the request, send the request and catch the response: r
r= requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data= r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k]


# In[ ]:

# Checking out the Wikipedia API

# Import package
import requests
import json

# Assign URL to variable: url
url='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data=r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

