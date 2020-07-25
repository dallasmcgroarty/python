import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('pandas_visual/df1',index_col=0)
print(df1.head())

df2 = pd.read_csv('pandas_visual/df2')
print(df2.head())

# histogram with pandas
df1['A'].hist()
#plt.show()

plt.figure()
df1['A'].plot(kind='hist',bins=30)
#plt.show()

# df1['A'].plot.hist() works as well


# area plot 
df2.plot.area(alpha=0.4)
#plt.show()

# bar plots
df2.plot.bar(stacked=True)
#plt.show()

# line plot
df1.plot.line(y='B',figsize=(12,3),lw=1)
#plt.show()

# scatter plot
df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')
#plt.show()

# scatter plot with size
df1.plot.scatter(x='A',y='B',s=df1['C']*100)
#plt.show()

# box plots
df2.plot.box()
#plt.show()

# hex plot !
df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='coolwarm')
#plt.show()

# kernel density estimation plot
plt.figure()
df2['a'].plot.kde()
#plt.show()

# just density
df2.plot.density()
plt.show()