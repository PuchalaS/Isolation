import numpy as np
from Isolation.Board import Board


class AlphaBeta(object):
    def __init__(self, board: Board, depth: int):
        self.board = board
        self.depth = depth
        self.__alpha = (-1) * np.inf
        self.__beta = np.inf
        self.evaluate = lambda: 1

    def predict_state(self):
        def AlphaBetaMax(state, alpha, beta, depth_left):
            if depth_left == 0:
                return (state, self.evaluate())

            for possible_state in self.board.legal_moves:
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

            for possible_state in self.board.legal_moves:
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
