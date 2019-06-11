
class Move:
    def __init__(self, move_type, first_order=None, second_order=None, target_table_id=None):
        self.type = move_type

        self.first_order = first_order
        self.second_order = second_order
        self.target_table_id = target_table_id
        self.items = [first_order, second_order, target_table_id]
        self.prediction_value = None


    def __repr__(self):
        return "{0} items: {1} pred_value: {2}".format(self.type, self.items, self.prediction_value)
