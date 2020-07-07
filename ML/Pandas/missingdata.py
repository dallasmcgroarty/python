# fixing missing data in pandas
import numpy as np
import pandas as pd

# dataframe with some missing values
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

# drop na method - will drop any row with a Null value
# need inplace argument set to true to affect original dataframe
df.dropna()
print(df)

# drop na with column instead of rows
# need inplace argument set to true to affect original dataframe
df.dropna(axis=1)
print(df)

# setting threshold of dropna method
# need inplace argument set to true to affect original dataframe
# will only drop a row if there are atleast 2 Null values
df.dropna(thresh=2,inplace=False)
print(df)

# fill na method - fills in null values
df1 = df.fillna(value='Fill')
print(df1)

# fill with mean of the column
print(df['A'])
df['A'].fillna(inplace=True,value=df['A'].mean())
print(df['A'])
