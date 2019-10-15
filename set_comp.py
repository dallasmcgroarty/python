#Set Comprehension

#create set with each value squared
set1 = {x**2 for x in range(10)}
print(set1)
print()

#creates a dict because of the colon, not a set
set2 = {x:x**2 for x in range(10)}
print(set2)
print()

#only one l in the set, because of no duplicates
set3 = {char.upper() for char in 'hello'}
print(set3)
print()

#check what vowels or if all vowels are in a string
string1 = "hello"

set4 = {char for char in string1 if char in 'aeiou'}
print(set4)
print()

string2 = "mountain"

set5 = {char for char in string2 if char in 'aeiou'}
print(set5)
print()

number_of_vowels = len({char for char in string2 if char in 'aeiou'})
print(number_of_vowels)
print()
