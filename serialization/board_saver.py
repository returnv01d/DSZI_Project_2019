class BoardSaver:

    @staticmethod
    def save_board_to_file(board, filepath):
        file = open(filepath, "w")

        file.write(str(board.board_size))
        file.write("\n")
        file.write("{0} {1}".format(str(board.waiter.x), str(board.waiter.y)))
        file.write("\n")

        for i in range(0, board.board_size):
            for j in range(0, board.board_size):
                file.write(str(board.objects[i][j]) + " ")
            file.write("\n")
        file.close()