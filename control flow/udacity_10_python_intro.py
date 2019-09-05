# Udacity Intro to Python
# Section 10 Quiz: Guess My Number


"""You decide you want to play a game where you are hiding
a number from someone.  Store this number in a variable
called 'answer'.  Another user provides a number called
'guess'.  By comparing guess to answer, you inform the user
if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
"""

answer = 5 # provide answer
guess = int(input("Please, guess a number: ")) # provide guess

if guess < 5: #provide conditional
    # another solution >>>  if guess < answer: <<<
    result = "Oops!  Your guess was too low."
elif guess > 5: #provide conditional
    # another solution >>>  if guess > answer: <<<
    result = "Oops!  Your guess was too high."
elif guess == 5:
    # another solution >>>  if guess == answer: <<<
    result = "Nice!  Your guess matched the answer!"

print(result)