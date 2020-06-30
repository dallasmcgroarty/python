import numpy as np

arr = np.arange(0,11)
print(arr[8])

# array from index 1-5(not including 5)
print(arr[1:5])

# array from 5 to the rest of the array
print(arr[5:])

# change values in that range to the given value
arr[0:5] = 100
print(arr)

arr = np.arange(0,11)

# does not copy the array to slices, just references the original
slices = arr[0:6]
slices[:] = 99
print(slices)
print(arr)

# copy array instead of using reference
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
print(arr)

# indexing 2D array

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

# first item in first row and column
print(arr_2d[0][0])

# indexing with comma instead of brackets
print(arr_2d[1,2])

# indexing multiple values within the 2d array
# get the right corner (4 values)
print(arr_2d[:2,1:])

# get bottom right corner
print(arr_2d[1:,1:])


##** conditional selection

arr = np.arange(0,11)

# convert array to a boolean array using comparison
bool_arr = arr > 5
print(bool_arr)

# conditionally select values from the original array where the value is true
# in the boolean array
print(arr[bool_arr])

# all in one step!
print(arr[arr>5])