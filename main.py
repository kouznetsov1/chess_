from board import Board
from graphics import start_graphics

def main():
    board = set_up_board()
    start_graphics()


def set_up_board():
    return Board()

main()
