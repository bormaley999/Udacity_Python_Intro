# Udacity Intro to Python | Section 3
# Code Playground File for Data Structures Section of the course

"""Tuples Example"""

# Moscow = (55.7558, 37.6173)
#
# print(type(Moscow))
#
# print("Moscow is at latitude: {}".format(Moscow[0]))
# print("Moscow is at longitude: {}".format(Moscow[1]))


# length, width, height = 52, 40, 100
# print("The dimensions are {} x {} x {}".format(length, width, height))

"""What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)
"""
# tuple_a = 1, 2
# tuple_b = (1, 2)
#
# print(tuple_a == tuple_b)
# print(tuple_a[1])

# fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
#
# print("watermelon" in fruit)  # check for element
#
# fruit.add("watermelon")  # add an element
# print(fruit)
#
# print(fruit.pop())  # remove a random element
# print(fruit)

"""Dictionaries and Identity Operators"""
# elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
# print(elements["carbon"])
#
# print(elements["helium"])  # print the value mapped to "helium"
# elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
# print(elements)
#
# print("carbon" in elements)
# print(elements.get("dilithium"))
#
# n = elements.get("dilithium")
# print(n is None)
# print(n is not None)


# elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
# elements.get('kryptonite', 'There\'s no such element!')
# print(elements.get("kryptonite", 'There\'s no such element!'))

# animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
# print(animals['dogs'][3])

# VINIX = {'C': 0.74, 'MA': 0.78, 'BA': 0.79, 'PG': 0.85, 'CSCO': 0.88, 'VZ': 0.9, 'PFE': 0.92, 'HD': 0.97, 'INTC': 1.0,
#          'T': 1.01, 'V': 1.02, 'UNH': 1.02, 'WFC': 1.05, 'CVX': 1.05, 'BAC': 1.15, 'JNJ': 1.41, 'GOOGL': 1.46,
#          'GOOG': 1.47, 'BRK.B': 1.5, 'XOM': 1.52, 'JPM': 1.53, 'FB': 2.02, 'AMZN': 2.96, 'MSFT': 3.28, 'AAPL': 3.94}

# VINIX = {'C': [0.74, -6.51], 'MA': [0.78, 34.77], 'BA': [0.79, 17.01], 'PG': [0.85, -8.81], 'CSCO': [0.88, 18.56],
#          'VZ': [0.9, 2.16], 'PFE': [0.92, 13.96], 'HD': [0.97, 3.2], 'INTC': [1.0, 2.61], 'T': [1.01, -15.19],
#          'V': [1.02, 24.0], 'UNH': [1.02, 19.32],'WFC': [1.05, -3.59], 'CVX': [1.05, -5.77], 'BAC': [1.15, 4.27],
#          'JNJ': [1.41, -5.58], 'GOOGL': [1.46, 17.84], 'GOOG': [1.47, 17.03], 'BRK.B': [1.5, 4.54],
#          'XOM': [1.52, -6.87], 'JPM': [1.53, 7.66], 'FB': [2.02, 0.91], 'AMZN': [2.96, 62.75], 'MSFT': [3.28, 26.61],
#          'AAPL': [3.94, 26.01]}
#
# print(VINIX["GOOG"])

# room_numbers = {
#     ('Freddie', 'Jen'): 403,
#     ('Ned', 'Keith'): 391,
#     ('Kristin', 'Jazzmyne'): 411,
#     ('Eugene', 'Zach'): 395}
#
# print(room_numbers)

"""Compound Data Structures"""

# elements = {"hydrogen": {"number": 1,
#                          "weight": 1.00794,
#                          "symbol": "H"},
#                "helium": {"number": 2,
#                          "weight": 4.002602,
#                          "symbol": "He"}}
# helium = elements["helium"]  # get the helium dictionary
# hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
# print(elements["helium"]["weight"])
#
# oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
# elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
# print('elements = ', elements)

"""# Quiz: Verse Dictionary
"""

# verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
# print(len(verse_dict))
#
# # find number of unique keys in the dictionary
# num_keys = 51
# print(num_keys)
#
# # find whether 'breathe' is a key in the dictionary
# contains_breathe = verse_dict.get("breathe") # another solution >>> contains_breathe = "breathe" in verse_dict <<<
# print(contains_breathe)
#
# # create and sort a list of the dictionary's keys
# sorted_keys = sorted(verse_dict) # another solution >>> sorted_keys = sorted(verse_dict.keys()) <<<
# print(sorted_keys)
#
# # get the first element in the sorted list of keys
# print(sorted_keys[0])
#
#
# # find the element with the highest value in the list of keys
# print(max(sorted_keys)) # another solution >>> print(sorted_keys[-1]) <<<



