# https://adventofcode.com/2019/day/4

puzzle_input = "137683-596253"
max_digits = 6


def two_adjacent_are_the_same(previous, current):
    return previous == current

def only_increase_or_stay_the_same(first_digit, digits):
    previous = first_digit
    for d in digits:
        if previous > int(d):
            return False
        previous = int(d)
    return True


def meets_criteria(password):
    l = len(password)
    two_adjacent_rule = False
    increase_rule = only_increase_or_stay_the_same(int(password[0]), password)

    # regular 2 adjacent rule
    for i in range(1, l):
        two_adjacent_rule = two_adjacent_are_the_same(password[i - 1], password[i])
        if two_adjacent_rule:
            break
    # matching digit should contain one pair at least
    matching_number = {}
    for i in range(1, l):
        n = password[i]
        if two_adjacent_are_the_same(password[i - 1], n):
            previous_matches = matching_number.get(n)
            if previous_matches:
                matching_number[n] = previous_matches + 1
            else:
                matching_number[n] = 1

    matching_number_pair_rule = False
    for key in matching_number:
        if matching_number[key] == 1:
            matching_number_pair_rule = True
            break

    if two_adjacent_rule and increase_rule and matching_number_pair_rule:
        return True
    else:
        return False


def day_4():
    passwords = []
    for p in range(137683, 596253 + 1):
        passwords.append(str(p))

    # passwords.append(data)
    count = 0

    for password in passwords:
        meets = meets_criteria(password)
        if meets:
            print(password + ": " + str(meets_criteria(password)))
            count += 1
    print(count)


# day_4("111111")
# day_4("223450")
# day_4("123789")
# day_4("112233") # True
# day_4("123444") # False
# day_4("111122") # True
# day_4("566789") # True
day_4()  # part1 = 1864, part 2 = 1258
