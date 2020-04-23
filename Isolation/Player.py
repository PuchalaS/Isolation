class Agent():
    def fetch_action(self) -> tuple:
        pass


class AlphaBetaAgent(Agent):
    def __init__(self):
        self.__agent = AlphaBeta(...)

    def fetch_action(self):
        return self.agent.predict_action()

class Player(Agent):

    def __init__(self, name, is_white, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.pos_x = start_x
        self.pos_y = start_y
        self.name = name
        self.is_white = is_white
    
    def return_position(self):
        return (self.pos_x, self.pos_y)

    def fetch_action(self):
        player_input = input()
        #parse
        return ((1,2),(2,3))
