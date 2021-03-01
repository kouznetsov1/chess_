from piece import Piece

class Board:
    board_size = 8
    board = dict()

    def __init__(self):
        self.board = self.set_up_board()
        self.print_board()

    # sets up a new board
    # uses starting_piece() and set_start_color() to put correct pieces
    def set_up_board(self):
        ascii_nr = 97
        board = {}
        for j in range(self.board_size):
            for i in range(self.board_size):
                pos_number = i+1
                pos_char = chr(ascii_nr)

                pos_name = str(pos_char + str(pos_number))

                piece = self.starting_piece(pos_char, pos_number)

                board[pos_name] = piece

            ascii_nr += 1

        print("Algebraic notation set for new board.")
        return board

    # function used when generating a new board, decides what piece to put on pos
    def starting_piece(self, char, pos):
        color = ""

        if (pos < 3 or pos > 6):
            color = self.set_start_color(pos)
            if pos in (2, 7):
                return Piece("P", color)
            if char in ("a", "h"):
                return Piece("R", color)
            if char in ("b", "g"):
                return Piece("N", color)
            if char in ("c", "f"):
                return Piece("B", color)
            if char in ("d"):
                return Piece("K", color)
            else:
                return Piece("Q", color)
        else:
            return Piece("E")

    # function used when generating a new board, decides what color to set on pos
    def set_start_color(self, pos):
        if pos < 3:
            return "W"
        return "B"

    # visual representation
    def print_board(self):
        pos_number = self.board_size
        board_list = []

        for j in range(self.board_size):
            ascii_nr = 97
            row_list = []
            for i in range(self.board_size):
                pos_char = chr(ascii_nr)
                pos_name = str(pos_char + str(pos_number))

                row_list.append(pos_name)
                ascii_nr += 1
            board_list.append(row_list)
            pos_number -= 1

        for row in board_list:
            for position in row:
                print(self.board[position].piece_type.value + "(" +
                      self.board[position].color.value + ")", " ", end="")
            print("\n", end="")

