# Udacity Intro to Python
# Section 5
# Quiz: Dictionaries and Identity Operators
"""Define a Dictionary, population, that provides information
on the world's largest cities.
The key is the name of a city (a string), and the associated
value is its population in millions of people."""

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
from typing import Dict, Any

cities_population_dict = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5} # the dictionary list
cities_population_dict["Moscow"] = 22.2 # add Moscow variable to the dictionary

n = cities_population_dict.get("Shanghai") # get method from the dictionary

print(n is not None)
print(cities_population_dict["Shanghai"])
print(cities_population_dict)
