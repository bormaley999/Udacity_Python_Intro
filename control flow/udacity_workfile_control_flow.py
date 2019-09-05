# Udacity Intro to Python | Section 4
"""Code Playground File for Control Flow Section of the course"""

"""Conditional Statements"""
#First Example - try changing the value of phone_balance


#Second Example - try changing the value of number

# number = 145
# if number % 2 == 0:
#     print("Number " + str(number) + " is even.")
# else:
#     print("Number " + str(number) + " is odd.")
#
#
# Third Example - try to change the value of age
# age = 10
#
# # Here are the age limits for bus fares
# free_up_to_age = 4
# child_up_to_age = 18
# senior_from_age = 65
#
# # These lines determine the bus fare prices
# concession_ticket = 1.25
# adult_ticket = 2.50
#
# # Here is the logic for bus fare prices
# if age <= free_up_to_age:
#     ticket_price = 0
# elif age <= child_up_to_age:
#     ticket_price = concession_ticket
# elif age >= senior_from_age:
#     ticket_price = concession_ticket
# else:
#     ticket_price = adult_ticket
#
# message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
# print(message)
#




# points = 174  # use this input when submitting your answer
#
# # set prize to default value of None
# prize = None
#
# # use the value of points to assign prize to the correct prize name
# if points <= 50:
#     prize = "wooden rabbit"
# elif 151 <= points <= 180:
#     prize = "wafer-thin mint"
# elif points >= 181:
#     prize = "penguin"
#
# # use the truth value of prize to assign result to the correct message
# if prize:
#     result = "Congratulations! You won a {}!".format(prize)
# else:
#     result = "Oh dear, no prize this time."
#
# print(result)


# points = 174
# if points <= 50:
#     result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#     result = "Oh dear, no prize this time."
# elif points <= 180:
#     result = "Congratulations! You won a wafer-thin mint!"
# else:
#     result = "Congratulations! You won a penguin!"
#
# print(result)


"""For loops"""

# i = int(input("How much money do you have?: "))
#
# while i >= 1:
#     print("You are rich")
#     i -= 1
#     print("Now you have")
#     print(i)
# else:
#     print("Now you are poor")
#
# print("Ha-ha")

# errors = 5
# if errors:
#     print("You have {} errors to fix!".format(errors))
# else:
#     print("No errors to fix!")


# text_list = ["One", "Two", "Three", "Four"]
#
# for text_letters in text_list:
#     print(text_letters.title())
#

# text_list = ["one", "two", "three", "four"]
# capitalized_words = ["fifth", "six"]
#
# for text_letters in text_list:
#     capitalized_words.append(text_letters.title())

# print(list(range(1, 10, 2)))
# print(list(range(4)))

# print(range(4))

# for number in range(4):
#     print(number)

# text_list = ["one", "two", "three", "four"]
#
# for index in range(len(text_list)):
#     text_list[index] = text_list[index].title()
#     print(text_list)
#
# for x in range(3):
#     print("Hi")

# cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
# for city in cities:
#     print(city)
# print("Done!")

# sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# for new_line in sentence:
#     print(new_line)
#
#
# for number in range(5, 35, 5):
#     print(number)
#
# print(list(range(5, 35, 5)))
#
# for number in range(4):
#     print(number)


# # print(list(range(5)))
#
# persons = ["Jim", "John", "Adam", "Peter"]
#
# search_person = "Jim"
#
# if search_person in persons:
#     print(f"{search_person} was found in person list")
# else:
#     print("No results")


""" While loops"""

# card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
# hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
# while sum(hand) < 25:
#     hand.append(card_deck.pop())
#
# print(sum(hand))

# step = 0
# max_steps = 5
#
# while step < max_steps:
#     step += 1
#     #print("I\'m working on ... {} remaining".format(max_steps - step)) >> another way of writing this code
#     print(f"I'm working on ... {max_steps - step} remaining")

# print the factorial of number
    # print(product)

# card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
# hand = []
#
# # adds the last element of the card_deck list to the hand list
# # until the values in hand add up to 17 or more
# while sum(hand)  < 17:
#     hand.append(card_deck.pop())
#
# print(hand)


