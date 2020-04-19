class Player():

    def __init__(self, name, is_white, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.pos_x = start_x
        self.pos_y = start_y
        self.name = name
        self.is_white = is_white
    
    def return_position(self):
        return (self.pos_x, self.pos_y)
