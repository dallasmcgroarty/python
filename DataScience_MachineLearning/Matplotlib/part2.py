import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

fig, axes = plt.subplots(nrows=1,ncols=2)

# axes is a list of matplotlib axes, so can iterate through
print(axes)

# for current_ax in axes:
#     current_ax.plot(x,y)

#axes.plot(x,y)

axes[0].plot(x,y)
axes[0].set_title('First')

axes[1].plot(y,x)
axes[1].set_title('Second')

# use tight layout to deal with overlapping plots
# probs good to use all the time anyway
plt.tight_layout()
#plt.show()

# ***figure size and DPI ****

# figsize arguments: width,height in inches
# dpi = dots per inch/pixels per inch

# fig = plt.figure(figsize=(8,2),dpi=100)

# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y)

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))

axes[0].plot(x,y)

axes[1].plot(x,y)

plt.tight_layout()
#plt.show()

# saving a figure to a file ***

# can save to png, jpg, eps, svg, pgf, pdf
# can also specify dpi here
fig.savefig('Matplotlib/my_pic.png',dpi=200)

# adding a legend to the plot
fig = plt.figure()

ax = fig.add_axes([0.1,0.1,.8,.8])

ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')

# can specify location for the legend
# can enter a tuple to specify location as well
ax.legend(loc=0)
plt.show()