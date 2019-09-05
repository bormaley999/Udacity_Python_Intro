# Udacity Intro to Python
# Section 13 Practice: For Loops | Quiz: Modify Usernames with Range

"""
Write a for loop that iterates over the names list to create a usernames list.
To create a username for each name, make everything lowercase and replace spaces with underscores.
Running your for loop over the list:
"""
#existing list
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)):
    usernames[index] = usernames[index].replace(" ", "_")
    usernames[index] = usernames[index].lower()
    print(usernames)

#alternative solution >>>
# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# for i in range(len(usernames)):
#     usernames[i] = usernames[i].lower().replace(" ", "_")
#
# print(usernames)
#alternative solution <<<

