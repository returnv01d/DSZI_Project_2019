from enum import Enum

class MoveType(Enum):
    EMPTY_MOVE = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    TAKE_ORDER = 5
    SERVE_ORDER = 6

    @staticmethod
    def opposite_move(move):
        if move.type == MoveType.UP:
            return MoveType.DOWN
        elif move.type == MoveType.DOWN:
            return MoveType.UP
        elif move.type == MoveType.LEFT:
            return MoveType.RIGHT
        elif move.type == MoveType.RIGHT:
            return MoveType.LEFT
