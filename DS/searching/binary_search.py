# binary seach method, uses divide and conquer
# divides the search space in half at each step
# O(logn) worst case
# list must be sorted in order to work

def binary_search(arr, target):
    first = 0
    last = len(arr)-1

    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr, 0))

# recursive version
def rec_binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid] == target:
            return True
        else:
            if target < arr[mid]:
                return rec_binary_search(arr[:mid], target)
            else:
                return rec_binary_search(arr[mid+1:], target)