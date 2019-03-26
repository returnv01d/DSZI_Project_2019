import pygame

class Order:
    def __init__(self, table_id, order_name):
        self.table_id = table_id
        self.order_name = order_name
        self.is_delivered = False