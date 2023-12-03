import unittest

from chess_bot.chess.board import Board, blank_board, starter_board
from chess_bot.chess.constant import Constants
from chess_bot.chess.enum.piece_type import PieceType


class BoardTest(unittest.TestCase):
    def test_get_pieces_all_pawns(self):
        self._test_board_homogenous_pieces(PieceType.PAWN)

    def test_get_pieces_all_knights(self):
        self._test_board_homogenous_pieces(PieceType.KNIGHT)

    def test_get_pieces_all_bishop(self):
        self._test_board_homogenous_pieces(PieceType.BISHOP)

    def test_get_pieces_all_rook(self):
        self._test_board_homogenous_pieces(PieceType.ROOK)

    def test_get_pieces_all_queen(self):
        self._test_board_homogenous_pieces(PieceType.QUEEN)

    def test_get_pieces_all_king(self):
        self._test_board_homogenous_pieces(PieceType.KING)

    def test_blank_board(self):
        board = blank_board()
        result = board.get_pieces()
        self.assertEqual(len(result), 0)

    def test_starter_board(self):
        board = starter_board()
        result = board.get_pieces()
        self.assertEqual(len(result), 32)

    def _test_board_homogenous_pieces(self, piece_type: PieceType):
        board = self._generate_board_of_one_piece(marker=piece_type.value.marker)
        result = board.get_pieces()
        self.assertEqual(len(result), 64)
        for piece in result:
            self.assertEqual(piece.piece_type, piece_type)

    @staticmethod
    def _generate_board_of_one_piece(marker: int) -> Board:
        raw_board = [
            [marker for _ in range(Constants.number_of_files.value)]
            for _ in range(Constants.number_of_ranks.value)
        ]
        return Board(raw_board=raw_board)

