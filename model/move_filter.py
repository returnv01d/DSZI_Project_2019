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
        if fields["UP"].__class__.__name__ == Carpet.__name__ and previous_move == MoveType.DOWN:
            fields[MoveType.UP] = None
        elif fields["DOWN"].__class__.__name__ == Carpet.__name__ and previous_move == MoveType.UP:
            fields[MoveType.DOWN] = None
        elif fields["LEFT"].__class__.__name__ == Carpet.__name__ and previous_move == MoveType.RIGHT:
            fields[MoveType.LEFT] = None
        elif fields["RIGHT"].__class.__name__ == Carpet.__name__ and previous_move == MoveType.LEFT:
            fields[MoveType.RIGHT] = None

    @staticmethod
    def check_interactions(fields, previous_move):
        MoveFilter.filter_possible_moves(fields, previous_move)

