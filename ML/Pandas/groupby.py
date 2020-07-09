# group by method to group rows of data and call aggregate functions

# group by allows you to group together rows based off of a column
# and perform an aggregate function on them

import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
    'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
    'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

print(df)

# using group by to group a column
# then perform some aggregate function
print(df.groupby('Company'))

# store resulting object 
byComp = df.groupby('Company')

print(byComp.mean())

print(byComp.sum())

print(byComp.std())

print()
# get sum of FB sales only
print(byComp.sum().loc['FB'])

# one liner!
print(df.groupby('Company').sum().loc['FB'])

print(df.groupby('Company').count())

print(df.groupby('Company').max())

# use describe for a bunch of different information
print(df.groupby('Company').describe())

# use transpose to change format look
print(df.groupby('Company').describe().transpose())