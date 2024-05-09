import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)
y1 = np.cos(x**2)
fig, ax = plt.subplots()
print(ax.plot(x,y))
print(ax.set_title('A single plot'))
fig, axs = plt.subplots(2)
fig.suptitle('Vertically Stacked subplots')
axs[0].plot(x,y)
axs[1].plot(x,y1, 'red')
print(plt.show())