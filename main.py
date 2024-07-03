import matplotlib.pyplot as plt
import numpy as np
from satellite import Satellite


sat1 = Satellite()
sat_tuple = sat1.run([[0, 1, 2]], [[1, 1, 1]], 20)
func = sat_tuple[0]
x1 = np.linspace(0, 30, 200)
y1 = func(x1)
x2 = sat_tuple[1]
y2 = sat_tuple[2]

fig, ax = plt.subplots()

ax.plot(x1, y1)
ax.scatter(x2, y2)

fig.suptitle('Satellite Path')

plt.show()

