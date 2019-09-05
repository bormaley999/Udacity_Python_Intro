# Udacity Intro to Python
# Section 17 Practice: Building Dictionaries


"""Method 1: Using a for loop to create a set of counters"""

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes',
               'the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for x in book_title:
    if x not in word_counter:
        word_counter[x] = 1
    else:
        word_counter[x] += 1

print(word_counter)

"""Method 2: Using a for loop to create a set of counters"""

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes',
               'the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)
