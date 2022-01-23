from Moves import Moves

class Piece:
    class Type:
        @staticmethod
        def Null(): return 0
        @staticmethod
        def Pawn(): return 1
        @staticmethod
        def Knight(): return 2
        @staticmethod
        def Bishop(): return 3
        @staticmethod
        def Rook(): return 4
        @staticmethod
        def Queen(): return 5
        @staticmethod
        def King(): return 6

    def __init__(self, piece_type):
        self._type = piece_type
        self._moves = []

    def player(self):
        return self._player

    def type(self):
        return self._type

    def moves(self, grid, filter_checks):
        return Moves.MoveTable()[self.type()](self, grid, filter_checks)

    def move_count(self):
        return len(moves)

    def copy(self):
        piece = Piece(self._type)
        piece._moves = self._moves.copy()
        return piece