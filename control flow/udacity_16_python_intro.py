# Udacity Intro to Python
# Section 15 Practice: For Loops | Quiz: Create an HTML List

""" Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str,
which is an HTML list.
For example, if the list is items = ['first string', 'second string'], printing html_str should output:
"""


items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)