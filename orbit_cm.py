import numpy as np
from body import Body


class Orbit_CM():
    """
    A class which models an orbit in polar coordinates using Classical Mechanics given some 2 body objects with masses and positions

    This class assumes that body_2, the orbiting body, is of infinitesimal mass compared to the orbited body, body_1
    """

    def __init__(self, body_1: Body, body_2: Body, separation_distance, angular_momentum, eccentricity, gravitational_parameter):
        """initializes an orbit object"""
        self.body_1 = body_1
        self.body_2 = body_2
        self.orbit = None
        self.points = []

        self.sep_distance = separation_distance
        self.angular_mom  = angular_momentum
        self.eccentricity = eccentricity
        self.mu           = gravitational_parameter

    def calc_eccentricity(self):
        """calculates the eccentricity of the orbit"""

    def calc_angular_momentum(self):
        """calculates the angular momentum of the orbiting body"""

    def run_orbit(self, theta):
        """runs the orbit equation, returning a value r for a value of theta"""

        term_1 = (self.angular_mom**2)/((self.body_2.get_mass()**2)*self.mu)
        term_2 = 1/1+self.eccentricity*np.cos(theta)
        return term_1*term_2
    