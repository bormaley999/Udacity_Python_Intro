# Udacity Intro to Python
# Bonus Section 3  Generator Expressions

"""
You can actually create a generator in the same way you'd normally
write a list comprehension, except with parentheses instead of square brackets.
"""


sq_list = [x**2 for x in range(10)]  # this produces a list of squares
print(sq_list)

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
for s in sq_iterator:
    print(s)