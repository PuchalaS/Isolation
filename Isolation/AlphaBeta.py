import numpy as np
from typing import Callable


class AlphaBeta(object):
    def __init__(self,
                 board: np.ndarray,
                 depth: int,
                 player: int,
                 enemy: int,
                 eval_function_factory):
        self.board = board.copy()
        margin = np.zeros((9,9))
        margin[1:-1, 1:-1] = self.board
        self.board = margin 
        self.depth = depth
        self.__alpha = (-1) * np.inf
        self.__beta = np.inf
        self.player = player
        self.enemy = enemy
        self.__inital_player_position = find_player_position(
            self.board, player)
        self.__inital_enemy_position = find_player_position(self.board, enemy)
        self.__player_state_eval_fn = eval_function_factory(self.player, self.enemy)
        self.__enemy_state_eval_fn = eval_function_factory(self.enemy, self.player)

    def update_state(self, state: np.ndarray) -> None:
        self.board = state.copy()
        margin = np.zeros((9,9))
        margin[1:-1, 1:-1] = self.board
        self.board = margin 

    def predict_state(self):
        def AlphaBetaMax(state, alpha, beta, depth_left):
            if depth_left == 0:
                return (state, self.__player_state_eval_fn(state))
            best_state = None
            best_value = -np.inf
            for possible_state in possible_states(state, self.player, self.enemy):
                _, score = AlphaBetaMin(
                    possible_state,
                    alpha,
                    beta,
                    depth_left - 1)

                if score > best_value:
                    best_value = score
                    best_state = possible_state
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return (best_state, best_value)

        def AlphaBetaMin(state, alpha, beta, depth_left):
            if depth_left == 0:
                return (state, (-1) * self.__enemy_state_eval_fn(state))
            best_state = None
            best_value = np.inf
            for possible_state in possible_states(state, self.enemy, self.player):
                _, score = AlphaBetaMax(
                    possible_state,
                    alpha,
                    beta,
                    depth_left - 1)
                if score < best_value:
                    best_value = score
                    best_state = possible_state
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return (best_state, best_value)

        current_state = self.board.copy()
        predicted_state, score = AlphaBetaMax(current_state, self.__alpha, self.__beta, self.depth)
        player_pos = np.array(np.where(predicted_state == self.player)).T[0] - np.array([1,1])
        removal = np.array(np.where((current_state == 0) != (predicted_state == 0))).T[0] - np.array([1,1])
        return ((player_pos[0], player_pos[1]), (removal[0], removal[1]))
        # TODO: Konwersja stanu na poszczególny ruch (nowa pozycja gracza, wsp. usuniętego kwadratu) - odjąć (1,1)



def MeasureOneToTwoFactory(first_player: int, second_player: int):
    def MeasureOneToTwo(state: np.ndarray) -> float:
        first_player_moves = count_possible_states(state, first_player)
        second_player_moves = count_possible_states(state, second_player)
        return first_player_moves - (2 * second_player_moves)
    return MeasureOneToTwo


def count_possible_states(state: np.ndarray, player: int) -> int:
    first_move = player_neighbourhood(state, player).sum() - player
    second_move = (state == 1).sum() - 1
    return first_move * second_move


def possible_states(state: np.ndarray, current_player: int, enemy_player: int):
    possible_moves = find_possible_player_moves(state, current_player)
    for move_vector in possible_moves:
        partial_state = move_player(state, current_player, move_vector)
        possible_removals = find_possible_removals(partial_state, enemy_player)
        for remove_pos in possible_removals:
            yield remove_square(partial_state, remove_pos)


def find_possible_player_moves(state: np.ndarray, current_player: int) -> list:
    pos_x, pos_y = find_player_position(state, current_player)
    player_neighbourhood = state[pos_x - 1: pos_x + 2, pos_y - 1: pos_y + 2]
    x_positions = (np.where(player_neighbourhood == 1)[0] + pos_x - 1)
    y_positions = (np.where(player_neighbourhood == 1)[1] + pos_y - 1)
    return np.array((x_positions, y_positions)).T.tolist()


def find_player_position(state: np.ndarray, player: int) -> tuple:
    pos_x, pos_y = np.where(state == player)
    return pos_x[0], pos_y[0]


def player_neighbourhood(state: np.ndarray, player: int) -> np.ndarray:
    pos_x, pos_y = np.where(state == player)
    pos_x = pos_x[0]
    pos_y = pos_y[0]
    return state[pos_x - 1: pos_x + 2, pos_y - 1: pos_y + 2]


def find_possible_removals(state: np.ndarray, player: int) -> list:
    player_pos = np.array(np.where(state == player)).T[0]
    res = np.array(np.where(state == 1)).T
    diff = res - player_pos
    distance = np.sqrt(np.sum(diff*diff, axis=1))
    asc_order_indexes = np.argsort(distance)
    return res[asc_order_indexes]


def move_player(state: np.ndarray, current_player: int, move_vector: tuple) -> np.ndarray:
    result = state.copy()
    pos_x, pos_y = find_player_position(state, current_player)
    result[move_vector[0], move_vector[1]] = current_player
    result[pos_x, pos_y] = 1
    return result


def remove_square(state: np.ndarray, square_pos: tuple) -> np.ndarray:
    result = state.copy()
    result[square_pos[0], square_pos[1]] = 0
    return result


def print_state(state: np.ndarray):
    print(state[1:-1, 1:-1])
