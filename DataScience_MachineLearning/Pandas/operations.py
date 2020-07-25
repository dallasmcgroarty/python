import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                    'col2':[444,555,666,444],
                    'col3':['abc','def','ghi','xyz']})

print(df.head())
print()

# finding unique values in a dataframe***

#unique() gives array of all unique values
print(df['col2'].unique())
print()

#nunique() gives number of unique values
print(df['col2'].nunique())
print()

# value_counts() gives the number of times each value is repeated
print(df['col2'].value_counts())
print()

# conditional selection
print(df[df['col1']>2])
print()

print(df[(df['col1']>2) & (df['col2']==444)])
print()

# apply method!!

def times2(x):
    return x * 2

# apply custom function onto dataframe
print(df['col1'].apply(times2))
print()

# can also use apply with built in functions
print(df['col3'].apply(len))
print()

# using lambda expressions!**
# very powerful and useful!***
print(df['col2'].apply(lambda x: x*2))
print()

# removing columns!
# inplace = true to actually remove it
print(df.drop('col1',axis=1))
print()

# get columns and index names
print(df.columns)
print()

print(df.index)
print()

# sort and order dataframe
print(df)
print()

# specify which column you want to sort by
print(df.sort_values('col2'))
print()

# isnull() to find null values in dataframe
print(df.isnull())
print()

# Pivot table! ***
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
print()

# create a pivot table
print(df.pivot_table(values='D',index=['A','B'],columns=['C']))