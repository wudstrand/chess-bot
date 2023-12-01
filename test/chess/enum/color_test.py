import unittest

from chess_bot.chess.enum.color import Color


class ColorTest(unittest.TestCase):
    def test_from_marker_white_pieces(self):
        self.assertEqual(Color.from_marker(1), Color.WHITE)
        self.assertEqual(Color.from_marker(2), Color.WHITE)
        self.assertEqual(Color.from_marker(3), Color.WHITE)
        self.assertEqual(Color.from_marker(4), Color.WHITE)
        self.assertEqual(Color.from_marker(5), Color.WHITE)
        self.assertEqual(Color.from_marker(6), Color.WHITE)

    def test_from_marker_white_black(self):
        self.assertEqual(Color.from_marker(-1), Color.BLACK)
        self.assertEqual(Color.from_marker(-2), Color.BLACK)
        self.assertEqual(Color.from_marker(-3), Color.BLACK)
        self.assertEqual(Color.from_marker(-4), Color.BLACK)
        self.assertEqual(Color.from_marker(-5), Color.BLACK)
        self.assertEqual(Color.from_marker(-6), Color.BLACK)

