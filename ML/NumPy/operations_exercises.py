import numpy as np

arr = np.arange(0,11)

print(arr)

# add two arrays together
print(arr + arr)

# subtract two arrays
print(arr - arr)

# multiply two arrays
print(arr * arr)

# add 100 to each element in array
# works same way for subtraction and multiply
print(arr + 100)

# array to the power
print(arr ** 2)

#square root of elements in array
print(np.sqrt(arr))

#exponential
print(np.exp(arr))

#max value
print(np.max(arr))

# sin
print(np.sin(arr))

# log
print(np.log(arr))

##*** exercises

#import numpy
#import numpy as np

# array of 10 zeros
arr = np.zeros(10)
print(arr)

# array of ten ones
arr = np.ones(10)
print(arr)

# array of ten fives
arr = np.ones(10) * 5
print(arr)

# array of integers from 10 to 50
arr = np.arange(10,51)
print(arr)

# array of all even integers from 10 to 50
arr = np.arange(10,51,2)
print(arr)

# 3x3 matrix from 0 to 8
arr = np.arange(0,9).reshape(3,3)
print(arr)

# random num between 0 and 1
rand = np.random.rand(1)
print(rand)

# array of 25 random numbers sampled from a standard normal distribution
arr = np.random.randn(25)
print(arr)

# matrix of numbers from 0.01 to 1
arr = np.arange(1,101).reshape(10,10) / 100
print(arr)

# array of 20 linearly spaced points between 0 and 1
arr = np.linspace(0,1,20)
print(arr)

# given this matrix 
mat = np.arange(1,26).reshape(5,5)
print(mat)

# get values from 12 to 25 but none from the first column
print(mat[2:,1:])

# get value 12 from the matrix
val = mat[3,4]
print(val)

# get values 2, 7 and 12 from the matrix
print(mat[:3,1:2])

# get the last row from the matrix
print(mat[4,0:])

# get sum of all values in matrix
print(np.sum(mat))

# get the standard deviation of the values in mat
print(np.std(mat))

# get the sum of all the columns in matrix
print(sum(mat))