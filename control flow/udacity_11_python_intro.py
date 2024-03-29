# Udacity Intro to Python
# Section 11 Quiz: Tax Purchase

'''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
'''

state = str(input("Please, input the state: "))  #Either CA, MN, or NY
purchase_amount = 10 #amount of purchase

if state == "CA": #provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount * (1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN": #provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount * (1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY":  #provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount * (1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
else:
    print("Are you sure you need to take a taxi? :D")


print(result)



