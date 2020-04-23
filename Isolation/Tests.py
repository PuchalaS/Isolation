﻿import numpy as np
from Board import Board
from Player import HumanPlayer, RandomPlayer, SemiRandomPlayer, MinMaxPlayer
from Game import new_game



def random_vs_radom(cycles):
    results= []
    for x in range(cycles):
        white = RandomPlayer("Biały", True, 6, 3)
        black = RandomPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    print ("Bialy wygral: "+ str(white_wins)+"%")
    print ("Czarny wygral: "+ str(black_wins)+"%")

def random_vs_semi_radom(cycles):
    results= []
    for x in range(cycles):
        white = RandomPlayer("Biały", True, 6, 3)
        black = SemiRandomPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    print ("Bialy wygral: "+ str(white_wins)+"%")
    print ("Czarny wygral: "+ str(black_wins)+"%")

def semi_random_vs_semi_radom(cycles):
    results= []
    for x in range(cycles):
        white = SemiRandomPlayer("Biały", True, 6, 3)
        black = SemiRandomPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    print ("Bialy wygral: "+ str(white_wins)+"%")
    print ("Czarny wygral: "+ str(black_wins)+"%")

def minmax_vs_radom(cycles):
    results= []
    for x in range(cycles):
        white = MinMaxPlayer("Biały", True, 6, 3)
        black = RandomPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    print ("Bialy wygral: "+ str(white_wins)+"%")
    print ("Czarny wygral: "+ str(black_wins)+"%")

def minmax_vs_semi_radom(cycles):
    results= []
    for x in range(cycles):
        white = MinMaxPlayer("Biały", True, 6, 3)
        black = SemiRandomPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    print ("Bialy wygral: "+ str(white_wins)+"%")
    print ("Czarny wygral: "+ str(black_wins)+"%")

def minmax_vs_minmax(cycles):
    results= []
    for x in range(cycles):
        white = MinMaxPlayer("Biały", True, 6, 3)
        black = MinMaxPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        results.append(new_game(board))
    black_wins = np.count_nonzero(results)/cycles * 100
    white_wins = 100 - black_wins
    print ("Bialy wygral: "+ str(white_wins)+"%")
    print ("Czarny wygral: "+ str(black_wins)+"%")

minmax_vs_radom(10)
#minmax_vs_semi_radom(10)