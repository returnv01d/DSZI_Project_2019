from model.carpet import Carpet
from model.freeSpace import FreeSpace
from model.kitchen import Kitchen
from model.move.move_type import MoveType
from model.table import Table


class MoveFilter:

    @staticmethod
    def filter_possible_moves(fields, previous_move, waiter):
        x = MoveFilter.filter_previous_move(fields, previous_move)
        s = MoveFilter.check_interactions(x, waiter)
        return MoveFilter.filter_from_none_and_free_space(s)

    @staticmethod
    def filter_from_none_and_free_space(fields):
        filtered = dict(filter(lambda item: item[1] is not None and item[1].__class__.__name__ != FreeSpace.__name__,
                               fields.items()))
        return filtered

    @staticmethod
    def filter_previous_move(fields, previous_move):
        if fields["UP"].__class__.__name__ == Carpet.__name__ and previous_move.type == MoveType.DOWN:
            fields["UP"] = None
        if fields["DOWN"].__class__.__name__ == Carpet.__name__ and previous_move.type == MoveType.UP:
            fields["DOWN"] = None
        if fields["LEFT"].__class__.__name__ == Carpet.__name__ and previous_move.type == MoveType.RIGHT:
            fields["LEFT"] = None
        if fields["RIGHT"].__class__.__name__ == Carpet.__name__ and previous_move.type == MoveType.LEFT:
            fields["RIGHT"] = None

        return fields

    @staticmethod
    def check_interactions(fields, waiter):
        for k,field in fields.items():
            if field.__class__.__name__ == Table.__name__ or field.__class__.__name__ == Kitchen.__name__:
                if not field.check_if_interaction_with_waiter_possible(waiter):
                    fields[k] = None

        return fields