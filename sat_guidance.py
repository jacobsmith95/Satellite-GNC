from numpy.polynomial import Polynomial


class Guidance():
    """A class which represents a guidance module for a satellite"""

    def __init__(self):
        """
        
        """
        self.path     = None
        self.next_pos = None

    def determine_path(self, state_vector):
        """
        
        """
        position_array = state_vector[0]
        x_array = []
        y_array = []
        for element in position_array:
            x_array.append(element[0])
            y_array.append(element[1])

        self.path = Polynomial.fit(x_array, y_array, 1)\
        
    def get_path(self):
        """returns the determined path"""
        return self.path