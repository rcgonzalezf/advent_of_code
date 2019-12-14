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
            resultPos = params[i + 3]
            params[resultPos] = result
        i = i + 4
    return params[pos]


print(day2_1([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 0))

print(day2_1([2, 3, 0, 3, 99], 3))

print(day2_1([2, 4, 4, 5, 99, 0], 5))

print(day2_1([1, 1, 1, 4, 99, 5, 6, 0, 99], 0))

print(day2_1(constant.INPUT, 0)) # 874653
