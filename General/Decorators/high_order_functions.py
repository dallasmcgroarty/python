# function that accepts a function as an arg or returns a function
from random import choice
def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total
def square(x):
    return x*x

print(sum(3,square))

def greet(person):
    def get_mood():
        msg = choice(('hello there ', 'go away ', 'i love you '))
        return msg
    result = get_mood() + person
    return result

print(greet('toby'))

def make_laugh(person):
    def get_laugh():
        laugh = choice(('HAHAHA', 'LOL','tehehe'))
        return f"{laugh} {person}"
    return get_laugh

laugh = make_laugh("Linda")
print(laugh())