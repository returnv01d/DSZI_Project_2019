class Order:

    def __init__(self, table_id, order_name):
        self.table_id = table_id
        self.order_name = order_name
        self.is_delivered = False
        self.is_taken_from_kitchen = False


    def __repr__(self):
        return "{0}-{1}".format(self.table_id, self.order_name)