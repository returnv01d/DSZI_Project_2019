from sprites.tableSprite import TableSprite

class Table:
    id = 0

    def __init__(self):
        self.id = Table.id
        Table.id += 1

        self.sprite = None

    def create_sprite(self, width, height):
        self.sprite = TableSprite(width, height)

    def __repr__(self):
        return "Table"
