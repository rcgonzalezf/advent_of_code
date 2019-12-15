import constant
import sys


def circuit_path(grid, direction, x, y, value, mark_parameter):
    next_x = x
    next_y = y
    mark, other_mark = mark_parameter
    for i in range(0, value):
        next_x, next_y = calculate_next_coordinates(direction, next_x, next_y)
        previous_value = grid[next_x][next_y]
        new_value = mark
        if previous_value == other_mark:
            new_value = constant.CROSS_WIRE_MARK
        grid[next_x][next_y] = new_value

    return next_x, next_y


def calculate_next_coordinates(direction, next_x, next_y):
    if direction == "R":
        next_x = next_x + 1
    elif direction == "L":
        next_x = next_x - 1
    elif direction == "U":
        next_y = next_y + 1
    else:
        next_y = next_y - 1
    return next_x, next_y


def create_base_grid():
    w, h = 100, 100
    grid = [[0 for x in range(w)] for y in range(h)]
    return grid


def retrieve_crossing_coordinates(grid):
    x, y = len(grid), len(grid[0])
    cross_coordinates = []
    for i in range(0, x):
        for j in range(0, y):
            if grid[i][j] == constant.CROSS_WIRE_MARK:
                cross_coordinates.append((i, j))
    return cross_coordinates


def calculate_shortest_distance(grid):
    crossing_coordinates = retrieve_crossing_coordinates(grid)
    length = len(crossing_coordinates)
    min_value = sys.maxsize
    min_tuple = (0, 0)
    for x, y in crossing_coordinates:
        addition = x + y
        if addition < min_value:
            min_value = addition
            min_tuple = (x, y)
    # print(min_tuple)
    return min_value


def day3_1(wire1, wire2):
    grid = create_base_grid()
    w1 = (constant.WIRE_1_MARK, constant.WIRE_2_MARK)
    increment_point(grid, w1, wire1)

    w2 = (constant.WIRE_2_MARK, constant.WIRE_1_MARK)
    increment_point(grid, w2, wire2)

    shortest_distance = calculate_shortest_distance(grid)
    print("shortest distance: " + str(shortest_distance))
    return grid


def increment_point(grid, wire_parameters, wire):
    central_port_x = 0
    central_port_y = 0
    for i in range(0, len(wire)):
        direction_2, value_2 = parse_path(wire[i])
        central_port_x, central_port_y = circuit_path(grid, direction_2,
                                                      central_port_x, central_port_y, int(value_2), wire_parameters)


def parse_path(path):
    return path[0], path[1:]


wire_1 = ["R8", "U5", "L5", "D3"]
wire_2 = ["U7", "R6", "D4", "L4"]
day3_1(wire_1, wire_2)

wire_1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
wire_2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
day3_1(wire_1, wire_2)
#
# wire_1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
# wire_2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
# day3_1(wire_1, wire_2)
