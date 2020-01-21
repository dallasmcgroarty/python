# selection sort
# looks for largest or smallest value on each pass and then places it in the correct place
# big O(n^2)

def sel_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx], = arr[min_idx], arr[i]

a = [4,3,5,6,2,4,8]
sel_sort(a)
print(a)