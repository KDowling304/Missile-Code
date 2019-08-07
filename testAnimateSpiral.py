#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:52:49 2019

@author: karadowling
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

# initialization function
def init():
	# creating an empty plot/frame
	line.set_data([], [])
	return line,

# lists to store x and y axis points
xdata, ydata = [], []

# animation function
def animate(i):
	# t is a parameter
	t = 0.1*i

	# x, y values to be plotted
	x = t*np.sin(t)
	y = t*np.cos(t)

	# appending new points to x, y axes points list
	xdata.append(x)
	ydata.append(y)
	line.set_data(xdata, ydata)
	return line,

# setting a title for the plot
plt.title('Creating a growing coil with matplotlib!')
# hiding the axis details
plt.axis('off')

# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
							frames=500, interval=20, blit=True)

# save the animation as mp4 video file
#anim.save('coil.gif',writer='imagemagick')

anim.save('coil.mp4', writer='ffmpeg', dpi=512)