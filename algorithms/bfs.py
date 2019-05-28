class BFS:
    found_solution = False
    soulution = None
    name = "BFS"

    @staticmethod
    def bfs(board, current_solution, previous_move, depth=0):
        print("bfs")