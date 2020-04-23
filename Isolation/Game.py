import numpy as np
import os
import platform
from Board import Board
from Player import HumanPlayer, RandomPlayer, SemiRandomPlayer

def clear():
    current_platform = platform.system()
    if current_platform == 'Darwin':
        os.system('clear')
    elif current_platform == 'Windows':
        os.system('cls')
    elif current_platform == 'Linux':
        os.system('clear')

def new_game(board):

    board.init_players_pos();
    while (board.is_active_player_lost()==False):
        board = board.active_player.fetch_action(board)
        #clear()
        board.print_board()
        board.switch_turn()
    
    print("Przegral - " +board.active_player.name)

    return board.active_player.is_white

