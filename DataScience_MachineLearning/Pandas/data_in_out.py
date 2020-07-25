import pandas as pd

#read csv file
ex = pd.read_csv('Pandas/example.csv')
print(ex)
print()

df = pd.read_csv('Pandas/example.csv')

# write dataframe to csv file
df.to_csv('Pandas/My_output',index=False)

df = pd.read_excel('Pandas/Excel_Sample.xlsx',sheet_name='Sheet1')
print(df)
print()

# write dataframe to excel file
df.to_excel('Pandas/Excel_Sample2.xlsx',sheet_name='NewSheet')

# read html data
data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')

# read_html return a list
print(type(data))

print(data[0])

print(data[0].head())

# SQL with pandas

from sqlalchemy import create_engine

# create sqlite engine in memory
engine = create_engine('sqlite:///:memory:')

# write df to sql 
df.to_sql('my_table',engine)

# read the sql data into data frame
sqldf = pd.read_sql('my_table',con=engine)
print(sqldf)