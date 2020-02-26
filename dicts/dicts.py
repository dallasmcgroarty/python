#using dictionaries

#creating dictionaries
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}
print(instructor)

cat = {"name": "blue", "age": 3.5, "isCute": True}
print(cat)
cat2 = dict(name="kitty")
print(cat2)
cat2 = dict(name="kitty", age=0.5)
print(cat2)

#accessing dictionaries

#accessing single values
print(instructor["name"])

print()
artist = {
    "first": "Niel",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
print(full_name)
print()
full_name = f"{artist['first']} {artist['last']}"
print(full_name)
print()

#iterating dictionaries

#.values() method gives all values in dict in list form
for value in instructor.values():
    print(value)

print()

#.keys() method gives all keys in dict in list form
for key in instructor.keys():
    print(key)

print()

#.items() method gives keys and values together
#need to use two variables to hold both key and value
for key, value in instructor.items():
    print(f"key is {key} and value is {value}")

print()

#get sum of values in a dict
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0
for dono in donations.values():
    total_donations += dono
print(total_donations)

print()

#using sum functions
total_donations = sum(dono for dono in donations.values())
#or
total_donations = sum(donations.values())
print(total_donations)

print()

#using in to check for keys in dictionaries
print("name" in instructor)

#checking for values in dictionaries
print("Colt" in instructor.values())
print("Nope!" in instructor.values())

print()

if "favorite_language" in instructor:
    print(f"favorite language is {instructor['favorite_language']}")

#dictionary methods
d = dict(a=1,b=2,c=3)

#clear() method clears all keys and values in dictionary
d.clear()

#copy() method makes a copy of a dict
clone = d.copy()

#fromkeys() method, creates key-value pairs from comma seperated values
{}.fromkeys("a","b")
{}.fromkeys(["email"], 'unknown')
{}.fromkeys("a", [1,2,3,4,5])

print()

#creates a dict with default values
new_user = {}.fromkeys(['name','score','email','profile bio'],'unknown')
print(new_user)
print()
new_user1 = new_user.fromkeys(range(1,10), 'unknown')
print(new_user1)

print()

#get() method gets a key in an object and return None instead of KeyError if the key doesnt exist
d = dict(a=1,b=2,c=3)
d['a'] # gets 1
print(d.get('a')) #gets 1
# d['no_key'] # error
d.get('no_key') #returns none 

print()

#check if a random chosen food is in a dict, 
# if it is print the amount otherwise print we dont make that
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
 
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
#using in method
if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that!")

#using get method
quantity = bakery_stock.get(food)
if quantity:
    print(f"{quantity} left")
else:
    print("We don't make that!")

print()

#generate a new dictionary given a list and initialize all values to 0
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

print()

#pop() method, takes a single argument corresponding to a key and removes
#the key value pair from the dict. Returns the value that was removed(not key)
d = dict(a=1,b=2,c=3)
popped = d.pop('a')
print(d)
print(popped)

#popitem() method removes a random key in a dictionary
d = dict(a=1,b=2,c=3,d=4,e=5)
popped = d.popitem()
print(d)
print(popped)
print(type(popped)) #returns a tuple

print()

#update() method, update keys and values in a dict with another set of key value pairs
first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}

second.update(first) #updates second with all of first dict pairs
print(second)

third = {"name": "Tony"} #adds new dict item to end of receiving dict
second.update(third)
print(second)

#exercise: using dict methods
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')