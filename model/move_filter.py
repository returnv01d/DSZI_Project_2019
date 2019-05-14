from model.carpet import Carpet
from model.freeSpace import FreeSpace
from model.move import Move
from model.move_type import MoveType

class MoveFilter:

    @staticmethod
    def filter_possible_moves(fields, previous_move):
        MoveFilter.filter_previous_move(fields, previous_move)
        return MoveFilter.filter_from_none_and_free_space(fields)

    @staticmethod
    def filter_from_none_and_free_space(fields):
        filtered = dict(filter(lambda item: item[1] is not None and item[1].__class__.__name__ != FreeSpace.__name__,
                               fields.items()))
        return filtered

    @staticmethod
    def filter_previous_move(fields, previous_move):
        if fields["UP"] == Carpet.__name__ and previous_move.type == MoveType.UP:
            fields["UP"] = None
        elif fields["DOWN"] == Carpet.__name__ and previous_move.type == MoveType.DOWN:
            fields["DOWN"] = None
        elif fields["LEFT"] == Carpet.__name__ and previous_move.type == MoveType.LEFT:
            fields["LEFT"] = None
        elif fields["RIGHT"] == Carpet.__name__ and previous_move.type == MoveType.RIGHT:
            fields["RIGHT"] = None