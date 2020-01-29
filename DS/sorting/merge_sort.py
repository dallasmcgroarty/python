# merge sort, fastest sort
# continue to split the list in half until you cannot split it anymore
# then merge the split lists together and sort them at the same time
# returns the new sorted arr after completion
# this implementation overwrites the given list

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        
arr = [11,2,5,77,3,5,9,4,23,12]

merge_sort(arr)
print(arr)