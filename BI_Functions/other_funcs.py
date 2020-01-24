# sorted function
# sorts an iterable but returns a copy and doesnt change the original iterable
print("use sort functions---")
nums = [2,6,31,4,7,25,3,1]
nums.sort()
print(nums)

nums = [2,6,31,4,7,25,3,1]
print(sorted(nums))
print(nums)

# reverse sort
print(sorted(nums, reverse=True))

# users example, sorting a dict
# good to use when sorting objects and we want to sort off certain properties
users = [
    {"username": "Samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "Katie","tweets": ["I love my cat"]},
    {"username": "Jeff", "tweets": []},
    {"username": "Bob123", "tweets": []},
    {"username": "Dan45", "tweets": ["dogs rule!"]}
]

print(sorted(users, key=lambda user: user['username']))

print(sorted(users, key=lambda user: len(user['tweets'])))

##*************
# min and max - returns min of an iterable or max of an iterable
print("using min and max---")

names = ['arya','samson','dora','tim','bartholomew']

print(min(names))
print(max(names))

# using lambda to find longest name and not highest first char value
longest_name = max(names, key=lambda n: len(n))
print(longest_name)

# get the name of the user who tweeted the most
most_tweets = max(users, key=lambda u: len(u['tweets']))['username']
print(most_tweets)

# create a function that accepts an iterable and returns a tuple of the min and max
def min_max(I):
    return min(I),max(I)

#*************
# reversed(I) - returnes the reverse of the iterable, and creates a copy
# .reverse() - reverses the iterable in place
print("using reverse and reversed---")

nums1 = [1,2,3,4]
nums1.reverse()
print(nums1)

nums1.reverse()

print(list(reversed(nums1)))

# reverse word with slicing
word = 'hello'
print(word[::-1])

# reverse iterate through a for loop
for x in reversed(range(0,10)):
    print(x, end=" ")
print()

#**************
# len() returns length of an object/iterable
#
print("using len---")
print(len('hello'))

#***********
# abs(), sum(), and round()
# abs() returns absolute value of number
# sum() returns sum of number
# round() returns number rounded to nearest digit
print("using abs, sum and round---")

print(abs(-23))

print(sum([1,2,3,4]))
print(sum((1.5,2,2.7)))

# can specify precision to round to
print(round(10.2))
print(round(1.2123, 2))

# problem
#create a function that accepts a list of numbers and returns the number
# with the maximum magnitude(i.e. the number furthest from 0)
def max_magnitude(nums):
    return max(abs(num) for num in nums)

#problem 2
# create a function that accepts a variable number of arguments and returns
# the sum of all the even numbers
# define sum_even_values
# use *args to accept a variable number or arguments
def sum_even_values(*args):
    return sum(arg for arg in args if arg%2 ==0)

#problem 3
# create a function that accepts a variable number or arguments and returns
# the sum of all the floats
def sum_floats(*args):
    return sum(arg for arg in args if isinstance(arg,float))