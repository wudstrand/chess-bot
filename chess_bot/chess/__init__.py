from chess_bot.chess.board import starter_board
from chess_bot.chess.enum.color import Color
from chess_bot.chess.piece import Piece


class Chess:
    def __init__(self):
        self._board = starter_board()
        self._turn = 1
        self._color_in_control = Color.WHITE

    def generate_legal_moves(self, piece: Piece):
        pass
