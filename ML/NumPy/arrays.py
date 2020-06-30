import numpy as np
#casting python list to numpy array

my_list = [1,2,3]

arr = np.array(my_list)

print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]

print(np.array(my_mat))

#most common way to make array using np.arange()

arr1 = np.arange(0,10)
print(arr1)

# add a step
arr1 = np.arange(0,11,2)
print(arr1)

# all zeros array
zeros = np.zeros(5)
print(zeros)

# all zeros with 2d array
zeros = np.zeros((2,5))
print(zeros)

#just ones
ones = np.ones(5)
print(ones)

# linspace() creates an array of evenly spaced numbers between start and stop.
space = np.linspace(0,5,10)
print(space)

# eye() creates an identity matrix
eye = np.eye(4)
print(eye)

# random.rand() creates array of random numbers from 0 to 1 uniformly distributed
rando = np.random.rand(5)
print(rando)

# 2d rand()
rando = np.random.rand(5,5)
print(rando)

#  standard normal distribution centered around 0
standard = np.random.randn(2)
print(standard)

# random integer from inclusive on start to exclusive on end
randint = np.random.randint(1,100)
print(randint)

randint = np.random.randint(1,100,5)
print(randint)

# random array of ints
ranarr = np.random.randint(0,50,10)
print(ranarr)

# reshape array, must have equal size when reshaping
arr = np.arange(25)
reshape = arr.reshape(5,5)
print(reshape)

# max and min 
print(ranarr.max())
print(ranarr.min())

# index of max and min value
print(ranarr.argmax())
print(ranarr.argmin())

# how to get the shape of the array
print(arr.shape)
print(reshape.shape)

# get the data type in the array
print(arr.dtype)