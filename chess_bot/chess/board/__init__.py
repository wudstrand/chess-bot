from dataclasses import dataclass
from typing import List, Optional

from chess_bot.chess.enum.color import Color
from chess_bot.chess.board.position import Position
from chess_bot.chess.piece import Piece
from chess_bot.chess.constant import Constants


@dataclass
class BoardState:
    white_pieces: List[Piece]
    black_pieces: List[Piece]


class Board:
    def __init__(self, raw_board: List[List[int]]):
        self._raw_board: List[List[int]] = raw_board
        self._pieces: Optional[List[Piece]] = None
        self._white_pieces: Optional[List[Piece]] = None
        self._black_pieces: Optional[List[Piece]] = None

    @property
    def pieces(self) -> List[Piece]:
        if self._pieces:
            return self._pieces

        pieces = []
        for rank_idx, rank in enumerate(self._raw_board):
            for file_idx, marker in enumerate(rank):
                maybe_piece = Piece.from_board(marker=marker, rank_idx=rank_idx, file_idx=file_idx)
                pieces.append(maybe_piece)
        self._pieces = [maybe_piece for maybe_piece in pieces if maybe_piece]
        return self._pieces

    @property
    def white_pieces(self) -> List[Piece]:
        if self._white_pieces:
            return self._white_pieces

        self._white_pieces = self.__filter_pieces(color=Color.WHITE)
        return self._white_pieces

    @property
    def black_pieces(self) -> List[Piece]:
        if self._black_pieces:
            return self._black_pieces

        self._black_pieces = self.__filter_pieces(color=Color.BLACK)
        return self._black_pieces

    def get_piece(self, color: Color) -> List[Piece]:
        if color == Color.WHITE:
            return self.white_pieces
        return self.black_pieces

    def get_piece(self, position: Position) -> Optional[Piece]:
        return self._get_piece(file_idx=position.file.idx, rank_idx=position.rank.idx)

    def is_open(self, position: Position) -> bool:
        return self._is_open(file_idx=position.file.idx, rank_idx=position.rank.idx)

    def _get_piece(self, file_idx: int, rank_idx: int) -> Optional[Piece]:
        marker = self._raw_board[rank_idx][file_idx]
        return Piece.from_board(marker, rank_idx=rank_idx, file_idx=file_idx)

    def _is_open(self, file_idx: int, rank_idx: int) -> bool:
        marker = self._raw_board[rank_idx][file_idx]
        return marker == 0

    def __filter_pieces(self, color: Color) -> List[Piece]:
        return [piece for piece in self.pieces if piece.color == color]

    def __iter__(self):
        for rank_idx, rank in enumerate(self._raw_board):
            for file_idx, marker in enumerate(rank):
                yield rank_idx, file_idx, marker


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


