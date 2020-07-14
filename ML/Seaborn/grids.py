# using grids

import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
print(iris.head())

print(iris['species'].unique())

# pair grid
# have to specify/map your own plots

g = sns.PairGrid(iris)

g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
#plt.show()

# facet grid **

tips = sns.load_dataset('tips')

# seperate by col,row
# map plot with a column of data

g = sns.FacetGrid(data=tips,col='time',row='smoker')
#plt.figure()

g.map(sns.distplot,'total_bill')
#plt.show()

g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(plt.scatter,'total_bill','tip')
plt.show()