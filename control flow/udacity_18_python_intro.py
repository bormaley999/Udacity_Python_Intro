# Udacity Intro to Python
# Section 18 Practice: Iterating Through Dictionaries with For Loops

"""Iterating through keys"""

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)


"""Iterating through keys and values"""

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("\nIterating through keys and values:")
for key, value in cast.items()
    print("Actor: {}    Role: {}".format(key, value))



