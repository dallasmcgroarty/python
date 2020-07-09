# SF salaries exercise
# download sf salaries dataset from Kaggle

import pandas as pd

sal = pd.read_csv('Pandas/Salaries.csv')

print(sal.head())

# get info 
print(sal.info()) # 148,654 entries
print()

# what is the average base pay?
print('avg base pay ->', sal['BasePay'].mean()) # $66,325.44884
print()

# what is the highest amount of OvertimePay in the dataset?
print('highest overtime pay ->', sal['OvertimePay'].max()) # 245,131
print()

# what is the job of JOSEPH DRISCOLL?
print('job of joseph driscoll ->\n', sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
print() # captain, fire supression

# how much does joseph driscoll make including benefits?
print('joseph driscoll benefits ->\n', sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])
print() # $270,324.91

# what is the name of the highest paid person (including benefits)
print('highest paid person ->\n', sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()])
print() # nathaniel ford

# what was the name of the lowest paid person?
print('lowest paid person ->\n', sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()])
print() # joe lopez

# what was the average (mean) BasePay of all employees per year? (2011-2014)?
print('average basepay per year from 2011-2014 ->\n', sal.groupby('Year')['BasePay'].mean())
print()

# how many unique job titles are there?
print('number of unique job titles -> ', sal['JobTitle'].nunique())
print() # 2159

# what are the top 5 most common jobs?
print('top 5 most common jobs ->\n', sal['JobTitle'].value_counts().head(5))
print()

# how many job titles were represented by only one person in 2013?
print('number of job titles held by one person ->', sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1))
print() # 202

# how many people have the word chief in their job title?
def chief(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

print('chief in job title ->', sum(sal['JobTitle'].apply(lambda x: chief(x))))
print() # 627

# is there a correlation between length of the job title string and salary?
sal['title_len'] = sal['JobTitle'].apply(len)
print('correlation between length of job title and salary ->\n', sal[['title_len','TotalPayBenefits']].corr())
# no correlation