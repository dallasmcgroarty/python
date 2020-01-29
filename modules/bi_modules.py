# modules help keep python files smaller
# modules allow you to reuse code
# a module is just another Python file

import random
# random module gives access to functions that allow for random choice
print(random.choice(["apple","cherry","orange","pear"]))
print(random.randint(1,100))

# can also import like
import random as rand
print(rand.randint(1,100))

# from lets you import parts of a module
from random import choice, randint
print(randint(1,100))

# from {module} import * imports all functions

#problem 
# create a function that accepts any number of strings
# return true if any string is a keyword or false if none are keywords
# use built in module keyword
import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item) == True:
            return True
    return False

print(contains_keyword('def','hello','nope','chicken'))