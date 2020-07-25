# filter function in python
# takes a lambda or function(true or false output) and an iterable object
# filters the the object based on the lambda and returns that value if true

names = ['austin','penny','tom','anthony','billy']

a_names = filter(lambda n: n[0] == 'a', names)

# convert filter object to a list and print
print(list(a_names))

users = [
    {"username": "Samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "Katie","tweets": ["I love my cat"]},
    {"username": "Jeff", "tweets": []},
    {"username": "Bob123", "tweets": []},
    {"username": "Dan45", "tweets": ["dogs rule!"]}
]

#using list comp
inactive_users2 = [user for user in users if not user['tweets']]
print(inactive_users2)
# can use len(u["tweets"]) == 0 or just use not u['tweets']
inactive_users = list(filter(lambda u: not u['tweets'], users))

print(inactive_users)

#********
# combine map and filter
#********

# use map to look at only usernames in users and then filter to 
# get all users that are inactive

inactive = list(map(lambda user: f"{user['username']} is an inactive user", 
    filter(lambda u: not u['tweets'], users)))

print(inactive)

t_name = [f"{name} is a cool guy" for name in names if len(name) < 5]
print(t_name)

# problem1
# filter out every number that is not divisible by 4 and
# then return a new list where every number is tripled
def triple_and_filter(L):
    fil = filter(lambda n: n % 4 == 0, L)
    return [n * 3 for n in fil]
    # or do:
    # return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

print(triple_and_filter([1,2,3,4]))