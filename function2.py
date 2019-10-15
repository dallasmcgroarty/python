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