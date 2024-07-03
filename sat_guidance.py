from numpy.polynomial import Polynomial


class Guidance():
    """
    A class which represents a guidance module for a satellite
    """

    def __init__(self):
        """initializes a Guidance object"""
        self.path         = None
        self.next_pos     = None
        self.avoid_pos    = None
        self.state_vector = None

    def determine_path(self):
        """"""
        x_array = [0, 1, 2]
        y_array = self.state_vector[0]
        self.path = Polynomial.fit(x_array, y_array, 1)

    def determine_next_pos(self, x_position, acceleration, time):
        """calculates the next desired position for the satellite"""
        velocity = self.state_vector[1][2]
        displacement = (velocity * time) + (0.5 * acceleration * (time^2))
        self.next_pos = (x_position, displacement)

    def calculate_avoidance_pos(self, x_position, time):
        """calculates the position needed to avoid collision"""
        velocity = self.state_vector[1][2]
        displacement = (velocity * (time+3))+3
        self.avoid_pos = (x_position+3, displacement)

    def add_state_vector(self, state_vector):
        """"""
        self.state_vector = state_vector
        
    def get_path(self):
        """returns the determined path"""
        return self.path
    
    def get_next_pos(self):
        """returns the calculated next position"""
        return self.next_pos
    
    def get_avoid_pos(self):
        """returns the calculated avoidance position"""
        return self.avoid_pos