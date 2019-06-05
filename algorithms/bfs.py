import copy
class BFS:
    found_solution = False
    soulution = None
    name = "BFS"
    
    @staticmethod
    def bfs(board, current_solution, previous_move):
        queque = list(current_solution)
        while board.all_orders_served():
            queque.append(previous_move)
            BFS.found_solution = True
            BFS.soulution = queque
            return queque
        queque.append(previous_move)
        for neighbour in board.get_possible_waiter_moves(previous_move):
            board_copy = copy.deepcopy(board)
            BFS.bfs(copy.deepcopy(board_copy.do(neighbour)), queque, neighbour)

