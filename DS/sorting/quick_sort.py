#quicksort sorting method
# uses divide and conquer
# selects a pivot value to split the list
# sorts items based on the pivot value
# once left and right marks cross, switch pivot value

def quick_sort(arr):

    # call help function with arr, first pos and last pos
    quick_sort_help(arr,0,len(arr)-1)
    

def quick_sort_help(arr, first, last):
    
    if first < last:
        # get splitpoint using partition
        splitpoint = partition(arr,first,last)

        # recursively call both sides of arr
        quick_sort_help(arr,first,splitpoint-1)

        quick_sort_help(arr,splitpoint+1, last)

def partition(arr, first, last):
    
    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1
        
        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark-=1
        
        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

arr = [2,5,4,6,7,3,1,4,12,11]
quick_sort(arr)
print(arr)