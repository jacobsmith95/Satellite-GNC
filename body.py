import numpy as np


class Body():
    """
    Models a celestial body object with a mass and a position vector
    """

    def __init__(self, mass, position_vector, velocity_vector):
        """creates a celestial body object with a mass and position vector"""
        self.mass = mass
        self.position = np.array(position_vector)
        self.velocity = np.array(velocity_vector)

    def get_mass(self):
        """returns the mass of the celestial body"""
        return self.mass
    
    def get_position(self):
        """returns the position of the celestial body"""
        return self.position
    
    def get_velocity(self):
        """returns the velocity vector of the celestial body"""
        return self.velocity
    
    def update_position(self, new_position_vector):
        """updates the position vector of the celestial body"""
        self.position = new_position_vector
        