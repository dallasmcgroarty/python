#lists, offsets, appending to lists
import random

states = ['Delaware', 'Calfifornia', 'Oregon', 'Texas']
print(states)

# using index to get state at that index
print(states[1])

# get last item in list
# using negative index starts from the back of list
print(states[-1])

# update item at that index
states[0] = 'Delawaria'
print(states)

# add to end of list
states.append('Missouri')
print(states)

#add to beginning of list
states.insert(0, 'New York')
print(states)

# extend list with multiple elements
states.extend(['Arizona', 'Nevada'])
print(states)

# randomly choose name from list
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

chosen = names[random.randint(0,len(names)-1)]
print(f'{chosen} is going to buy the meal today!')

#nested lists
nested = [names, states]
print(nested)

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")