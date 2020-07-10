# setting line color, line width, line types
# customizing plot appearance

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

# edit color with color argument
# can also use Hex codes for color / RGB
# use linewidth(lw) argument to edit line width
#use alpha argument to change opacity
# use linestyle(ls) to edit line style (--,-.,::,-)
# can also use markers, which map data points (*,+,o,1,.)
ax.plot(x,y,color='orange', lw=2, alpha=0.5, ls='--', marker='o', 
        markersize=5, markerfacecolor='blue',markeredgewidth=2,markeredgecolor='green')
#plt.show()

#** control over axis appearance and plot range **

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color='blue', lw=2,ls='--')

# set x and y limits
# lower and upperbound
ax.set_xlim([0,1])
ax.set_ylim([0,2])
#plt.show()