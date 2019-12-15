import constant
import sys


def circuit_path(grid, direction, x, y, value, mark_parameter, steps):
    next_x = x
    next_y = y
    mark, other_mark = mark_parameter
    for i in range(0, value):
        next_x, next_y = calculate_next_coordinates(direction, next_x, next_y)
        previous_value = grid.get((next_x, next_y))
        if previous_value:
            (previous_mark, previous_steps) = previous_value
            if previous_mark == other_mark:
                cross_steps = previous_steps + steps
                new_value = (constant.CROSS_WIRE_MARK, cross_steps)
            else:
                new_value = (mark, steps)
        else:
            new_value = (mark, steps)
        steps += 1

        grid[next_x, next_y] = new_value

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
    grid = {}
    return grid


def retrieve_crossing_coordinates(grid):
    cross_coordinates = []
    for (x, y) in grid:
        (mark, steps) = grid[x, y]
        if mark == constant.CROSS_WIRE_MARK:
            cross_coordinates.append((x, y))

    return cross_coordinates


def calculate_shortest_distance(grid):
    crossing_coordinates = retrieve_crossing_coordinates(grid)
    min_value = sys.maxsize
    min_steps = sys.maxsize
    for x, y in crossing_coordinates:
        addition = abs(x) + abs(y)
        (_, steps) = grid[x, y]
        if steps < min_steps:
            min_steps = steps
        if addition < min_value:
            min_value = addition

    print("minSteps:" + str(min_steps))
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
    steps = 1
    for i in range(0, len(wire)):
        direction, value = parse_path(wire[i])
        central_port_x, central_port_y = circuit_path(grid, direction,
                                                      central_port_x, central_port_y, int(value), wire_parameters,
                                                      steps)
        steps += int(value)


def parse_path(path):
    return path[0], path[1:]


wire_1 = ["R8", "U5", "L5", "D3"]
wire_2 = ["U7", "R6", "D4", "L4"]
day3_1(wire_1, wire_2)

wire_1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
wire_2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
day3_1(wire_1, wire_2)

wire_1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
wire_2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
day3_1(wire_1, wire_2)

day3_1(constant.INPUT3_1_1, constant.INPUT3_1_2)
