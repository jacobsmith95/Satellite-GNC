from numpy.polynomial import Polynomial
from sat_guidance import Guidance
from sat_navigation import Navigation


class Satellite():
    """
    Creates a satellite object with 3 sub-objects for:
        Guidance
        Navigation
        Control

    The satellite object consumes position data fed from the orbit simulator,
    in order to simulate the satellite gathering position data from sensors
    """

    def __init__(self):
        """initializes a Satellite object"""
        self.guidance   = Guidance()
        self.navigation = Navigation()

        self.curr_pos = None
        self.curr_vel = None
        self.curr_acc = None
        self.path     = None
        self.track    = {}
        self.x_list   = []
        self.y_list   = []

    def update_position(self, new_position):
        """updates the satellite's current position"""
        self.curr_pos = new_position

    def calculate_path(self):
        """"""
        self.orbit = Polynomial.fit(self.x_list, self.y_list, 1)

    def calc_next_move(self):
        """calculates the next move for the satellite"""

    def add_position(self):
        """adds current x and y coordinates to the self.x_pos and self.y_pos attributes"""
        self.x_list.append(self.curr_pos[0])
        self.y_list.append(self.curr_pos[1])

    def run(self, position_array, velocity_array, timing):
        """runs the satellite object; returns self.orbit, self.x_pos, and self.y_pos"""

        self.navigation.create_state_vector(position_array, velocity_array)
        self.guidance.add_state_vector(self.navigation.get_state_vector())
        self.guidance.determine_path()
        path = self.guidance.get_path()
        self.update_position((3, position_array[0][2]))

        for time in range(timing):
            self.guidance.add_state_vector(self.navigation.get_state_vector())
            self.guidance.determine_next_pos(self.curr_pos[0] + 1, time+4)
            next_pos = self.guidance.get_next_pos()
            self.update_position(next_pos)
            self.add_position()

        return (path, self.x_list, self.y_list)
