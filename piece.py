from enum import Enum

"""
Type of piece + B/W (?) -> (how many allowed f,b,d,l,r) + jump over
"""

class Piece:
    def __init__(self, piece_type, color=None):
        self.piece_type = Piece_Type(piece_type)
        if (color):
            self.color = Piece_Color(color)
        else:
            self.color = Piece_Color("E")

class Piece_Type(Enum):
    K = "K" # king
    Q = "Q" # queen
    R = "R" # rook
    B = "B" # bishop
    N = "N" # knight
    P = "P" # pawn
    E = "E" # empty

class Piece_Color(Enum):
    WHITE = "W"
    BLACK = "B"
    EMPTY = "E"