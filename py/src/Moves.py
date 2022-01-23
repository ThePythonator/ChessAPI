from Player import Player
from Coord import Coord

class Moves:
    @staticmethod
    def filter_moves(piece, board, moves):
        # Remove moves which move into check
        filtered_moves = []
        for move in moves:
            temp = board.copy()
            temp.move(piece.position, move)

            if not Moves.in_check(board, Player.Type.opposite_type(piece.player().type())):
                filtered_moves.append(move)
        
        return filtered_moves
    
    @staticmethod
    def in_check(board, player_type):
        for piece in board.get_pieces(player_type):
            if piece.type() == Piece.Type.king():
                # Is this king in check?

                for p in board.get_pieces(Player.Type.opposite_type(player_type)):
                    if piece.position in p.moves(grid, False):
                        return False

        return True

    @staticmethod
    def Pawn(piece, board, filter_checks):
        # If filter is True, moves which move into check, or remain in check are removed.
        moves = []
        if not board.on_board(piece.position + piece.player().direction_coord()):
            return moves

        for offset in [Coord(1, 0), Coord(-1, 0)]:
            move = piece.position + offset + piece.player().direction_coord()
            
            if not board.on_board(piece.position + piece.player().direction_coord()):
                continue

            if not board.empty_at(move):
                if board.at(move).player().type() == Player.Type.opposite_type(piece.player().type()):
                    # Pieces are on opposite teams
                    moves.append(move)

        move = piece.position + piece.player().direction_coord()
        if board.empty_at(move):
            moves.append(move)

        return Moves.filter_moves(piece, board, moves) if filter_checks else moves

    @staticmethod
    def Bishop(piece, board, filter_checks):
        return Moves._straight_line_moves(piece, board, filter_checks, [Coord(1, 1), Coord(1, -1), Coord(-1, -1), Coord(-1, 1)])

    @staticmethod
    def Rook(piece, board, filter_checks):
        return Moves._straight_line_moves(piece, board, filter_checks, [Coord(1, 0), Coord(0, 1), Coord(0, -1), Coord(-1, 0)])

    @staticmethod
    def Knight(piece, board, filter_checks):
        moves = []

        for offset in [Coord(2, 1), Coord(-2, 1), Coord(-2, -1), Coord(2, -1)]:
            move = piece.position + offset + piece.player().direction_coord()
            
            if not board.on_board(piece.position + piece.player().direction_coord()):
                continue

            if board.empty_at(move) or board.at(move).player().type() == Player.Type.opposite_type(piece.player().type()):
                # Pieces are on opposite teams, or space is empty
                moves.append(move)

        return Moves.filter_moves(piece, board, moves) if filter_checks else moves

    @staticmethod
    def Queen(piece, board, filter_checks):
        return Moves.bishop(piece, board, filter_checks) + Moves.rook(piece, board, filter_checks)

    @staticmethod
    def King(piece, board, filter_checks):
        moves = []

        for offset in [Coord(1, 0), Coord(1, 1), Coord(0, 1), Coord(-1, 1), Coord(-1, 0), Coord(-1, -1), Coord(0, -1), Coord(1, -1)]:
            move = piece.position + offset + piece.player().direction_coord()
            
            if not board.on_board(piece.position + piece.player().direction_coord()):
                continue

            if board.empty_at(move) or board.at(move).player().type() == Player.Type.opposite_type(piece.player().type()):
                # Pieces are on opposite teams, or space is empty
                moves.append(move)

        # Check if we can castle
        if not Moves.in_check(board, piece.player().type()) and piece.move_count() == 0:
            for p in board.get_pieces(piece.player().type()):
                if p.type() == Piece.Type.Rook() and p.move_count() == 0 and p.position.y == piece.position.y:
                    # TODO: Check that king doesn't pass _through_ check
                    # TODO: Check that there are no pieces between the king and the rook
                    # TODO: Current issue with move system is that the board class (when moving the king), needs to work out if the move is a castle, and if so, move the correct rook too
                    pass # Currently don't support castling

        return Moves.filter_moves(piece, board, moves) if filter_checks else moves

    @staticmethod
    def Null(piece, board, filter_checks):
        return []

    @staticmethod
    def MoveTable():
        return [Moves.Null, Moves.Pawn, Moves.Knight, Moves.Bishop, Moves.Rook, Moves.Queen, Moves.King]

    @staticmethod
    def _straight_line_moves(piece, board, filter_checks, directions):
        moves = []

        for direction in directions:
            temp = piece.position
            end = False

            while not end:
                temp += direction
            
                if not board.on_board(piece.position + piece.player().direction_coord()):
                    end = True

                elif board.empty_at(temp):
                    moves.append(move)

                elif board.at(move).player().type() == Player.Type.opposite_type(piece.player().type()):
                    moves.append(move)
                    end = True

                elif board.at(move).player().type() == piece.player().type():
                    end = True

        return Moves.filter_moves(piece, board, moves) if filter_checks else moves