class BoardSaver:

    @staticmethod
    def save_board_to_file(board, filepath):
        file = open(filepath, "w")

        file.write(str(board.board_size))
        file.write("\n")
        file.write("{0} {1}".format(str(board.waiter.y), str(board.waiter.x)))
        file.write("\n")
        file.write(str(len(board.kitchen.waiting_orders)))
        file.write("\n")


        for j in range (0, len(board.kitchen.waiting_orders)):
            file.write("{0} {1}".format(str(board.kitchen.waiting_orders[j].table_id), str(board.kitchen.waiting_orders[j].order_name)))
            file.write("\n")

        for i in range(0, board.board_size):
            for j in range(0, board.board_size):
                file.write(str(board.objects[i][j]) + " ")
            file.write("\n")
        file.close()