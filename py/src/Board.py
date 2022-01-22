class Board:
    def on_board(self, position):
        return not (position.x < 0 or position.y < 0 or position.x >= self._size.x or position.y >= self._size.y)