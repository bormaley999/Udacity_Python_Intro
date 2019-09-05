# Udacity Intro to Python
# Section 9 Practice: Conditional Statements

"""Write an if statement that lets a competitor know which of these prizes they won
based on the number of points they scored, which is stored in the integer variable points.
"""

# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin

# points = 174  # use this input to make your submission

#TODO's:
# 1. Points variable can only take on positive integer values up to 200
# 2. In your if statement, assign the result variable to a string holding the
# 2.1 appropriate msg based on the value of points.
# 3. If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name.
# 3.1 If there's no prize, the message should state "Oh dear, no prize this time."



points = 181

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)