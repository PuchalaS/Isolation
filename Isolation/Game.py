import numpy as np
import os
import platform
from Board import Board
from Player import HumanPlayer, RandomPlayer, SemiRandomPlayer, MinMaxPlayer

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
        clear()
        board.print_board()
        board.switch_turn()
    
    print("Przegral - " +board.active_player.name)
    
    return board.active_player.is_white

def menu():
    clear()
    key_input = ""
    print("||*****************GRA W IZOLACJE*****************||")
    print("||===================== MENU =====================||\n")
    print("(1). Rozpocznij gre przeciwko algorytmowi min-max \n")
    print("(2). Rozpocznij gre przeciwko ludzkiemu graczowi\n")
    print("(3). Zasady\n")
    print("(q). Wyjdz z gry\n")
    print("||================================================||\n")
    key_input = input("Podaj opcje: ")
    while key_input!="q" and key_input!='1' and key_input!='2' and key_input!='3':
        key_input = input("Bledna opcja! Sproboj ponownie: ")
    if key_input == "1":
        min_max_game()
    if key_input == "2":
        human_game()
    if key_input == "3":
        rules()
    if key_input == "q":
        print("Dziekuje za gre! Do widzenia.")

def rules():
    clear()
    print("Gra odbywa sie na plany 7x7. Figura bialego jest wyswietlana jako B, a czarnego jako C.")
    print("Pola usuniete z gry oznaczone sa X. Tura sklada sie z 2 czesci: wykonania ruchu swoja figura oraz usuniecia wolnego pola z planszy")
    print("Ruchy i usuniecia nalezy podawac w postaci: wiersz,kolumna. Np.: 1,3.")
    print("Przegrywa ten gracz ktory nie moze wykonacz posuniecia\n")
    key_input = input("Nacisnij dowolny klawisz, aby wrocic do menu glownego...")
    menu()

def min_max_game():
    clear()
    print("Czy chcesz grac (B)ialym czy (C)zarnym?")
    white_black = input(">")
    while white_black!="B" and white_black!='C':
        white_black = input("Bledna opcja! Sproboj ponownie: ")

    print("Podaj glebokosc przeszukiwania algorytmi min-max. Zalecena: 3")
    while True:
        try:
            key_input = input(">")
            depth = int(key_input)
            if (depth > 4):
                print ("Uwaga: Wybrano glebokosc wieksza niz 4. Algorytm moze dzialac powoli")
            break;
        except ValueError:
            print('Niepoprawne znaki! Sprobuj ponownie')
            continue

    if white_black == "B":
        white = HumanPlayer("Biały", True, 6, 3)
        black = MinMaxPlayer("Czarny", False, 0, 3, depth)
        board = Board(white, black)
        clear()
        print ("Grasz jako bialy. Powodzenia!")
        new_game(board)
        key_input = input("Nacisnij dowolny klawisz, aby wrocic do menu glownego")
        menu()
    if white_black == "C":
        white = MinMaxPlayer("Biały", True, 6, 3, depth)
        black = HumanPlayer("Czarny", False, 0, 3)
        board = Board(white, black)
        clear()
        print ("Grasz jako czarny. Powodzenia!")
        new_game(board)
        key_input = input("Nacisnij dowolny klawisz, aby wrocic do menu glownego")
        menu()

def human_game():
 
    white = HumanPlayer("Biały", True, 6, 3)
    black = HumanPlayer("Czarny", False, 0, 3)
    board = Board(white, black)
    clear()
    new_game(board)
    key_input = input("Nacisnij dowolny klawisz, aby wrocic do menu glownego")
    menu()


