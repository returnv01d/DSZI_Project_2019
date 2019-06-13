from enum import Enum

class MoveType(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    TAKE_ORDER = 4
    SERVE_ORDER = 5
    EMPTY_MOVE = 6

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

    def __str__(self):
        return "Type: {0}".format(str(self.name))
