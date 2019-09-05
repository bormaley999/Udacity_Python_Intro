# Udacity Intro to Python
# Section 15 Practice: For Loops | Quiz Tag Counter

"""
Write a for loop that iterates over a list of strings, tokens,
and counts how many of them are XML tags. XML is a data language similar to HTML.
You can tell if a string is an XML tag if it begins with a left angle bracket "<"
and ends with a right angle bracket ">".
Keep track of the number of tags using the variable count.
"""


tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)
