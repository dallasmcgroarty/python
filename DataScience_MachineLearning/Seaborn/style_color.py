import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# style - ticks, darkgrid, whitegrid, 
sns.set_style('ticks')
sns.countplot(x='sex',data=tips)

# despine() gets rid of top and right spine
# argument left=True, bottom=True gets rid of all spines/borders
sns.despine()
#plt.show()

# use matplotlib figuresize with seaborn plots
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)
#plt.show()

plt.figure()
sns.set_context('poster')
sns.countplot(x='sex',data=tips)
#plt.show()

# palette for color changes, matplotlib.org colormaps
sns.set_context('notebook')
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')
plt.show()
