# any and all functions

# all -  returns true if all the elements of the iterable are truthy(or if empty)

people = ['Charlie', 'Casey', 'Cody','Carly','Cristina']

val = all([name[0] =='C' for name in people])
print(val)

# any - returns true if any element of the iterable is truthy(false if empty)

nums = [2,60,26,18]
val1 = any([num % 2 == 0 for num in nums])
print(val1)

# generator expressions
# instead of [] for list comp, use () and it wwont return a list or save to memory
# good for when plugging into function and you just want a true or false or a value
# and not an object back
val2 = (name[0] == 'C' for name in people)
print(val2)

import sys
list_comp = sys.getsizeof([x*10 for x in range(1000)])
gen_exp = sys.getsizeof(x*10 for x in range(1000))

print(f"List Comp: {list_comp} bytes")
print(f"Generator expr: {gen_exp} bytes")