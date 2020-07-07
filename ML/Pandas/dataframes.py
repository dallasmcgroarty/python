import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

# each column and row is a pandas series
# all share common index, basically from dataframe is
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

# indexing and selection
print(df['W'])

# can also use . but can get confusing
print(df.W)

# multiple columns
# pass in list of column names
print(df[['W','Z']])

# creating a new column in a dataframe
df['new'] = df['W'] + df['Y']
print(df)

# drop a column/delete it
# need axis = 1 to delete a column
# need inplace = New
df.drop('new', axis=1, inplace=True)
print(df)

# drop rows too
df.drop('E', axis=0, inplace=True)
print(df)

# get the shape of the dataframe
print(df.shape)

# selecting rows from a dataframe
print(df.loc['A'])

# selecting row C by using index instead
print(df.iloc[2])

# select single value
print(df.loc['B','Y'])

# selecting a subset
print(df.loc[['A','B'],['W','Y']])

##******* dataframes part 2!

# can use conditionals with dataframes
booldf = df > 0

print(booldf)

# using this statement, the values that were True will show the int
# and false will be Nan
print(df[booldf])

# simplified
print(df[df>0])

# most likely the way youd use conditionals on a dataframe
# just use it on a row or column
print(df['W'] > 0)

print(df[df['W']>0])

# want to get rows where Z is less than 0
print(df[df['Z']<0])

# can store the resulting frame
resultdf = df[df['W']>0]

print(resultdf['X'])

# all one step
print(df[df['W']>0]['X'])

# also get multiple 
print(df[df['W']>0][['Y','X']])

# broken down to show how this works
boolser = df['W'] > 0
result = df[boolser]
mycols = ['Y','X']
print(result[mycols])

# multiple conditions
# note the use of & is needed when using a series
print(df[(df['W']>0) & (df['Y']<1)])

# for or use |
print(df[(df['W']>0) | (df['Y']>1)])

# resetting the index or changing it
print(df)

#reset index
# to do it inplace/save it, use inplace=True in the argument 
print(df.reset_index())

# another index example
# setting the index
newind = 'CA NY WY OR'.split()
print(newind)

# set index like this
# creates a new column
df['States'] = newind
print(df)

# create a new row
# to do it inplace/save it, use inplace=True in the argument
print(df.set_index('States'))


### ******** dataframes part 3

# multi level index dataframes

# index levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

# multi-level index dataframe with 6 rows, 2 columns
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

# calling data from this 
print(df.loc['G1'])
print(df.loc['G1'].loc[1])

# call outside first and go inward

# set index names
df.index.names = ['Groups','Num']
print(df)

# get value in G2, num 2, column b
print(df.loc['G2'].loc[2,'B'])

# another way, grabbing cross sections
print(df.xs('G1'))

print(df.xs(1,level='Num'))