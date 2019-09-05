# Udacity Intro to Python
# Section 14 Practice: For Loops | Quiz Solution: Create Usernames

"""
Write a for loop that iterates over the names list to create a usernames list.
To create a username for each name, make everything lowercase and replace spaces with underscores.
Running your for loop over the list:
"""
#existing list
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

