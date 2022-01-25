from Board import Board
from Player import Player
from Piece import Piece

class Chess:
    def __init__(self):
        self._board = Board()

        self._move_number = 0

    def setup(self):
        self._white = Player(Player.Type.White())
        self._black = Player(Player.Type.Black())

        # White's pieces are on ranks 1 and 2 (y=0 and y=1)

        for p, player in enumerate([self._white, self._black]):
            for i in range(8):
                # Pawns first
                self._board.add_piece(Piece(Piece.Type.Pawn(), Coord(i, 1 + p*5), player))

            # Minors
            for i in range(2):
                # Rooks
                self._board.add_piece(Piece(Piece.Type.Rook(), Coord(i*7, p*7), player))

                # Knights
                self._board.add_piece(Piece(Piece.Type.Knight(), Coord(1 + i*5, p*7), player))

                # Bishops
                self._board.add_piece(Piece(Piece.Type.Bishop(), Coord(2 + i*3, p*7), player))

            # Queen
            # We assume square 0, 0 is black
            self._board.add_piece(Piece(Piece.Type.Queen(), Coord(3, p*7), player))

            # King
            self._board.add_piece(Piece(Piece.Type.King(), Coord(4, p*7), player))

    def turn(self):
        if self._move_number % 2 == 0:
            # White's turn
            # TODO
            pass
        else:
            # Black's turn
            # TODO
            pass

        self._move_number += 1