import numpy as np


class Navigation():
    """
    A class which represents a navigation module for a satellite
    """

    def __init__(self):
        """initializes a Navigation object"""
        self.state_vector = None

    def create_state_vector(self, position_array, velocity_array):
        """creates a state vector from position and velocity data"""
        position_vector = np.array(position_array)
        velocity_vector = np.array(velocity_array)
        
        self.state_vector = np.concatenate((position_vector, velocity_vector), axis=0)

    def get_state_vector(self):
        """returns the state vector"""
        return self.state_vector



    