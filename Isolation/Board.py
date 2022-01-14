import numpy as np
import os
import platform
import random

#from Player import Player
# clear = lambda: os.system('cls') #on Windows System


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


class Board():

    """Klasa implementująca plansze do gry."""

    """Pola planszy"""
    PLAYER_WHITE = 2
    PLAYER_BLACK = 3
    FREE_SQUARE = 1
    NO_SQUARE = 0

    def __init__(self, white_player, black_player, width=7, height=7):
        """
        Parameters
        ----------
        width : int, optional
            Szerokość planszy do gry (domyslnie 7)
        height : int, optional
            Wysokość planszy do gry (domyslnie 7)
        white_player : object

        black_player : object

        """

        self.width = width
        self.height = height
        # aktywny gracz (na posunieciu)
        self.active_player = white_player
        # nieaktywny gracz
        self.inactive_player = black_player
        # np array: zawiera informacje o stanie planszy
        self.board_status = np.ones((width, height))
        # tablica zawierajaca informacje o stanie planszy
        self.move_nuber = 0
        # lista legalnych posuniec aktywnego gracza
        self.legal_moves = []
        # lista legalnych posuniec nieaktywnego gracza
        self.legal_moves_inactive = []
        # lista legalnych usuniec pola aktywnego gracza
        self.legal_removes = []

    def init_players_pos(self):
        """Inicjalizacja poczatkowego ustawienia figur graczy"""
        self.board_status[self.active_player.start_x,
                          self.active_player.start_y] = Board.PLAYER_WHITE
        self.board_status[self.inactive_player.start_x,
                          self.inactive_player.start_y] = Board.PLAYER_BLACK

    def switch_turn(self):
        """Zmiana kolejki. Zamienia aktywnego gracza z nieaktywnym"""
        tmp_player = self.active_player
        self.active_player = self.inactive_player
        self.inactive_player = tmp_player

    def get_active_player_pos(self):
        """Zwraca pozycję aktywnego gracza.

        Returns
        -------
        (int,int)
            Współrzedne gracza
        """
        return (self.active_player.pos_x, self.active_player.pos_y)

    def get_inactive_player_pos(self):
        """Zwraca pozycję nieaktywego gracza.

        Returns
        -------
        (int,int)
            Współrzedne nieaktywanego gracza
        """
        return (self.inactive_player.pos_x, self.inactive_player.pos_y)

    def is_move_legal(self, move):
        """Sprawdza poprawność wprowadzonego ruchu.

        Parameters
        ----------
        move : (int, int)
            Współrzędne sprawdzanego ruchu.

        Returns
        -------
        bool
            Czy współrzędne znajdują się w zakresie planszy i czy wybrane pole jest równe 1
        """
        return (0 <= move[0] < self.height and 0 <= move[1] < self.width and
                self.board_status[move[0], move[1]] == Board.FREE_SQUARE)

    def set_legal_moves(self):
        """Wpisuje legalne ruchy aktywnego gracza do legal_moves."""
        player_pos = self.get_active_player_pos()
        self.legal_moves = []
        # góra
        if self.is_move_legal((player_pos[0], player_pos[1]+1)):
            self.legal_moves.append((player_pos[0], player_pos[1]+1))
        # dół
        if self.is_move_legal((player_pos[0], player_pos[1]-1)):
            self.legal_moves.append((player_pos[0], player_pos[1]-1))
        # prawo
        if self.is_move_legal((player_pos[0]+1, player_pos[1])):
            self.legal_moves.append((player_pos[0]+1, player_pos[1]))
        # lewo
        if self.is_move_legal((player_pos[0]-1, player_pos[1])):
            self.legal_moves.append((player_pos[0]-1, player_pos[1]))
        # lewe-górne
        if self.is_move_legal((player_pos[0]-1, player_pos[1]+1)):
            self.legal_moves.append((player_pos[0]-1, player_pos[1]+1))
        # prawe-górne
        if self.is_move_legal((player_pos[0]+1, player_pos[1]+1)):
            self.legal_moves.append((player_pos[0]+1, player_pos[1]+1))
        # lewe-dolne
        if self.is_move_legal((player_pos[0]-1, player_pos[1]-1)):
            self.legal_moves.append((player_pos[0]-1, player_pos[1]-1))
        # prawe-dolne
        if self.is_move_legal((player_pos[0]+1, player_pos[1]-1)):
            self.legal_moves.append((player_pos[0]+1, player_pos[1]-1))

    def set_legal_moves_inactive(self):
        """Wpisuje legalne ruchy nieaktywnego gracza do legal_moves_inactive."""
        player_pos = self.get_inactive_player_pos()
        self.legal_moves_inactive = []
        # góra
        if self.is_move_legal((player_pos[0], player_pos[1]+1)):
            self.legal_moves_inactive.append((player_pos[0], player_pos[1]+1))
        # dół
        if self.is_move_legal((player_pos[0], player_pos[1]-1)):
            self.legal_moves_inactive.append((player_pos[0], player_pos[1]-1))
        # prawo
        if self.is_move_legal((player_pos[0]+1, player_pos[1])):
            self.legal_moves_inactive.append((player_pos[0]+1, player_pos[1]))
        # lewo
        if self.is_move_legal((player_pos[0]-1, player_pos[1])):
            self.legal_moves_inactive.append((player_pos[0]-1, player_pos[1]))
        # lewe-górne
        if self.is_move_legal((player_pos[0]-1, player_pos[1]+1)):
            self.legal_moves_inactive.append(
                (player_pos[0]-1, player_pos[1]+1))
        # prawe-górne
        if self.is_move_legal((player_pos[0]+1, player_pos[1]+1)):
            self.legal_moves_inactive.append(
                (player_pos[0]+1, player_pos[1]+1))
        # lewe-dolne
        if self.is_move_legal((player_pos[0]-1, player_pos[1]-1)):
            self.legal_moves_inactive.append(
                (player_pos[0]-1, player_pos[1]-1))
        # prawe-dolne
        if self.is_move_legal((player_pos[0]+1, player_pos[1]-1)):
            self.legal_moves_inactive.append(
                (player_pos[0]+1, player_pos[1]-1))

    def set_legal_removes(self):
        """Wpisuje legalne usuniecia do legal_removes."""
        self.legal_removes = []
        result = np.where(self.board_status == 1)
        self.legal_removes = list(zip(result[0], result[1]))

    def make_move(self, move):
        """Wykonuje ruch na planszy. Update board_status, pozycji aktywnego gracza oraz ilości wykonanych ruchów

        Parameters
        ----------
        move : (int, int)
            Współrzędne wykonywanego ruchu.

        Returns
        -------
        bool
            Czy udało sie wykonać ruch
        """
        self.set_legal_moves()
        current_position = self.get_active_player_pos()
        if (move in self.legal_moves):
            if self.move_nuber in [0, 1]:  # dla pierwszego ruchu bialego i czarnego chcemy
                # usunać pole na którym wczesniej stała figura
                self.board_status[current_position[0]
                                  ][current_position[1]] = Board.NO_SQUARE
            else:
                self.board_status[current_position[0],
                                  current_position[1]] = Board.FREE_SQUARE
            if(self.active_player.is_white):
                self.board_status[move[0], move[1]] = Board.PLAYER_WHITE
            else:
                self.board_status[move[0], move[1]] = Board.PLAYER_BLACK
            self.active_player.pos_x = move[0]
            self.active_player.pos_y = move[1]
            self.move_nuber = self.move_nuber + 1

        return (move in self.legal_moves)



    def make_remove(self, move):
        """Usuwa pole z planszy. Update board_status.

        Parameters
        ----------
        move : (int, int)
            Współrzędne usuwanego pola.
        """
        self.set_legal_removes()
        if (move in self.legal_removes):
            self.board_status[move[0], move[1]] = Board.NO_SQUARE

        return (move in self.legal_removes)

    def is_active_player_lost(self):
        """Sprawdza czy aktywny gracz moze wykonać jakiś ruch

        Returns
        -------
        bool
            true jeżeli przegał
        """

        self.set_legal_moves()

        #print ("Możliwe posuniecia: " + str(self.legal_moves))
        return (not self.legal_moves)

    def randomize(self):
        """Funkcja pomocnicza do testow. Wylosowywuje stan planszy """
        self.board_status = np.random.randint(
            2, size=(self.width, self.height))
        for _ in range(random.randint(1, 6)):
            self.switch_turn()
        self.active_player.pos_x = random.randint(0, self.width-1)
        self.active_player.pos_y = random.randint(0, self.height-1)
        self.inactive_player.pos_x = random.randint(0, self.width-1)
        self.inactive_player.pos_y = random.randint(0, self.height-1)
        if (self.active_player.is_white):
            self.board_status[self.active_player.pos_x][self.active_player.pos_y] = 2
            self.board_status[self.inactive_player.pos_x][self.inactive_player.pos_y] = 3
        else:
            self.board_status[self.active_player.pos_x][self.active_player.pos_y] = 3
            self.board_status[self.inactive_player.pos_x][self.inactive_player.pos_y] = 2

        print("Aktywny gracz: " + self.active_player.name)
        self.print_board()

        
        
    def print_board(self):
        """Konwersja board_status na tablice ze znakami.
        0 = "X" usuniete z gry pole
        1 = " " wolne pole
        2 = "B" figura gracza białego
        3 = "C" figura gracza czarnego

        Dodane rowniez elemety interfejsu planszy
        """
        charar = np.chararray((7, 7))
        charar = np.where(self.board_status == 1, "   ",self.board_status)
        charar = np.where(self.board_status == 0, " X ",charar)
        charar = np.where(self.board_status == 2, " B ",charar)
        charar = np.where(self.board_status == 3, " C ",charar)
        row_str = ""
        col = ""
        for row in range(self.height):
            print(" |---------------------------|")
            row_str = ""
            for col in range(self.width):
                row_str = row_str + charar[row][col] + "|"
            print (str(row) + "|" + row_str)
        print(" |---------------------------|")
        print("   0   1   2   3   4   5   6   ")
       