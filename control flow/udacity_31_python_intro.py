# Udacity Intro to Python
# Section 31 Quiz: Enumerate

"""Use enumerate to modify the cast list so that each element contains the name
followed by the character's corresponding height.
For example, the first element of cast should change
from "Barney Stinson" to "Barney Stinson 72".
"""

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]


# for cast in enumerate((cast), (heights[0])):
#     print(cast) >>> my initial solution

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)




