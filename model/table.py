from sprites.tableSprite import TableSprite

class Table:
    id = 0

    def __init__(self):
        self.id = Table.id
        Table.id += 1

        self.sprite = None

    def create_sprite(self, width, height):
        self.sprite = TableSprite(width, height)
        self.sprite.update_status(self.status())

    def __repr__(self):
        return "Table"

    def __str__(self):
        return 'T'

    def status(self):
        return ["id: " + str(self.id)]