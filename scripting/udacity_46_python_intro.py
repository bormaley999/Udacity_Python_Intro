# Udacity Intro to Python
# Section 46  Quiz: Flying Circus Cast List

"""Write a function called create_cast_list that takes a filename as input and returns a list of actors' names.
"""


def create_cast_list(filename):
    cast_list = []

    with open("flying_circus_cast.txt") as f:     # use with to open the file filename
        for actor_name in f:     # use the for loop syntax to process each line
            cast_list.append(actor_name.split(",")[0])     # and add the actor name to cast_list
            # name = line.split(",")[0] -> another solution
            # cast_list.append(name) -> another solution



    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)




