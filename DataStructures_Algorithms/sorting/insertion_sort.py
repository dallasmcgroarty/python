# insertion sort method
# always maintains a sorted sub list in the lower positions of the list

def insert_sort(arr):
    for i in range(1, len(arr)):
        curr_val = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > curr_val:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = curr_val

a = [4,3,5,6,2,4,8]
insert_sort(a)
print(a)