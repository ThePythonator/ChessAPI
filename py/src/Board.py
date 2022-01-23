from Coord import Coord

class Board:
    def __init__(self, width = 8, height = 8):
        self._board = [[None] * width] * height
        self._size = Coord(width, height)

    def at(self, coord):
        return self._board[coord.y][coord.x]
    
    def empty_at(self, coord):
        return self.at(coord) is None
    
    def get_pieces(self, piece_type = None):
        if piece_type is None: return [piece for row in self._board for piece in row if piece is not None]
        else: return [piece for piece in self.get_pieces() if piece.player().type() == piece_type]

    def on_board(self, position):
        return not (position.x < 0 or position.y < 0 or position.x >= self._size.x or position.y >= self._size.y)

    def copy(self):
        board = Board(self._size.x, self._size.y)

        for piece in self.get_pieces():
            board.add_piece(piece.copy())

        return board

    def add_piece(self, piece):
        self.set(piece.position, piece)

    def move(self, start, end):
        if self.empty_at(start): return False
        
        piece = self.at(start)
        piece.add_move(end)

        # Anything I've missed?
        # TODO: calculate if castling, and if so, find the corresponding rook and move it too
        self.set(start, None)
        self.set(end, piece)
        return True

    def set(self, coord, piece):
        self._board[coord.y][coord.x] = piece