#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:01:18 2019

@author: karadowling
"""

'''import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(5, 3))
ax.set(xlim=(-3, 3), ylim=(-1, 1))'''


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
   line.set_data([], [])
   return line,
def animate(i):
   x = np.linspace(0, 4, 1000)
   y = np.sin(2 * np.pi * (x - 0.01 * i))
   line.set_data(x, y)
   return line,


anim = FuncAnimation(fig, animate, init_func=init,
                              frames=200, interval=20, blit=True)


anim.save('sine_wave.mp4', writer='ffmpeg', dpi=512)
#im_ani.save('im.mp4', writer=writer)