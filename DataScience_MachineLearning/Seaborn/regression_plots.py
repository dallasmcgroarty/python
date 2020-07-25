# regression plotttsss

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
print(tips.head())

# lmplot
# displaying linear models

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],
            scatter_kws={'s':100})
#plt.show()

sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',
            aspect=0.6,size=8)
plt.show()

