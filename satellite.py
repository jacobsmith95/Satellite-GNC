

class Satellite():
    """
    
    """

    def __init__(self, position, velocity, acceleration):
        """initializes a satellite object"""
        self.pos   = position
        self.vel   = velocity
        self.acc   = acceleration
        self.orbit = None
        self.track = {}
        self.x_pos = []
        self.y_pos = []

    def move(self, new_position):
        """moves the satellite object to the new position"""
        self.pos = new_position

    def calc_orbit(self):
        """"""


    def add_position(position):
        """adds x and y coordinates to the self.x_pos and self.y_pos attributes"""

    def run(self):
        """runs the satellite object; returns self.orbit, self.x_pos, and self.y_pos"""