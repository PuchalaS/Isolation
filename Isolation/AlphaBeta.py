import numpy as np
from Isolation.Board import Board


class AlphaBeta(object):
    def __init__(self, board: Board, current_player: int, depth: int):
        self.board = board
        self.depth = depth
        self.__alpha = (-1) * np.inf
        self.__beta = np.inf
        self.current_player = current_player
        self.evaluate = lambda: 1

    def predict_state(self):        
        def AlphaBetaMax(state, alpha, beta, depth_left):
            if depth_left == 0:
                return (state, self.evaluate())

            for possible_state in possible_states(state, 2):
                found_state, score = AlphaBetaMin(
                    possible_state, 
                    alpha, 
                    beta,
                    depth_left - 1)
                if score >= beta:
                    return (found_state, beta)
                if score > alpha:
                    alpha = score

        def AlphaBetaMin(state, alpha, beta, depth_left):
            if depth_left == 0:
                return (state, -self.evaluate())

            for possible_state in possible_states(state, 3):
                found_state, score = AlphaBetaMin(
                    possible_state, 
                    alpha, 
                    beta, 
                    depth_left - 1)
                if score <= alpha:
                    return (found_state, alpha)
                if score < beta:
                    beta = score

        return AlphaBetaMax(self.board, self.__alpha, self.__beta, self.depth)

def possible_states(state: np.ndarray, current_player: int):
    possible_moves = find_possible_player_moves(state, current_player)
    for move_vector in possible_moves:
        partial_state = move_player(state, current_player, move_vector)
        possible_removals = find_possible_removals(partial_state)
        for remove_pos in possible_removals:
            yield remove_square(partial_state, remove_pos)

def find_possible_player_moves(state: np.ndarray, current_player: int) -> list:
        pos_x, pos_y = np.where(state == current_player)
        pos_x = pos_x[0]
        pos_y = pos_y[0]
        player_neighbourhood = state[pos_x - 1: pos_x + 2, pos_y - 1: pos_y + 2]
        x_positions = (np.where(player_neighbourhood == 1)[0] + pos_x - 1)
        y_positions = (np.where(player_neighbourhood == 1)[1] + pos_y - 1)
        return np.array((x_positions, y_positions)).T.tolist()

def find_possible_removals(state: np.ndarray) -> list:
    return np.array(np.where(state == 1)).T.tolist()
    
def move_player(state: np.ndarray, current_player: int, move_vector: tuple) -> np.ndarray:
    result = state.copy()
    result[move_vector[0], move_vector[1]] = current_player
    result[move_vector[0], move_vector[1]] = 1
    return result

def remove_square(state: np.ndarray, square_pos: tuple) -> np.ndarray:
    result = state.copy()
    result[square_pos[0], square_pos[1]] = 0
    return result