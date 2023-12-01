import unittest

from chess_bot.chess.enum.piece_type import PieceType


class PieceTypeTest(unittest.TestCase):
    def test_pawn_creation(self):
        self.assertEqual(PieceType.from_marker(1), PieceType.PAWN)
        self.assertEqual(PieceType.from_marker(-1), PieceType.PAWN)

    def test_knight_creation(self):
        self.assertEqual(PieceType.from_marker(2), PieceType.KNIGHT)
        self.assertEqual(PieceType.from_marker(-2), PieceType.KNIGHT)

    def test_bishop_creation(self):
        self.assertEqual(PieceType.from_marker(3), PieceType.BISHOP)
        self.assertEqual(PieceType.from_marker(-3), PieceType.BISHOP)

    def test_rook_creation(self):
        self.assertEqual(PieceType.from_marker(4), PieceType.ROOK)
        self.assertEqual(PieceType.from_marker(-4), PieceType.ROOK)

    def test_queen_creation(self):
        self.assertEqual(PieceType.from_marker(5), PieceType.QUEEN)
        self.assertEqual(PieceType.from_marker(-5), PieceType.QUEEN)

    def test_king_creation(self):
        self.assertEqual(PieceType.from_marker(6), PieceType.KING)
        self.assertEqual(PieceType.from_marker(-6), PieceType.KING)

