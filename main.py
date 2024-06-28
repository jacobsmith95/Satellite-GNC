import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()

ax.scatter(t, s)
ax.plot(t, s)

fig.suptitle('Satellite Paths')
  
plt.show()

