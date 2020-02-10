# infinite generator
# allows you to just hold one value instead of a giant list or dict
def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

beat = current_beat()
num = 5
print(next(beat))
print(next(beat))