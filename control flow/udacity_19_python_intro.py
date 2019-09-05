# Udacity Intro to Python
# Section 19 Quiz: Fruit Basket

"""Task 1"""
"""You would like to count the number of fruits in your basket.
In order to do this, you have the following dictionary and list of fruits.
Use the dictionary and list to count the total number of fruits,
but you do not want to count the other items in your basket.
"""

# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# result = 0
#
# for object, value in basket_items.items(): #Iterate through the dictionary
#     if object in fruits: #if the key is in the list of fruits, add the value (number of fruits) to result
#         result += value
#
# print("There {} fruits in the basket".format(result))


"""Task 2"""
# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, value in basket_items.items():#Iterate through the dictionary
    if object in fruits:
        fruit_count += value
        #if the key is in the list of fruits, add to fruit_count.    else:
        object not in fruits
        not_fruit_count += value
        # if the key is not in the list, then add to the not_fruit_count
print("There {} fruits and {} not fruits are in the basket".format(fruit_count, not_fruit_count))



"""Solution from tutor"""
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))


