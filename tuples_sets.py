#tuples and sets in python
#tuple is an ordered collection or grouping of items
tuple1 = (1,2,3,4)

#tuples are immutable, meaning they can't be changed after created
alphabet = ('a', 'b', 'c', 'd')
print(type(alphabet))
print()

#tuples faster than lists, safer from bugs/changes you don't want
#work as valid keys in a dictionary

#common tuples: months in a year, denominations

#creating / accessing
#create using () or the tuple() function
#acces like a list
print(tuple1[0])
print()

#tuples as keys in a dictionary. Cannot use LISTS as KEYS in a dictionary
locations = {
    (35.6895,39.6917): "Tokyo",
    (40.7128, 74.0060): "New York",
    (37.7749, 122.4194): "San Francisco"
}
print(locations)
print()

#dictionary method .items() returns tuples instead of lists

#looping
names = ('colt','dallas','john', 'john')
for name in names:
    print(name)
print()

#count() returns number of times a value appears in a tuple
print(names.count('john'))
print()

#index() returns index at which a value is found in a tuple
print(names.index('dallas'))
print()

## Sets !! ****
#sets do not have duplicate values and there isnt any order
#cannot access items in a set by index
#sets are useful if you need to keep track of a collection of elements, but don't care about 
# ordering, keys or values and duplicates

#common use to find/store unique values

#creating / accessing sets
s = set({1,2,3,4,5,5,5}) #duplicates wont be allowed
s1 = {1,4,5}
print(s)
#use in to see if an item exists in the set
print(2 in s)
print()

#access the same as lists, use a for loop or loops
for item in s:
    print(item, end=" ")

print()
print()
#set methods!

#add() method adds an element into set, if element is already in set it won't add it
s1.add(10)
print(s1)
print()

#remove() method, removes value from a set, returns keyError if not found
s1.remove(10)
print(s1)
print()

#copy() method creates a copy of the set
s2 = s1.copy()
print(s2)
print()

#clear() method removes all the contents of the set

#Set Math !! ***

#Suppose you have two classes:
math_students = {'matt','helen','pirash','james','daniel'}
bio_students = {'jane','matt','charlotte','mesut','oliver','james'}

#want to get the union of both sets
union_set = math_students | bio_students
print(union_set)
print()

#want to get the intersection of both sets
inter_set = math_students & bio_students
print(inter_set)
print()

#create a variable which is a tuple with a single value of 1
value = tuple([1])
#or
value = (1,)

#convert list to tuple
values = [1,2,3,4]
static_values = tuple(values)
print(static_values)
print()
#convert list to set
stuff = [1,2,3,5,5,3,2,6,7,7,8]
unique_stuff = set(stuff)
print(unique_stuff)