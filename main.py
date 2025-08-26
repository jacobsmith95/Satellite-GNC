import matplotlib.pyplot as plt
import numpy as np
from satellite import Satellite
from body import Body
from orbit_cm import Orbit_CM as Orbit

"""
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
ax.plot(x2, y2)

fig.suptitle('Satellite Path')

plt.show()
"""

body_1 = Body(30, [0,0], [0,0])
body_2 = Body(1, [10,5], [0,0])
orbit = Orbit(body_1, body_2, 10,  3.98)
theta = np.arange(0, np.pi*2, 0.01)
r = orbit.run_orbit(theta)

fig, ax = plt.subplots(figsize=(5, 8), subplot_kw={'projection': 'polar'},
                        layout='constrained')
ax = ax
ax.plot(theta, r)
ax.set_rmax(15)
ax.set_rticks([1, 2])  # Fewer radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Orbits", va='bottom')

"""
ax = axs[1]
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rmin(1)  # Change the radial axis to only go from 1 to 2
ax.set_rorigin(0)  # Set the origin of the radial axis to 0
ax.set_thetamin(0)
ax.set_thetamax(225)
ax.set_rticks([1, 1.5, 2])  # Fewer radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line


ax.grid(True)
ax.set_title("Same plot, but with reduced axis limits", va='bottom')
"""
plt.show()
