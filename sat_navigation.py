import numpy as np


class Navigation():
    """An object which represents a navigation module for the """

    def __init__(self):
        """

        """
        self.state_vector = None

    def create_state_vector(self, position_1, position_2, position_3, velocity):
        """
        creates a state vector from position and velocity data
        """
        position_vector = np.array([position_1, position_2, position_3])
        velocity_vector = np.array([velocity, velocity, velocity])
        
        self.state_vector = np.array([position_vector, velocity_vector])

    def get_state_vector(self):
        """
        returns the state vector
        """
        return self.state_vector



    