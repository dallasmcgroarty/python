# lambdas
# best used when passing a function into parameters of another function
def square(num): return num * num

square2 = lambda num: num * num

add = lambda a,b: a + b

print(add(3,10))
print(square(9))