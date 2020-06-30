from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No kwargs allowed')
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f'hi there {name}')

greet('Tony')

def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

print(twoSum([2,5,5,11], 16))