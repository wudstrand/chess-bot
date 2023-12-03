from typing import List

from chess_bot.chess.piece import Piece
from chess_bot.chess.board.position import Position


# Should this code generate all move to n-depth or should it just do on turn worth....
#
# How to handle testing the moves legality?
# Need
#   - board
#   - piece movement history (i.e. is the first move)


def generate_moves(
        piece: Piece
) -> List[Position]:
    pass


def _pawn_moves(position: Position) -> List[Position]:
    # Cases
    # 1. First move - Can move up to two squares forward
    # 2. en passant
    pass


def _knight_moves(position: Position) -> List[Position]:
    move_options = [(3, 1), (3, -1), (-3, 1), (-3, -1)]
    return [position.move(file_delta=x, rank_delta=y) for x, y in move_options]


def _bishop_moves(position: Position) -> List[Position]:
    move_options = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    pass


def _rook_moves(position: Position) -> List[Position]:
    move_options = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    pass


def _queen_moves(position: Position) -> List[Position]:
    pass


def _king_moves(position: Position) -> List[Position]:
    move_options = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, 1), (1, -1), (-1, -1)
    ]
    return [position.move(file_delta=x, rank_delta=y) for x, y in move_options]
