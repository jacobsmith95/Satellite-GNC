from numpy.polynomial import Polynomial


class Guidance():
    """
    A class which represents a guidance module for a satellite
    """

    def __init__(self):
        """initializes a Guidance object"""
        self.path     = None
        self.next_pos = None

    def determine_path(self, state_vector):
        """"""
        x_array = [0, 1, 2]
        y_array = state_vector[0]
        self.path = Polynomial.fit(x_array, y_array, 1)

    def determine_next_pos(self):
        """"""
        
    def get_path(self):
        """returns the determined path"""
        return self.path