# shell sort method
# like insertion sort but breaks list into sublists
# use increment to create sub lists

def shell_sort(arr):
    sublistcount = len(arr) // 2
    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion(arr, start, sublistcount)
        sublistcount = sublistcount // 2

def gap_insertion(arr, start, gap):
    for i in range (start+gap, len(arr), gap):
        curr_val = arr[i]
        pos = i

        while pos >= gap and arr[pos-gap] > curr_val:
            arr[pos] = arr[pos-gap]
            pos = pos-gap
        
        arr[pos] = curr_val
    
a = [4,3,5,6,2,4,8]
shell_sort(a)
print(a)