# """Practice: Factorials with While Loops
# """
#
# # number to find the factorial of
# number = 6
# # start with our product equal to one
# product = 1
# # track the current number being multiplied
# current = 1
#
# while  current <= number:
#     # multiply the product so far by the current number
#     product *= current
#     # increment current with each iteration until it reaches number
#     current += 1
#
#
# """Practice: Factorials with For Loops
# """
# # number we'll find the factorial of
# number = 6
# # start with our product equal to one
# product = 1
#
# # calculate factorial of number with a for loop
# for num in range(2, number + 1):
#     product *= num
#
# # print the factorial of number
# print(product)


"""Break, Continue"""

# manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
#
# # the code breaks the loop when weight exceeds or reaches the limit
# print("METHOD 1")
# weight = 0
# items = []
# for cargo_name, cargo_weight in manifest:
#     print("current weight: {}".format(weight))
#     if weight >= 100:
#         print("  breaking loop now!")
#         break
#     else:
#         print("  adding {} ({})".format(cargo_name, cargo_weight))
#         items.append(cargo_name)
#         weight += cargo_weight
#
# print("\nFinal Weight: {}".format(weight))
# print("Final Items: {}".format(items))
#
# # skips an iteration when adding an item would exceed the limit
# # breaks the loop if weight is exactly the value of the limit
#
# print("\nMETHOD 2")
# weight = 0
# items = []
# for cargo_name, cargo_weight in manifest:
#     print("current weight: {}".format(weight))
#     if weight >= 100:
#         print("  breaking from the loop now!")
#         break
#     elif weight + cargo_weight > 100:
#         print("  skipping {} ({})".format(cargo_name, cargo_weight))
#         continue
#     else:
#         print("  adding {} ({})".format(cargo_name, cargo_weight))
#         items.append(cargo_name)
#         weight += cargo_weight
#
# print("\nFinal Weight: {}".format(weight))
# print("Final Items: {}".format(items))


"""zip and enumerate"""

# manifest = [  # >>> this is a list with a tuple of size 2
#     ("bananas", 15),
#     ("mattresses", 34),
#     ("dog kennels", 42),
#     ("machine", 120),
#     ("cheeses", 5)
# ]
# print("\n", "Method 1")
# print(manifest)
#
# items = ["bananas", "mattresses", "dog kennels", "machine", "cheeses"]
# weights = [15, 34, 42, 120, 5]
#
# print("\n", "Method 2")
# print(list(zip(items, weights)))
#
#
# items = ["bananas", "mattresses", "dog kennels", "machine", "cheeses"]
# weights = [15, 34, 42, 120, 5]
#
# print("\n", "Method 3")
#
# for cargo in zip(items, weights):
#     print(cargo[0], cargo[1])
#     print(type(cargo))
#
#
# manifest = [
#     ("bananas", 15),
#     ("mattresses", 34),
#     ("dog kennels", 42),
#     ("machine", 120),
#     ("cheeses", 5)
# ]
# items, weights = zip(*manifest)
#
# print("\n", "Unzipping method")
# print(items)
# print(weights)
#
#
# items = ["bananas", "mattresses", "dog kennels", "machine", "cheeses"]
# print("\n", "Preparing for enumerate function")
# for i, item in zip(range(len(items)), items):
#     print(i, items)


# items = ["bananas", "mattresses", "dog kennels", "machine", "cheeses"]
# print("\n", "Enumerate function in progress")
# for i, item in enumerate(items):
#     print(i, item)

# some_list = [('a', 1), ('b', 2), ('c', 3)] # >>> the example of zip
# letters, nums = zip(*some_list)
# print(type(some_list))

# letters = ['a', 'b', 'c', 'd', 'e'] # >>> the example of enumerate
# for i, letter in enumerate(letters):
#     print(i, letter)


"""List Comprehensions
"""
# cities = ["new york city", "mountain view", "chicago", "los angeles"]
# capitalized_cities = []
# for city in cities:
#     capitalized_cities.append(city.title())
# print("Example WITHOUT using a List Comprehension")
# print(capitalized_cities)
#
# cities = ["new york city", "mountain view", "chicago", "los angeles"]
# capitalized_cities = [city.title() for city in cities]
# print("\n", "Example WITH a List Comprehension")
# print(capitalized_cities)
#
# squares = []
#
# for x in range(9):
#     squares.append(x**2)
# print("\n", "Second Example WITHOUT a List Comprehension")
# print(squares)
#
# squares = [x**2 for x in range(9)]
# print("\n", "Second Example WITH a List Comprehension")
# print(squares)
#
# squares = [x**2 for x in range(9) if x % 2 == 0]
# print("\n", "Third Example WITH a List Comprehension")
# print(squares)
#
#
# squares = [x**2 if x % 2 == 0 else x + 3
# for x in range(9)]
# print("\n", "Fourth Example WITH a List Comprehension")
# print(squares)
#
# D = {'a': 97, 'c': 0 , 'b':0,'e': 94, 'r': 97 , 'g':0}
# # sum(value == 0 for value in D.values())
#
# print(list(D.values()).count(0))


