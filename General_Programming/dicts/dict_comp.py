#dictionary comprehension

#syntax {__:__ for __ in __}
#iterates over keys by default
#to iterate over keys and values use .items()

#iter over dict
numbers = dict(first=1, second=2, third = 3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers)

print()
#creates dict using list, index is list items, value is index squared
nums = {num: num ** 2 for num in [1,2,3,4,5]}
print(nums)

print()

#interweaving two strings to create a dict, A - 1, B - 2, C - 3
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)
#can also use zip() function
dict(zip(str1,str2))

print()

#upper each char in each key and value in dict
instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {k.upper(): v.upper() for k,v in instructor.items()}
print(yelling_instructor)

print()

#conditional logic with dicts
num_list = [1,2,3,4,]

even_odds = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(even_odds)

#create a dict from a nested list
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer = dict(person)
# or
answer1 = {key: value for key, value in person}

print(answer)

print()

#create a dict with keys as vowels and value is 0.
answer = {key: 0 for key in 'aeiou'}
# or
answer1 = dict.fromkeys('aeiou', 0)

print(answer)
print()

# create a dict with ascii numbers and their associated letter
answer = {key: chr(key) for key in range(65,91)}

print(answer)
print()