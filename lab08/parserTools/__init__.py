def precedence(oper):
    if oper in ['+', '-']:
        return 1
    elif oper in ['*', '/']:
        return 2
    else:
        return 3


def operatorp(x):
    return x in ['+', '-', '/', '*', '!']


def numberp(x):
    return not operatorp(x)


def parse(expr):
    if expr == []:
        return []
    return parseHelper(expr, [], [])


def parseHelper(expr, operators, operands):
    if expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)
    elif len(expr[0]) > 1:
        return parseHelper(expr[1:], operators, [parse(expr[0])] + operands)
    elif numberp(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], [], []]] + operands)
    elif operators == [] or precedence(expr[0]) > precedence(operators[0]):
        return parseHelper(expr[1:], [expr[0]] + operators, operands)
    else:
        return handleOp(expr, operators, operands)


def handleOp(expr, operators, operands):
    if operators[0] == "!":
        return parseHelper(expr, operators[1:], [[operators[0], operands[0], []]] + operands[1:])
    else:
        return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]] + operands[2:])
