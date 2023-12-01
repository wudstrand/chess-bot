import unittest
from typing import Optional, List

from chess_bot.chess.board.position import Position
from chess_bot.chess.constant import Constants
from chess_bot.chess.enum.color import Color
from chess_bot.chess.enum.piece_type import PieceType
from chess_bot.chess.piece import Piece

# _valid_positions = [
#     [Position(x=0, y=0), Position(x=1, y=0), Position(x=2, y=0), Position(x=3, y=0), Position(x=4, y=0), Position(x=5, y=0), Position(x=6, y=0), Position(x=7, y=0)],
#     [Position(x=0, y=1), Position(x=1, y=1), Position(x=2, y=1), Position(x=3, y=1), Position(x=4, y=1), Position(x=5, y=1), Position(x=6, y=1), Position(x=7, y=1)],
#     [Position(x=0, y=2), Position(x=1, y=2), Position(x=2, y=2), Position(x=3, y=2), Position(x=4, y=2), Position(x=5, y=2), Position(x=6, y=2), Position(x=7, y=2)],
#     [Position(x=0, y=3), Position(x=1, y=3), Position(x=2, y=3), Position(x=3, y=3), Position(x=4, y=3), Position(x=5, y=3), Position(x=6, y=3), Position(x=7, y=3)],
#     [Position(x=0, y=4), Position(x=1, y=4), Position(x=2, y=4), Position(x=3, y=4), Position(x=4, y=4), Position(x=5, y=4), Position(x=6, y=4), Position(x=7, y=4)],
#     [Position(x=0, y=5), Position(x=1, y=5), Position(x=2, y=5), Position(x=3, y=5), Position(x=4, y=5), Position(x=5, y=5), Position(x=6, y=5), Position(x=7, y=5)],
#     [Position(x=0, y=6), Position(x=1, y=6), Position(x=2, y=6), Position(x=3, y=6), Position(x=4, y=6), Position(x=5, y=6), Position(x=6, y=6), Position(x=7, y=6)],
# ]

_valid_positions = []


def _expected_pieces_with_color(piece_type: PieceType, color: Color) -> List[List[Piece]]:
    pieces = []
    for rank_of_positions in _valid_positions:
        rank = []
        for position in rank_of_positions:
            piece = Piece(piece_type=piece_type, color=color, position=position)
            rank.append(piece)
    return pieces


class PieceTest(unittest.TestCase):
    def test_blank_space(self):
        self.__test_all_board_positions(marker=0, expected_pieces=None)
        self.__test_invalid_board_positions(marker=0)

    def test_pawn(self):
        expected_white_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.WHITE)
        self.__test_all_board_positions(marker=1, expected_pieces=expected_white_pieces)
        expected_black_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.BLACK)
        self.__test_all_board_positions(marker=-1, expected_pieces=expected_black_pieces)
        
        self.__test_invalid_board_positions(marker=1)
        self.__test_invalid_board_positions(marker=-1)

    def test_knight(self):
        expected_white_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.WHITE)
        self.__test_all_board_positions(marker=2, expected_pieces=expected_white_pieces)
        expected_black_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.BLACK)
        self.__test_all_board_positions(marker=-2, expected_pieces=expected_black_pieces)
        
        self.__test_invalid_board_positions(marker=2)
        self.__test_invalid_board_positions(marker=-2)

    def test_bishop(self):
        expected_white_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.WHITE)
        self.__test_all_board_positions(marker=3, expected_pieces=expected_white_pieces)
        expected_black_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.BLACK)
        self.__test_all_board_positions(marker=-3, expected_pieces=expected_black_pieces)
        
        self.__test_invalid_board_positions(marker=3)
        self.__test_invalid_board_positions(marker=-3)

    def test_rook(self):
        expected_white_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.WHITE)
        self.__test_all_board_positions(marker=4, expected_pieces=expected_white_pieces)
        expected_black_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.BLACK)
        self.__test_all_board_positions(marker=-4, expected_pieces=expected_black_pieces)
        
        self.__test_invalid_board_positions(marker=4)
        self.__test_invalid_board_positions(marker=-4)

    def test_queen(self):
        expected_white_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.WHITE)
        self.__test_all_board_positions(marker=5, expected_pieces=expected_white_pieces)
        expected_black_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.BLACK)
        self.__test_all_board_positions(marker=-5, expected_pieces=expected_black_pieces)
        
        self.__test_invalid_board_positions(marker=5)
        self.__test_invalid_board_positions(marker=-5)

    def test_king(self):
        expected_white_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.WHITE)
        self.__test_all_board_positions(marker=6, expected_pieces=expected_white_pieces)
        expected_black_pieces = _expected_pieces_with_color(piece_type=PieceType.PAWN, color=Color.BLACK)
        self.__test_all_board_positions(marker=-6, expected_pieces=expected_black_pieces)
        
        self.__test_invalid_board_positions(marker=6)
        self.__test_invalid_board_positions(marker=-6)

    def __test_invalid_board_positions(self, marker: int):
        invalid_idx = [-12, -11, -10, -9, -8, 8, 9, 10, 11, 12]

        for rank_idx in invalid_idx:
            for file_idx in invalid_idx:
                result = Piece.from_board(
                    marker=marker,
                    rank_idx=rank_idx,
                    file_idx=file_idx
                )
                self.assertEqual(result, None)

    def __test_all_board_positions(self, marker: int, expected_pieces: Optional[List[List[Piece]]]):
        for rank_idx in range(Constants.number_of_ranks.value):
            for file_idx in range(Constants.number_of_files.value):
                expected_piece = expected_pieces[rank_idx][file_idx] if expected_pieces else None
                result = Piece.from_board(
                    marker=marker,
                    rank_idx=rank_idx,
                    file_idx=file_idx
                )
                self.assertEqual(result, expected_piece)
