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
        return "table-id:{0}.order id:{1}, {2}".format(self.table_id, self.id ,self.name)

