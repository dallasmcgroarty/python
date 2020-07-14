import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

print(tips.head())

# dist plot - distribution plot

# pass in single column of dataframe
# bins argument to change number of bins/points
# kde = kernel density estimation
sns.distplot(tips['total_bill'],kde=False,bins=30)
#plt.show()

# joint plot **

# can combine two distribution plots
# kind argument can change inside plot (hex,reg,kde)
# reg adds a regression line
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
#plt.show()

# pair plot **

# plot pairwise relationships across entire dataframe
# color hue for categorical columns
# hue used to change color of points for different categories
sns.pairplot(tips,hue='sex',palette='coolwarm')
#plt.show()

# rug plot **

# draws dash mark for every point on the distribution
# plots datapoints in an array as sticks on an axis.
sns.rugplot(tips['total_bill'])
#plt.show()

# kde plot

#sns.kdeplot(tips['total_bill'])
plt.show()