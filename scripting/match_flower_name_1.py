# Udacity Intro to Python
# Section 50  Practice Question

"""
Question:
1. Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary.

2. The main (separate) function should take user input (user's first name and last name) and parse the user input
to identify the first letter of the first name.

3.It should then use it to print the flower name with the same first letter
(from dictionary created in the first function).
"""

flowers_file = "flower.txt"
flowers_list_dict = {}  # define type
first_letter = ''



with open(flowers_file) as fp:
   for cnt, line in enumerate(fp):
       key = line[0]
       value = line.split(": ")[1]
       flowers_list_dict[key] = value


def input_func():
    name = str(input("First Name: "))
    first_letter = name[0]
    dict_value = flowers_list_dict[first_letter]
    print(dict_value)


input_func()






