# iterator - is an object that can be iterated upon. and object which returns data, one element at a time when next() is called on it
# iterable - is an object which will return an iterator when iter() is called on it

# ex. 'Hello' is an iterable, not an iterator
name = 'oprah'
print(iter(name))
it = iter(name)

print(next(iter(it)))
print(next(iter(it)))
print(next(iter(it)))
print()
#custom for loop

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)

def square(x):
    print(x*x)

my_for('hello', print)
print()
my_for([1,2,3,4], square)
