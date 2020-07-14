import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
print(tips.head())

# using plots to see categorical differences

# bar plot **
# allows you to aggregate the categorical data based of some function
# group by action
# one category column, one numerical column
# estimator argument used to change aggregate function used

# using plt.figure() to reset the figure, so
# plots dont stack on the same figure
plt.figure()
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
#plt.show()

# count plot **
# same as bar plot, but estimator is counting number of occurences

plt.figure()
sns.countplot(x='sex',data=tips)
#plt.show()

# box pots and violin plots **

# box plot shows the distribution of categorical data
plt.figure()
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
#plt.show()

# violinplot showing kde of underlying distribution
# harder to interpret
plt.figure()
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
#plt.show()

# strip plot **
# scatter plot based off category

plt.figure()
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex',split=True)
#plt.show()

# swarm plot **
# similar to strip plot, but points adjusted to not overlap
# like scatter + violin
# better for small data sets
# can add in violin plot on top of swarm plot

plt.figure()
#sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips)
#plt.show()

# factor plot **
# kind argument to specify which plot type you want

plt.figure()
sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')
plt.show()