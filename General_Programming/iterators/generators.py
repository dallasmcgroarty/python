# generators are iterators
# can be created with generator functions
# uses the yield keyword
# can yield multiple times
# can be created with generator expressions
# when invoked returns a generator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

c = count_up_to(5)
next(c) # moves forward one
for i in c:
    print(i)

def yes_or_no():
    pas = 0
    while True:
        if pas == 0:
            yield 'yes'
            pas += 1
        else:
            yield 'no'
            pas -= 1

p = yes_or_no()
print(next(p))
print(next(p))
print(next(p))

def make_song(num=99,bev='soda'):
    while num > 0:
        if num == 1:
            yield 'Only 1 bottle of ' + bev + ' left!'
        else:
            yield str(num) + ' bottles of ' + bev + ' on the wall.'
        num -= 1
    yield 'No more ' + bev + '!'
    
c = make_song(5, 'pop')
for i in c:
    print(i)

def fib_gen(num):
    x = 0
    y = 1
    count = 0
    while count < num:
        x, y = y, x + y
        yield x
        count += 1

for n in fib_gen(10):
    print(n)


#***** generator expressions
import time
# look like list comps
# use () instead of []

g = (num for num in range(1,10))
print(next(g))

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_stop = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_stop = time.time() - list_start_time

print(f"gen took {gen_stop}")
print(f"list took {list_stop}")