"""Functions"""

# def print_greeting():
#     print("\n","Function WITHOUT arguments")
#     print("Hello World")
# print(print_greeting())
#
# def cylinder_volume(height, radius):
#     pi = 3.14159
#     volume = height * pi * radius ** 2
#     return volume
#
# print("\n","Function WITH arguments")
# print(cylinder_volume(50, 45))
#
# # this prints something, but does not return anything
# def show_plus_ten(num):
#     print(num + 10)
#
# # this returns something
# def add_ten(num):
#     return(num + 10)
#
# print("\n")
# print('Calling show_plus_ten...')
# return_value_1 = show_plus_ten(5)
# print('Done calling')
# print('This function returned: {}'.format(return_value_1))
#
# print('\nCalling add_ten...')
# return_value_2 = add_ten(5)
# print('Done calling')
# print('This function returned: {}'.format(return_value_2))
#
# # Простая функция
# print("\n")
# def simple_action():
#     print('I am a simple function! Nothing interesting yet...')
#
# simple_action()  # вызывает выполнение функции
#
#
# def cylinder_volume(height, radius=5): # here we assign arguments to a function
#     pi = 3.14159
#     return height * pi * radius ** 2
# print("Default arguments function")
# print(cylinder_volume(10, 7))
# # here we have changed the argument of radius (2nd position). It's 7 instead 5 now.
#
# cylinder_volume(10) # this will mean that the system will take the default arg of radius which is 5.
# cylinder_volume(10, 7)  # pass in arguments by position
# cylinder_volume(height=10, radius=7)  # pass in arguments by name
#
# # This will result in an error
# def some_function():
#     word = "hello"
# print("Variable Scope with an error")
# print(word)
#
# # Assigning one variable (word) to a different functions
# def some_function():
#     word = "hello"
#
# def another_function():
#     word = "goodbye"
#
# # Here, word is said to have a global scope.
# word = "hello"
#
# def some_function():
#     print(word)
#
# some_function()
#
#
# egg_count = 0
#
# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs
#
# buy_eggs()
#
# # This causes an UnboundLocalError, since Python doesn't allow functions to modify variables
# # that are outside the function's scope. A better way would be to pass the variable as an argument
# # and reassign it outside the function.
#
# egg_count = 0
#
# def buy_eggs(count):
#     return count + 12  # purchase a dozen eggs
#
# egg_count = buy_eggs(egg_count)
# print(egg_count)

"""Lambda Expressions"""

# def multiply(x, y):
#     return x * y
#
# multiply = lambda x, y: x * y
#
# print(multiply(5, 10))


"""Scripting"""
#
# name = input("Enter your name: ")
# print("Hello there, {}!".format(name.title()))
#

# num = int(input("Enter an integer: "))
# print("hello" * num)


# result = eval(input("Enter an expression: "))
# print(result)


# x = int(input("Enter a number: "))
# x += 20
# print(x)


# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except:
#         print("That\'s not a valid number!")
#     # finally:
    #     print("\nAttempted Input\n")

# try:
#     # some code
# except ValueError:
#     # some code
#
# try:
#     # some code
#     except (ValueError, KeyboardInterrupt):
# # some code
#
# try:
#     # some code
# except ValueError:
#     # some code
# except KeyboardInterrupt:
#     # some code
# try:
#     x = int(input("Please, give a number: "))
# except ValueError as e:
#    # some code
#    print("ZeroDivisionError occurred: {}".format(e))
#
# try:
#     x = int(input("Please, give a number: "))
# except Exception as e:
#    # some code
#    print("Exception occurred: {}".format(e))

# truth = "beauty"
# index = 0
# letters = []
# while index < len(truth):
#     letters.append(truth[index])
#     index += 2
#
# letters = '-'.join(letters)
# print(letters)

# print("the dry like"[4:6])

import random
colors = ["red", "blue", "green", "white", "d", "n"]
for x in colors:
    if len(colors[1]) >= 4:
     print(random.choice(colors))
else:
    print("Why?")
print(len(colors))