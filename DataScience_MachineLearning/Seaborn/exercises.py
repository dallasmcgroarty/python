import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())

# example joing plot
sns.jointplot(x='fare',y='age',data=titanic)


# example dist plot
plt.figure()
sns.distplot(titanic['fare'],kde=False,bins=30,color='red')
#plt.show()

# example box plot
plt.figure()
sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')
#plt.show()

# swarmplot example
plt.figure()
sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
#plt.show()

# countplot example
plt.figure()
sns.countplot(x='sex',data=titanic)
#plt.show()

# heat map example
plt.figure()
tc = titanic.corr()
sns.heatmap(tc,cmap='coolwarm')
plt.title('titanic.corr()')
#plt.show()

# facet grid example
plt.figure()
g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
plt.show()