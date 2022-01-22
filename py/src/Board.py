class Board:
    def __init__(self, width = 8, height = 8):
        self._board = [[None] * width] * height

    def at(self, coord):
        return self._board[coord.y][coord.x]
    
    def empty_at(self, coord):
        return self.at(coord) is None
    
    def get_pieces(self, piece_type = None):
        if piece_type is None: return [piece for row in self._board for piece in row if piece is not None]
        else: return [piece for piece in self.get_pieces() if piece.player().type() == piece_type]

    def on_board(self, position):
        return not (position.x < 0 or position.y < 0 or position.x >= self._size.x or position.y >= self._size.y)