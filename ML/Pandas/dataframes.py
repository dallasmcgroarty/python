import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

# each column is a pandas series
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