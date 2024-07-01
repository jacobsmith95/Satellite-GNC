from numpy import polynomial as poly


class Satellite():
    """
    
    """

    def __init__(self, x_1, y_1, x_2, y_2):
        """initializes a satellite object"""
        self.curr_pos = (x_2, y_2)
        self.past_pos = (x_1, y_1)
        #self.vel      = velocity
        #self.acc      = acceleration
        self.orbit    = None
        self.track    = {}
        self.x_lst    = []
        self.y_lst    = []

    def move(self, new_position):
        """moves the satellite object to the new position"""
        self.past_pos = self.curr_pos
        self.curr_pos = new_position

    def calc_orbit(self):
        """"""
        

    def calc_next_move(self):
        """calculates the next move for the satellite"""

    def add_position(self, position):
        """adds x and y coordinates to the self.x_pos and self.y_pos attributes"""
        self.x_lst.append(position[0])
        self.y_lst.append(position[1])

    def run(self, timing):
        """runs the satellite object; returns self.orbit, self.x_pos, and self.y_pos"""
        self.add_position(self.pos)
        for i in range(timing):
            x = self.curr_pos[0] + 0.1
            y = self.orbit(x)
            new_position = (x, y)
            self.move(new_position)
            self.add_position(self.pos)

        return (self.orbit, self.x_lst, self.y_lst)