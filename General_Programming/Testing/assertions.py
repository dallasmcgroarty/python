# Assertions - can make simple assertion with assert keyword
# assert accepts an expression
# returns None if expression is truthy
# raises AssertionError if the expressionis falsy
# accepts an optional error message as a second argument

def add_pos_nums(x,y):
    assert x > 0 and y > 0, "Both numbers must be Positive!"
    return x + y

print(add_pos_nums(1,1))
#print(add_pos_nums(1,-1))

def eat_junk(food):
    assert food in [
        'pizza',
        'ice cream',
        'candy',
        'fried butter'
    ], 'Food must be a junk food!'
    return f"Nom nom nom i am eating {food}"

food = input('Enter a food please: ')
print(eat_junk(food))

# if python file run with -O flag, assertions will not be evaluated