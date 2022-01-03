import random
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(100, 100)
theta = np.linspace(0, 2*np.pi, 100)
radius = 10

for i in ax:
	for j in i:
		a = radius*np.cos(theta)
		b = radius*np.sin(theta)
		j.plot(a, b)
		j.axis('off')

plt.show()
