import matplotlib.pyplot as plt
import numpy as np
from satellite import Satellite as sat


sat1 = sat()
sat_tuple = sat1.run()
x = sat_tuple(0)
y = sat_tuple(1)

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()

ax.scatter(x, y)
ax.plot(t, s)

fig.suptitle('Satellite Paths')
  
plt.show()

