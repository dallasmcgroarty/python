# built in function map
# accepts to arguments and a function and a iterable (list, tuple, set, dicts)
# runs the lambda for each iterable and returns a map objects containing everything

nums = [2,4,6,8,10]

doubles = map(lambda x: x * 2, nums)

print(list(doubles))

people = ['tom', 'bob', 'sally', 'tim']

# using lambda to map uppercased names to people list
peeps = map(lambda name: name[0].upper() + name[1:], people)

#convert map to list to read/use, most used method
print(list(peeps))

# problem: create a function that takes a list and decrements each element by 1
# and then returns the new list
def decrement_list(L):
    return list(map(lambda num: num-1, L))

print(decrement_list(nums))