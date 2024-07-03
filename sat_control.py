

class Control():
    """
    A class which represents a control module for a satellite
    """

    def __init__(self):
        """initializes a Control object"""
        self.acceleration = None
        self.state_vector = None

    def calculate_acceleration(self, next_position):
        """calculates the acceleration needed to reach the next given position"""


    def add_state_vector(self, state_vector):
        """adds the given state vector"""
        self.state_vector = state_vector

    def get_acceleration(self):
        """returns acceleration"""
        return self.accelerationS