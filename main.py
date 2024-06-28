import matplotlib.pyplot as plt
import numpy as np
from satellite import Satellite as sat


sat1 = sat(0, 1, 1, 1)
sat_tuple = sat1.run(8)
func = sat_tuple[0]
x1 = np.linspace(0, 2, 200)
y1 = func(x1)
x2 = sat_tuple[1]
y2 = sat_tuple[2]

fig, ax = plt.subplots()

ax.plot(x1, y1)
ax.scatter(x2, y2)

fig.suptitle('Satellite Paths')
  
plt.show()
print(sat_tuple)

