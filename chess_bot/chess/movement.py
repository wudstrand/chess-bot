from typing import List

from chess_bot.chess.piece import Piece
from chess_bot.chess.board.position import Position


# Should this code generate all move to n-depth or should it just do on turn worth....
#
# How to handle testing the moves legality?
# Need
#   - board
#   - piece movement history (i.e. is the first move)

def generate_moves(piece: Piece, depth: int = 1) -> List[Position]:
    pass


def _pawn_move(position: Position, depth: int = 1) -> List[Position]:
    pass


def _knight_move(position: Position, depth: int = 1) -> List[Position]:
    pass


def _bishop_move(position: Position, depth: int = 1) -> List[Position]:
    pass


def _rook_move(position: Position, depth: int = 1) -> List[Position]:
    pass


def _queen_move(position: Position, depth: int = 1) -> List[Position]:
    pass


def _king_move(position: Position, depth: int = 1) -> List[Position]:
    pass
