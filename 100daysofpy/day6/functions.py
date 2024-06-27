# functions

# define a function
def hello():
  print('Hello!')

hello()

# while loops
flag = True
p = 0
while flag:
  p += 1
  if p == 5:
    flag = False
print(p)

#Reeborg maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()