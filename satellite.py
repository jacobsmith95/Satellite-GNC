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

    def __init__(self, position_1, position_2, position_3, velocity):
        """initializes a satellite object"""
        
        self.guidance   = Guidance()
        self.navigation = Navigation()

        #self.curr_pos = position_3
        #self.scnd_pos = position_2
        #self.thrd_pos = position_1
        self.curr_vel = velocity
        self.curr_acc = None
        self.path     = None
        self.track    = {}
        self.x_list   = []
        self.y_list   = []

    def move(self, new_position):
        """moves the satellite object to the new position"""
        #self.thrd_pos = self.scnd_pos
        #self.scnd_pos = self.curr_pos
        #self.curr_pos = new_position

    def calculate_path(self):
        """"""
        self.orbit = Polynomial.fit(self.x_list, self.y_list, 1)

    def calc_next_move(self):
        """calculates the next move for the satellite"""

    def add_position(self, position):
        """adds x and y coordinates to the self.x_pos and self.y_pos attributes"""
        self.x_list.append(position[0])
        self.y_list.append(position[1])

    def run(self, position_array, velocity_array, timing):
        """runs the satellite object; returns self.orbit, self.x_pos, and self.y_pos"""
        self.add_position(self.curr_pos)
        self.add_position(self.curr_pos)
        self.calculate_path()
        for i in range(timing):
            x = self.curr_pos[0] + 0.1
            y = self.path(x)
            new_position = (x, y)
            self.move(new_position)
            self.add_position(self.curr_pos)

        return (self.path, self.x_list, self.y_list)