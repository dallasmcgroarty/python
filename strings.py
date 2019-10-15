#f-strings in python3

#places a value in a string
x = 10
print(f"I've told you {x} times already")

#join function
#can use logic in the join argument

#takes a list and joins them together in a string
names = ["hey","there","tom"]
names_str = ' '.join(names)
print(names_str)

#takes a list of numbers and converts them into a string using join
numbers = [1,2,3,4,5,]
number_str = ''.join(str(num) for num in numbers)
print(number_str)