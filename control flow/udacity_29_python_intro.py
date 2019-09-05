# Udacity Intro to Python
# Section 29 Quiz: Unzip Tuples

"""Unzip the cast tuple into two names and heights tuples.
"""

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)

print(names)
print(heights)






