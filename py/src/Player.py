class Player:
    class Type:
        @staticmethod
        def Null(): return 0
        @staticmethod
        def White(): return 1
        @staticmethod
        def Black(): return 2

        @staticmethod
        def opposite_type(player_type):
            if player_type == Type.White(): return Type.Black()
            elif player_type == Type.Black(): return Type.White()
            else: return Type.Null()

    def __init__(self, player_type):
        self._type = player_type

    def type(self):
        return self._type