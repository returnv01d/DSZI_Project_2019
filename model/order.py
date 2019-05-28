class Order:
    id = 0
    def __init__(self, table_id, order_name):
        self.id = Order.id
        Order.id += 1
        self.table_id = table_id
        self.name = order_name
        self.is_delivered = False
        self.is_taken_from_kitchen = False


    def __repr__(self):
        return "{0}-{1}".format(self.table_id, self.name)



    # def __eq__(self, other):
    #     if other.id == self.id:
    #         return True
    #     return False