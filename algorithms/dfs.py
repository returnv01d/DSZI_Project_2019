import copy
class DFS:
    found_solution = False
    solution = None
    name = "DFS"

    @staticmethod
    def dfs(board, current_solution, previous_move, depth=0):
        if depth > 1000:
            print("przekroczono maksymalną głebokosc")
            return
        if DFS.found_solution:
            print("znaleziono juz gdzies rozwiązanie, ucinamy szukające wciąż rozwiązania dfsy")
            return
        # print()
        # print("dfs {0}.all orders served? {1}".format(str(depth), board.all_orders_served()))

        new_solution = list(current_solution)
        if board.all_orders_served():
            new_solution.append(previous_move)
            # print("returning solution:")
            # print(new_solution)
            DFS.found_solution = True
            DFS.solution = new_solution
            return new_solution
        new_solution.append(previous_move)

        # print("current solution: {0}".format(new_solution))
        # print("possible moves: {0}".format(board.get_possible_waiter_moves(previous_move)))
        for move in board.get_possible_waiter_moves(previous_move):
            # print("dfs {0} doing move {1}".format(str(depth), move))
            board_copy = copy.deepcopy(board)
            DFS.dfs(copy.deepcopy(board_copy.do(move)), new_solution, move, depth + 1)