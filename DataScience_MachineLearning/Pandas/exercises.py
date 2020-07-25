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

# ECOMMERCE Purchases exercises!***

# load csv file into df
ecom = pd.read_csv('Pandas/Ecommerce_Purchases')
print(ecom.head())
print()

# what is the average purchase price?
print('avg purchase price ->', ecom['Purchase Price'].mean())
print()

# how many rows and columns are there?
print(ecom.info()) # 10000 rows, 14 columns
print()

# what were the highest and lowest purchase prices?
print('highest price ->', ecom['Purchase Price'].max())
print('lowest price ->', ecom['Purchase Price'].min())
print()

# How many people have English 'en' as their Language of choice on the website?
print('number of "en" language users ->', ecom[ecom['Language']=='en']['Language'].value_counts())
print() # 1098
# can also use -> ecom[ecom['Language']=='en'].count()

# how many people have the job title of lawyer?
print('how many lawyers ->', ecom[ecom['Job']=='Lawyer']['Job'].value_counts())
print() #30
# can also do ecom[ecom['Job'] == 'Lawyer'].info()

# How many people made the purchase during the AM and how many people made the purchase during PM ?
print('number of AM purchases ->\n', ecom['AM or PM'].value_counts())
print()

# 5 most common job titles?
print('most common job titles ->\n', ecom['Job'].value_counts().head(5))
print()

# Someone made a purchase that came from Lot: \"90 WT\" , 
# what was the Purchase Price for this transaction?
print('Lot 90WT purchase price ->\n', ecom[ecom['Lot']=='90 WT']['Purchase Price'])
print()

# What is the email of the person with the following Credit Card Number: 4926535242672853?
print('Email of CC number ->\n', ecom[ecom['Credit Card']==4926535242672853]['Email'])
print()

# How many people have American Express as their Credit Card Provider *and* made a purchase above $95
print('american express and over $95 ->\n', ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price'] > 95)].count())
print() # 39

# Hard: How many people have a credit card that expires in 2025?
# cc exp date is 03/25 format, so slice using lambda
print('CC expires in 2025 ->', sum(ecom['CC Exp Date'].apply(lambda x:x[3:])=='25'))
print() # 1033

#Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
print('Most popular email providers ->\n', ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head())