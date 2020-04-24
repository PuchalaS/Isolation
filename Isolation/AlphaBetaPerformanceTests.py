from Player import Agent, RandomPlayer, SemiRandomPlayer
from AlphaBeta import AlphaBeta, MeasureOneToTwoFactory, MeasureOneStepFurtherFactory
from Board import Board
from Game import new_game
import os
import numpy as np
import time


def measure_name(state_eval_factory):
    name = state_eval_factory.__name__
    if name == 'MeasureOneToTwoFactory':
        return 'Simple'
    elif name == 'MeasureOneStepFurtherFactory':
        return 'Complex'
    else:
        return name

class MinMaxPlayer(Agent):
    def __init__(self, name, is_white, start_x, start_y, depth, state_eval_factory, log_file, n_game):
        super().__init__(name, is_white, start_x, start_y)
        self.depth = depth
        self.state_eval_factory = state_eval_factory
        self.play_as = 2 if is_white else 3
        self.play_against = 3 if is_white else 2
        self.log_file = log_file
        self.n_game = n_game


    def fetch_action(self, board):
        minmax = AlphaBeta(board.board_status,
                           self.depth,
                           self.play_as,
                           self.play_against,
                           self.state_eval_factory)
        started = time.time()
        move, remove = minmax.predict_state()
        duration = time.time() - started
        log_string = "MinMax,{0},{1},{2},{3},{4}\n".format(started, duration, self.depth, measure_name(self.state_eval_factory), self.n_game)
        with open(self.log_file, mode='a+') as fs:
            fs.write(log_string)

        print(move)
        print(remove)
        board.make_move(move)
        board.make_remove(remove)
        return board


def minmax_vs_radom(cycles, min_max_depth, state_eval_factory, log_file):
    results = []
    for x in range(cycles):
        white = MinMaxPlayer("Biały", True, 6, 3,
                             min_max_depth, state_eval_factory, log_file, x)
        black = RandomPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    print("Bialy wygral: " + str(white_wins)+"%")
    print("Czarny wygral: " + str(black_wins)+"%")


def minmax_vs_semi_radom(cycles, min_max_depth, state_eval_factory, log_file, game_log):
    results = []
    for x in range(cycles):
        white = MinMaxPlayer("Biały", True, 6, 3,
                             min_max_depth, state_eval_factory, log_file, x)
        black = SemiRandomPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    with open(game_log, 'w+') as fs:
        fs.writelines(f'black_wins,{black_wins},white_wins,{white_wins}')
    print("Bialy wygral: " + str(white_wins)+"%")
    print("Czarny wygral: " + str(black_wins)+"%")


def minmax_vs_minmax(cycles, first_min_max_depth, first_state_eval_factory, first_log_file, second_min_max_depth, second_state_eval_factory, second_log_file, game_log):
    results = []
    for x in range(cycles):
        white = MinMaxPlayer("Biały", True, 6, 3,
                             first_min_max_depth, first_state_eval_factory, first_log_file, x)
        black = MinMaxPlayer("Czarny", False, 0, 3,
                             second_min_max_depth, second_state_eval_factory, second_log_file, x)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    with open(game_log, 'w+') as fs:
        fs.writelines(f'black_wins,{black_wins},white_wins,{white_wins}')
    print("Bialy wygral: " + str(white_wins)+"%")
    print("Czarny wygral: " + str(black_wins)+"%")

#minmax_vs_semi_radom(50, 2, MeasureOneStepFurtherFactory, 'MinMax_vs_SemiRandom_50_2_Complex', 'MinMax_vs_SemiRandom_50_2_Complex_GameResult.csv')
#minmax_vs_semi_radom(50, 3, MeasureOneToTwoFactory, 'MinMax_vs_SemiRandom_50_3_Simple.csv', 'MinMax_vs_SemiRandom_50_3_Simple_GameResult.csv')
#minmax_vs_semi_radom(50, 3, MeasureOneStepFurtherFactory, 'MinMax_vs_SemiRandom_50_3_Complex', 'MinMax_vs_SemiRandom_50_3_Complex_GameResult.csv')


#minmax_vs_minmax(30, 3, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_White_30_3_Simple', 3, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_Black_30_3_Simple', 'MinMax_vs_MinMax_30_3_Simple_3_Simple_GameResult.csv')
#minmax_vs_minmax(30, 3, MeasureOneStepFurtherFactory, 'MinMax_vs_MinMax_White_30_3_Complex', 3, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_Black_30_3_Simple','MinMax_vs_MinMax_30_3_Complex_3_Simple_GameResult.csv')
#minmax_vs_minmax(30, 3, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_White_30_3_Simple', 4, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_Black_30_4_Simple', 'MinMax_vs_MinMax_30_3_Simple_4_Simple_GameResult.csv')
#minmax_vs_minmax(30, 3, MeasureOneStepFurtherFactory, 'MinMax_vs_MinMax_White_30_3_Simple', 4, MeasureOneStepFurtherFactory, 'MinMax_vs_MinMax_Black_30_4_Simple', 'MinMax_vs_MinMax_White_30_3_Simple_4_Complex_GameResult.csv')
