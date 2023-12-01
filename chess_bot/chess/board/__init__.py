from typing import List

from chess_bot.chess.piece import Piece
from chess_bot.chess.constant import Constants


class Board:
    def __init__(self, raw_board: List[List[int]]):
        self._raw_board: List[List[int]] = raw_board

    def get_pieces(self) -> List[Piece]:
        pieces = []
        for rank_idx, rank in enumerate(self._raw_board):
            for file_idx, marker in enumerate(rank):
                maybe_piece = Piece.from_board(marker=marker, rank_idx=rank_idx, file_idx=file_idx)
                pieces.append(maybe_piece)
        return [maybe_piece for maybe_piece in pieces if maybe_piece]

    def make_move(self) -> 'Board':
        pass


def starter_board() -> Board:
    raw_board = [
        [4, 2, 3, 6, 5, 3, 2, 4],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-4, -2, -3, -6, -5, -3, -2, -4]
    ]
    return Board(raw_board=raw_board)


def blank_board() -> Board:
    raw_board = [
        [0 for _ in range(Constants.number_of_files.value)]
        for _ in range(Constants.number_of_ranks.value)
    ]
    return Board(raw_board=raw_board)


