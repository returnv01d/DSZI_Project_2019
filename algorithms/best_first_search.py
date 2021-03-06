import copy
import math


class BestFirstSearch:
    found_solution = False
    soulution = None
    name = "A*"

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

        # print(vector_after_move)
        return vector_after_move

    @staticmethod
    def vector_length(vector, x_f, x_s, y_f, y_s):
        # print(vector)
        vector[0] += x_f - x_s
        vector[1] += y_f - y_s

        # print("vector: 01")
        # print(vector[0])
        # print(vector[1])

        prediction_value = float(math.sqrt(vector[0] * vector[0] + vector[1] * vector[1]))

        # print(prediction_value)
        return prediction_value

        # vector[0] += board.waiter.x - board.kitchen.x
        # vector[1] += board.waiter.y - board.kitchen.y

    @staticmethod
    def count_heuristic(board, possible_moves):
        for move in possible_moves:

            # vector_to_possible_aim = [0, 0]
            if move.type.name == "SERVE_ORDER":
                move.prediction_value = 0
                # print("Nadano wartosc: 0 SERVE_ORDER")
            elif move.type.name == "TAKE_ORDER":
                move.prediction_value = 1
                # print("Nadano wartosc: 1 TAKE_ORDER")
            else:
                vector = BestFirstSearch.vector_displacement(move.type.name)
                # print(vector)
                if not board.waiter.heldOrders:

                    move.prediction_value = BestFirstSearch.vector_length(vector, board.waiter.x, board.kitchen.x,
                                                                          board.waiter.y,
                                                                          board.kitchen.y)
                    # print("Sprawdzam do kuchni {0}".format(move.prediction_value))

                elif len(board.waiter.heldOrders) == 2:
                    # print(board.waiter.heldOrders)
                    distances = []
                    for table in board.tables:
                        # print("position of table x: {0}, y: {1}".format(table.x, table.y))
                        # print(table)
                        # print(table.id)
                        # print(board.waiter.heldOrders[0].table_id)
                        # print(board.waiter.heldOrders[1].table_id)
                        if table.id == board.waiter.heldOrders[0].table_id or table.id == board.waiter.heldOrders[
                            1].table_id:
                            distances.append(
                                BestFirstSearch.vector_length(list(vector), board.waiter.x, table.x, board.waiter.y,
                                                              table.y))
                    # print("distances {0}".format(distances))
                    move.prediction_value = min(distances)
                    # print(move.prediction_value)
                elif len(board.waiter.heldOrders) == 1:
                    # print(board.waiter.heldOrders)
                    for table in board.tables:
                        # print("position of table x: {0}, y: {1}".format(table.x, table.y))
                        # print(table)
                        # print(table.id)
                        # print(board.waiter.heldOrders[0].table_id)
                        # print(board.waiter.heldOrders[1].table_id)
                        if table.id == board.waiter.heldOrders[0].table_id:
                            move.prediction_value = BestFirstSearch.vector_length(vector, board.waiter.x, table.x,
                                                                                  board.waiter.y, table.y)
                    # print(move.prediction_value)

    @staticmethod
    def best_first(board, current_solution, move_queue, previous_move, depth=0):

        if depth > 1000:
            print("przekroczono maksymalna glebokosc")
            return
        if BestFirstSearch.found_solution:
            print("znaleziono juz gdzies rozwiazanie")
            return

        new_solution = list(current_solution)

        if board.all_orders_served():
            new_solution.append(previous_move)
            BestFirstSearch.found_solution = True
            BestFirstSearch.soulution = new_solution
            return new_solution
        if previous_move.type.name != "EMPTY_MOVE":
            new_solution.append(previous_move)

        possible_moves = board.get_possible_waiter_moves(previous_move)

        BestFirstSearch.count_heuristic(board, possible_moves)

        new_solution_copy = copy.deepcopy(new_solution)

        for possible_move in possible_moves:
            move_queue.append([possible_move.prediction_value, possible_move, copy.deepcopy(board), copy.deepcopy(new_solution)])

        move_queue.sort(key=lambda move: move[0])

        new_move = move_queue.pop(0)

        BestFirstSearch.best_first(new_move[2].do(new_move[1]), new_move[3], move_queue, new_move[1], depth + 1)
