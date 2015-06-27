import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1000430)

n = 100
x = np.random.random(n)
y = np.random.random(n)
c = np.random.random(n) 
s = 500 * np.random.random(n) 

fig, ax = plt.subplots()
im = ax.scatter(x, y, c=c, s=s, cmap=plt.cm.jet)

fig.colorbar(im, ax=ax)

plt.savefig('plot_rnd.png')
plt.show()