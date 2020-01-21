# bubble sort sorting method
# O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print('this is i: ' + str(i))
        for k in range(0, n-i-1):
            print('k index: ' + str(k))
            if arr[k] > arr[k+1]:
                arr[k+1], arr[k] = arr[k], arr[k+1]

a = [4,3,5,6,2,4,8]
bubble_sort(a)
print(a) 