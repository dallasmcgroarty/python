# matplotlib part 1 lecture

import matplotlib.pyplot as plt
import numpy as np
# use plt.show() at end of plotting command to see the figure

# example

x = np.linspace(0,5,11)
y = x ** 2

print('x ->', x)
print('y ->', y)

# functional method for plotting

plt.plot(x,y)
#plt.show()

# add labels

plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
#plt.show()

# multi plots on same canvas
# arguments: num rows, num columns, plot number referring to
plt.subplot(1,2,1)
plt.plot(x,y,'r') # r = color of line red

plt.subplot(1,2,2)
plt.plot(y,x,'b') # b = color of line blue
#plt.show()

# Object oriented method for plotting **

fig = plt.figure() # blank canvas

# add axes to canvas/plot
# arguments: left, bottom, width, height / as a list
axes = fig.add_axes([0.1,0.1,0.8,0.8])

# plot on the axes
axes.plot(x,y)

# add labels and titles
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
#plt.show()

# two figures on one canvas
fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

# plot on the two axes
axes1.plot(x,y)
axes1.set_title('Larger Plot')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')
plt.show()