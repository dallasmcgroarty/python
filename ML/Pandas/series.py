# pandas is a tool built on top of numpy
# it allows for fast analysis and data cleaning and preparation
# has built in visualization features
# it can work with data from a wide variety of sources
import numpy as np
import pandas as pd

# working with Series in Pandas

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(pd.Series(data=my_data))

# change index using labels list
series = pd.Series(data=my_data,index=labels)
print(series)

series = pd.Series(arr,labels)
print(series)

# using a dict
series = pd.Series(d)
print(series)

# can uses string or ints
print(pd.Series(data=labels))

# can even hold functions
print(pd.Series(data=[sum,print,len]))

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)

# getting values back from the series
# same as using a dictionary
print(ser1['USA'])

# using int as index
ser3 = pd.Series(data=labels)
print(ser3)

print(ser3[0])

# adding to series
print(ser1 + ser2)