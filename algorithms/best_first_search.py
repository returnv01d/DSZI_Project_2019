import copy
import math

class Best_first_search:
    found_solution = False

    @staticmethod
    def best_first(board, current_solution, to_do_move, depth = 0):
        if depth > 1000:
            print("przekroczono maksymalna glebokosc")
            return
        if Best_first_search.found_solution:
            print("znaleziono juz gdzies rozwiazanie")
            return

        new_solution = list(current_solution)

        if board.all_orders_served():
            new_solution.append(to_do_move)
            Best_first_search.found_solution = True
            return new_solution
        new_solution.append(to_do_move)

        possible_moves = []
        possible_moves = board.get_possible_waiter_moves(to_do_move)

        # print(possible_moves)

        for move in possible_moves:

            vector_to_possible_aim = [0, 0]
            if move.type.name == "SERVE_ORDER":
                move.prediction_value = 0
                # print("Nadano wartosc: 0 SERVE_ORDER")
            elif move.type.name == "TAKE_ORDER":
                move.prediction_value = 1
                # print("Nadano wartosc: 1 TAKE_ORDER")
            else:
                if move.type.name == "UP":
                    vector_to_possible_aim[0] = - 1
                elif move.type.name == "DOWN":
                    vector_to_possible_aim[0] = + 1
                elif move.type.name == "LEFT":
                    vector_to_possible_aim[1] = - 1
                elif move.type.name == "RIGHT":
                    vector_to_possible_aim[1] = + 1

                # print(vector_to_possible_aim)
                # print(board.waiter.x, board.waiter.y)

                if not board.waiter.heldOrders:
                    vector_to_possible_aim[0] += board.waiter.x - board.kitchen.x
                    vector_to_possible_aim[1] += board.waiter.y - board.kitchen.y
                    # print(vector_to_possible_aim)

                    move.prediction_value = float(math.sqrt(
                        vector_to_possible_aim[0] * vector_to_possible_aim[0] + vector_to_possible_aim[1] *
                        vector_to_possible_aim[1]))

                    # print(move.prediction_value)

                elif len(board.waiter.heldOrders) == 2:
                    inf = float(math.inf)
                    # print(board.waiter.heldOrders)

                    distances = []
                    for table in board.tables:
                        # print(table)
                        # print(table.id)
                        # print(board.waiter.heldOrders[0].table_id)
                        # print(board.waiter.heldOrders[1].table_id)
                        if table.id == board.waiter.heldOrders[0].table_id or table.id == board.waiter.heldOrders[1].table_id:
                            vector = vector_to_possible_aim
                            vector[0] += board.waiter.x - table.x
                            vector[1] += board.waiter.y - table.y
                            distance = float(math.sqrt(vector[0]*vector[0] + vector[1]*vector[1]))
                            distances.append(distance)
                    move.prediction_value = min(distances)
                    # print(move.prediction_value)
                else:
                    for table in board.tables:
                        # print(table)
                        # print(table.id)
                        # print(board.waiter.heldOrders[0].table_id)
                        if table.id == board.waiter.heldOrders[0].table_id:
                            vector = vector_to_possible_aim
                            vector[0] += board.waiter.x - table.x
                            vector[1] += board.waiter.y - table.y
                            distance = float(math.sqrt(vector[0]*vector[0] + vector[1]*vector[1]))

                            move.prediction_value = distance
                    # print(move.prediction_value)


        possible_moves.sort(key=lambda move: move.prediction_value)

        for move in possible_moves:
            board_copy = copy.deepcopy(board)
            Best_first_search.best_first(copy.deepcopy(board_copy.do(move)), new_solution, move, depth + 1)
