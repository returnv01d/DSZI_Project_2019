import copy
import math

class BestFirstSearch:
    found_solution = False
    soulution = None
    name = "DFS"


    @staticmethod
    def vector_displacement(move_type):

        vector_after_move = [0, 0]
        if move_type == "UP":
            vector_after_move[0] = - 1
        elif move_type == "DOWN":
            vector_after_move[0] = + 1
        elif move_type == "LEFT":
            vector_after_move[1] = - 1
        elif move_type == "RIGHT":
            vector_after_move[1] = + 1

        print(vector_after_move)
        return vector_after_move

    @staticmethod
    def vector_lenght(vector, x_f, x_s, y_f, y_s):
        vector[0] += x_f - x_s
        vector[1] += y_f - y_s

        prediction_value = float(math.sqrt(vector[0] * vector[0] + vector[1] * vector[1]))

        print(prediction_value)
        return prediction_value

        # vector[0] += board.waiter.x - board.kitchen.x
        # vector[1] += board.waiter.y - board.kitchen.y

    @staticmethod
    def count_heuristic(board, possible_moves):
        for move in possible_moves:

            # vector_to_possible_aim = [0, 0]
            if move.type.name == "SERVE_ORDER":
                move.prediction_value = 0
                print("Nadano wartosc: 0 SERVE_ORDER")
            elif move.type.name == "TAKE_ORDER":
                move.prediction_value = 1
                print("Nadano wartosc: 1 TAKE_ORDER")
            else:
                vector = BestFirstSearch.vector_displacement(move.type.name)
                print(vector)
                if not board.waiter.heldOrders:

                    move.prediction_value = BestFirstSearch.vector_lenght(vector, board.waiter.x, board.kitchen.x,
                                                                          board.waiter.y,
                                                                          board.kitchen.y)
                elif len(board.waiter.heldOrders) == 2:
                    # print(board.waiter.heldOrders)
                    distances = []
                    for table in board.tables:
                        # print(table)
                        # print(table.id)
                        # print(board.waiter.heldOrders[0].table_id)
                        # print(board.waiter.heldOrders[1].table_id)
                        if table.id == board.waiter.heldOrders[0].table_id or table.id == board.waiter.heldOrders[1].table_id:
                            distances.extend(BestFirstSearch.vector_lenght(vector, board.waiter.x, table.x, board.waiter.y, table.y))
                    move.prediction_value = min(distances)
                    print(move.prediction_value)
                elif len(board.waiter.heldOrders) == 1:
                    # print(board.waiter.heldOrders)
                    for table in board.tables:
                        # print(table)
                        # print(table.id)
                        # print(board.waiter.heldOrders[0].table_id)
                        # print(board.waiter.heldOrders[1].table_id)
                        if table.id == board.waiter.heldOrders[0].table_id:
                            move.prediction_value = BestFirstSearch.vector_lenght(vector, board.waiter.x, table.x,
                                                                                  board.waiter.y, table.y)
                    print(move.prediction_value)

    @staticmethod
    def best_first(board, current_solution, all_moves, to_do_move, depth=0):

        all_moves.pop(0)

        print("all moves po wykonaniu {0}".format(all_moves))
        if depth > 1000:
            print("przekroczono maksymalna glebokosc")
            return
        if BestFirstSearch.found_solution:
            print("znaleziono juz gdzies rozwiazanie")
            return

        new_solution = list(current_solution)

        if board.all_orders_served():
            new_solution.append(to_do_move)
            BestFirstSearch.found_solution = True
            BestFirstSearch.soulution = new_solution
            return new_solution
        new_solution.append(to_do_move)

        possible_moves = []
        possible_moves = board.get_possible_waiter_moves(to_do_move)

        # print(possible_moves)

        BestFirstSearch.count_heuristic(board, possible_moves)

        all_moves.extend(possible_moves)
        all_moves.sort(key=lambda move: move.prediction_value)

        print("all_moves {0}".format(all_moves))

        board_copy = copy.deepcopy(board)
        BestFirstSearch.best_first(copy.deepcopy(board_copy.do(all_moves[0])), new_solution, all_moves, all_moves[0],
                                   depth + 1)
