#list comprehension

#double numbers in a list
numbers = [1,2,3,4,5]
double_numbers = [num * 2 for num in numbers]
print(double_numbers)

#uppercase each character in a string and convert to list
name = "dallas"
up_name = [char.upper() for char in name]
print(up_name)

#uppercase first letter of each string in a list
#upper() will only return a single character if using friend[0]
friends = ['john', 'logan', 'holden']
up_friends = [friend.capitalize() for friend in friends]
print(up_friends)

#creates a list of numbers 1 - 5 multiplied by 10
nums = [num * 10 for num in range(1,6)]
print(nums)

#convert list of numbers to list of strings
numbers = [1,2,3,4,5]
string_list = [str(num) for num in numbers]
print(string_list)

#list comprehension with conditional logic

#get evens or odds in a list of numbers
numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(odds)
print(evens)

#more conditionals
new_nums = [num * 2 if num % 2 == 0 else num/2 for num in numbers]
print(new_nums)

#take vowels out of a string
with_vowels = "this is so much fun!"
no_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(no_vowels)

#given two lists make a new list that is the intersection of the two
answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]
print(answer)

#given a list of words make a new list with each word reversed and in lowercase
answer2 = [name[::-1].lower() for name in ["Elie","Tim","Matt"]]
print(answer2)

#create a list of numbers from 1 - 100 that are divisible by 12
answer3 = [val for val in range(1,101) if val % 12 == 0]
print(answer3)

#given a string, create a list of all the letters excluding vowels
answer4 = [char for char in "amazing" if char not in 'aeiou']
print(answer4)

#nested lists: can contain any kind of element even other lists
nested_list = [[1,2,3,],[4,5,6],[7,8,9]]

print(nested_list[0][1])
print(nested_list[1][-1])
print(nested_list[1])

#looping through nested lists
for l in nested_list:
    for val in l:
        print(val, end = " ") #lets you print on same line, with space between each value

print("") # new line
#nested list comprehension, printing all values in nested list
[[print(val, end = " ") for val in l] for l in nested_list]

print("")
#game board example
board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

#X's and O's
table = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(table)

#***
stars = [["*" for x in range(1,4)] for i in range(1,4)]
print(stars)