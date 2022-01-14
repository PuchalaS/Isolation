import numpy as np
import os
import platform
import random
from AlphaBeta import AlphaBeta, MeasureOneToTwoFactory
def clear():
    current_platform = platform.system()
    if (
        current_platform == 'Darwin'
        or current_platform != 'Windows'
        and current_platform == 'Linux'
    ):
        os.system('clear')
    elif current_platform == 'Windows':
        os.system('cls')

class Agent():

    """Klasa agenta - rodzica dla wszystkich graczy"""

    def __init__(self, name, is_white, start_x, start_y):
        """
    Parameters
    ----------
    name : string
        Nazwa gracza (istote przy drukowaniu statusu)
    is_white : int
        Czy gracz jest graczem bialym
    start_x : int
        Wpolrzedna x startowej pozycji
    start_y : int
        Wpolrzedna y startowej pozycji
    """
        self.start_x = start_x
        self.start_y = start_y
        self.pos_x = start_x
        self.pos_y = start_y
        self.name = name
        self.is_white = is_white

    def fetch_action(self):
        """Funkcja zmieniajaca obiekt board zgodnie z wybranym ruchem"""
    def return_position(self):
        """Zwraca pozycję  gracza.

        Returns
        -------
        (int,int)
            Współrzedne gracza
        """
        return (self.pos_x, self.pos_y)


class HumanPlayer(Agent):

    """Klasa implementujaca gracza sterowanego przez czlowieka"""

    def __init__(self, name, is_white, start_x, start_y):
        """Jak w klasie Agent"""
        super().__init__(name, is_white, start_x, start_y)

    def fetch_action(self, board):
        """Funkcja zmieniajaca obiekt board zgodnie z wybranym ruchem. Zawiera rowniez obsluge inputu gracza"""
        valid_choice = False
        clear()
        print ("Na posunieciu gracz: "+ board.active_player.name)
        board.print_board()
        while not valid_choice:
            try:
                key_input = input("Podaj ruch: ")
                move = tuple(int(x) for x in key_input.split(","))

                while (not board.make_move(move)):
                    print("Nielegalny ruch!")
                    try:
                        key_input = input("Podaj poprawny ruch: ")
                        move = tuple(int(x) for x in key_input.split(","))
                    except ValueError:
                        continue
            except ValueError:
                print('Niepoprawne znaki!')
                continue
            valid_choice = True
            if key_input == "q":
                    break
        clear()
        board.print_board()
        valid_choice = False
        while not valid_choice:
            try:
                key_input = input("Podaj usuniecie: ")
                move = tuple(int(x) for x in key_input.split(","))

                while (not board.make_remove(move)):
                    print("Nielegalne usuniecie!")
                    try:
                        key_input = input("Podaj poprawne usuniecie: ")
                        move = tuple(int(x) for x in key_input.split(","))
                        if key_input == "q":
                            break
                    except ValueError:
                        continue
            except ValueError:
                print('Niepoprawne znaki!')
                continue
            valid_choice = True
        clear()
        board.print_board()
        return board


class RandomPlayer(Agent):

    """Klasa implementujaca zupelnie losowego gracza"""

    def __init__(self, name, is_white, start_x, start_y):
        """Jak w klasie Agent"""
        super().__init__(name, is_white, start_x, start_y)

    def make_random_move(self,board):
        """Obliczenie i wykonanie losowego ruchu"""
        board.set_legal_moves()
        random_move = random.choice(board.legal_moves)
        board.make_move(random_move)

    def make_random_remove(self,board):
        """Obliczenie i wykonanie losowego usuniecia"""
        board.set_legal_removes()
        random_remove = random.choice(board.legal_removes)
        board.make_remove(random_remove)

    def fetch_action(self, board):
        """Funkcja zmieniajaca obiekt board zgodnie z wybranym ruchem"""
        self.make_random_move(board)
        self.make_random_remove(board)
        return board
   
class SemiRandomPlayer(Agent):

    """Klasa implementujaca gracza poslugujacego sie prosta logika. 
    Porusza sie w strone srodka planszy oraz usuwa losowe pole z sasiedztwa gracza przeciwnego"""

    def __init__(self, name, is_white, start_x, start_y):
        """Jak w klasie Agent"""
        super().__init__(name, is_white, start_x, start_y)

    def make_move_to_center(self,board):
        """Obliczenie i wykonanie ruchu w strone srodka """
        board.set_legal_moves()
        
        legal_moves_ndarray = np.asarray(board.legal_moves)
        abs_sum = np.abs(legal_moves_ndarray[:,0]-3) + np.abs(legal_moves_ndarray[:,1]-3)
        result = np.where(abs_sum == np.min(abs_sum))
        move_to_center = tuple(map(tuple,legal_moves_ndarray[result[0],:]))[0]
        board.make_move(move_to_center)

    def make_semi_random_remove(self,board):
        """Obliczenie i usuniecie pola z sasiedztwa gracza przeciwnego """
        board.set_legal_moves_inactive()
        if board.legal_moves_inactive:
            random_remove = random.choice(board.legal_moves_inactive)
            board.make_remove(random_remove)

    def fetch_action(self, board):
        """Funkcja zmieniajaca obiekt board zgodnie z wybranym ruchem"""
        self.make_move_to_center(board)
        self.make_semi_random_remove(board)

        return board

class MinMaxPlayer(Agent):

    """Klasa implementujaca gracza poslugujacego sie algorytmem min-max"""
    def __init__(self, name, is_white, start_x, start_y, depth):
        super().__init__(name, is_white, start_x, start_y)
        self.depth = depth

    def fetch_action(self, board):
        """Funkcja oblicza najlepszy ruch za pomocą algorytmu min-max"""
        if self.is_white:
            minmax = AlphaBeta(board.board_status,self.depth,2,3, MeasureOneToTwoFactory)
        else:
            minmax = AlphaBeta(board.board_status,self.depth,3,2, MeasureOneToTwoFactory)
        print ("AI oblicza ruch...")

        move, remove = minmax.predict_state()
        clear()
        board.make_move(move)
        board.make_remove(remove)
        return board


