from enum import Enum

"""
Type of piece + B/W (?) -> (how many allowed f,b,d,l,r) + jump over
"""

class Piece:
    def __init__(self, piece_type, color=None):
        self.piece_type = self.set_piece(piece_type)
        if (color):
            self.color = color
        else:
            color = "E"

    def set_piece(self, piece_type):
        if piece_type == "P":
            return self.Pawn()
        if piece_type == "R":
            return self.Rook()
        if piece_type == "N":
            return self.Knight()
        if piece_type == "B":
            return self.Bishop()
        if piece_type == "K":
            return self.King()
        if piece_type == "Q":
            return self.Queen()

    def print_piece(self):
        name = type(self.piece_type).__name__
        first_char = name[0]

        # if knight
        if first_char == "K":
            if name[1] == "n":
                first_char = "N"

        return first_char

    class Pawn:
        def __init__(self):
            print("Pawn!")

    class Rook:
        def __init__(self):
            print("Rook!")

    class Bishop:
        def __init__(self):
            print("Bishop!")

    class Knight:
        def __init__(self):
            print("Knight!")

    class Queen:
        def __init__(self):
            print("Queen!")

    class King:
        def __init__(self):
            print("King!")
