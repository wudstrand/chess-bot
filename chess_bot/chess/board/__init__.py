from dataclasses import dataclass
from typing import List, Optional

from chess_bot.chess.piece import Piece
from chess_bot.chess.constant import Constants


@dataclass
class BoardState:
    white_pieces: List[Piece]
    black_pieces: List[Piece]


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

    def get_piece_from_rank_and_file(self, file: str, rank: int) -> Optional[Piece]:
        file_idx = ord(file) - ord('a')
        rank_idx = rank - 1
        return self.get_piece(file_idx=file_idx, rank_idx=rank_idx)

    def get_piece(self, file_idx: int, rank_idx: int) -> Optional[Piece]:
        marker = self._raw_board[rank_idx][file_idx]
        return Piece.from_board(marker, rank_idx=rank_idx, file_idx=file_idx)

    def is_open(self, file_idx: int, rank_idx: int) -> bool:
        marker = self._raw_board[rank_idx][file_idx]
        return marker == 0


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


