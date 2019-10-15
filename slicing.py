#slicing in python 

#reversing strings
string1 = "wassup"
string2 = string1[::-1] #"pussaw"
print(string2)

#syntax --> some_list[start:end:step] - exclusive on end

#change values in a list
numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']
print(numbers) # [1,'a','b','c',4,5]

#swapping values in lists or strings
names = ["joe", "bob"]
names[0], names[1] = names[1], names[0]
print(names) #["bob", "joe"]