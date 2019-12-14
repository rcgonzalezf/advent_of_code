# https://adventofcode.com/2019/day/1
import math


def fuel_calculator(mass):
    result = 0
    fuel = mass
    while True:
        fuel = fuel_calculator_internal(fuel)
        if fuel > 0:
            result += fuel
        else:
            break

    return result


def fuel_calculator_internal(mass):
    third_of_mass = mass / 3
    round_down = math.floor(third_of_mass)
    fuel = round_down - 2
    return fuel


def print_fuel(mass):
    print(fuel_calculator(mass))


def read_file(file_name):
    lines = []
    file = ""
    try:
        file = open(file_name, "r")
        for line in file:
            lines.append(int(line))
        return lines
    finally:
        file.close()


def day1_solver_part1():
    return day1_solver(True)


def day1_solver_part2():
    return day1_solver(False)


def day1_solver(is_part_one):
    masses = read_file("./input.txt")
    fuels = []
    for mass in masses:
        if is_part_one:
            fuel = fuel_calculator_internal(mass)
        else:
            fuel = fuel_calculator(mass)
        fuels.append(fuel)
    result = 0
    for fuel in fuels:
        result += fuel
    return result


# print_fuel(12)
# print_fuel(14)
# print_fuel(1969)
# print_fuel(100756)
# print(read_file("./input.txt"))
print(day1_solver_part1())
print(day1_solver_part2())
