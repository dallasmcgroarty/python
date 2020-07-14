import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

# want data in matrix form first
# in order to use heatmap
tc = tips.corr()
print(tc)

# heatmap **
# annot argument to specify number value
sns.heatmap(tc,annot=True,cmap='coolwarm')
#plt.show()

# convert flights to matrix form
print()
fp = flights.pivot_table(index='month',columns='year',values='passengers')

# can change linecolor and linewidth if needed
plt.figure()
sns.heatmap(fp,cmap='magma',linecolor='white',linewidth=1)
#plt.show()

# cluster map **
# cluster version of heat map
# standard scale to normalize the cluster data from 0 - 1
plt.figure()
sns.clustermap(fp,cmap='coolwarm',standard_scale=1)
plt.show()