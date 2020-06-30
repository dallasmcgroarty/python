# * parameter excepts any number of arguments
# * args is a tuple
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(1,2,3,4,5))

# **kwargs special operator to pass to functions
# gathers remaining keyword arguments as a dictionary
# instead of a tuple like *args
def fave_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
fave_colors(colt='purple', ruby='red', dan='blue')
fave_colors(colt="royal deep amazinly purple purple")

# exercise: combine prefix and word or word and suffic
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

# parameter ordering
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

# argument unpacking
# * before argument says take the list/tuple and pass each 
# item as a seperate argument
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

nums = (1,2,3,4,5,6)
sum_all_values(*nums)

# dictionary unpacking
# ** before argument
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {'first':'Colt', 'second':'Rusty'}
display_names(**names)

def add_multiply_numbers(a,b,c, **kwargs):
    print(a + b * c)
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55, name='tony')
add_multiply_numbers(**data)

def some(**kwargs):
    return kwargs['t'] +  str(float(kwargs['p']))
print(some(t='yo bitch', p=2))

'''
unpack dict args and evaluate some expressions based on what the values are
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(**kwargs):
    result = ''
    if('make_float' in kwargs and kwargs['make_float'] == True):
        if(kwargs['operation'] == 'add'):
            result = kwargs['first'] + kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(float(result))
            else:
                return 'The result is ' + str(float(result))
        elif(kwargs['operation'] == 'subtract'):
            result = kwargs['first'] - kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(float(result))
            else:
                return 'The result is ' + str(float(result))
        elif(kwargs['operation'] == 'divide'):
            result = kwargs['first'] / kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(float(result))
            else:
                return 'The result is ' + str(float(result))
        elif(kwargs['operation'] == 'multiply'):
            result = kwargs['first'] * kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(float(result))
            else:
                return 'The result is ' + str(float(result))
    else:
        if(kwargs['operation'] == 'add'):
            result = kwargs['first'] + kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(result)
            else:
                return 'The result is ' + str(result)
        elif(kwargs['operation'] == 'subtract'):
            result = kwargs['first'] - kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(result)
            else:
                return 'The result is ' + str(result)
        elif(kwargs['operation'] == 'divide'):
            result = kwargs['first'] / kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(result)
            else:
                return 'The result is ' + str(result)
        elif(kwargs['operation'] == 'multiply'):
            result = kwargs['first'] * kwargs['second']
            if('message' in kwargs):
                return kwargs['message'] + ' ' + str(result)
            else:
                return 'The result is ' + str(result)
