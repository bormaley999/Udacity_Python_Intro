# Udacity Intro to Python
# Section 47  Quiz: Quiz: Practice Debugging

"""
"""

# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers
for i in range(10):

    try:
        userInput = int(input("Enter any 2-digit number: "))
        user_list.append(userInput)
        if userInput % 2 == 0:
            list_sum += userInput
    except ValueError as e:
        print("OLOLO! {}".format(e))

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))