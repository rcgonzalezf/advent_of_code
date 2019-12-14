import constant


def day2_1(params, pos):
    i = 0
    n = len(params)
    while True:
        operation = params[i]
        if i == n or operation == constant.HALT:
            break
        else:
            operand1 = params[params[i + 1]]
            operand2 = params[params[i + 2]]
            if operation == constant.ADD:
                result = operand1 + operand2
            elif operation == constant.MULT:
                result = operand1 * operand2
            else:
                print("Something went wrong")
                break
            result_pos = params[i + 3]
            params[result_pos] = result
        i = i + 4
    return params[pos]


def day2_2():
    noun = 0
    verb = 0
    expected = 19690720
    while noun <= 99:
        while verb <= 99:
            new_input = constant.INPUT_2.copy()
            new_input[1] = noun
            new_input[2] = verb
            result = day2_1(new_input, 0)
            if expected == result:
                print("noun:" + str(noun) + ", verb:" + str(verb))
                return result, noun, verb
            verb = verb + 1
        noun = noun + 1
        verb = 0


# print(day2_1([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 0))
#
# print(day2_1([2, 3, 0, 3, 99], 3))
#
# print(day2_1([2, 4, 4, 5, 99, 0], 5))
#
# print(day2_1([1, 1, 1, 4, 99, 5, 6, 0, 99], 0))
triplet = day2_2()
print(triplet)  # 874653, 5482655

r, n, v = triplet
answer = 100 * n + v
print(answer)
