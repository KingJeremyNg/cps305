from pythonds.basic import Stack

def infixToPostfix(infixexpr) :
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prec["!"] = 4
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList :
        if token in "0123456789" :
            postfixList.append(token)

        elif token == '(' :
            opStack.push(token)

        elif token == ')' :
            topToken = opStack.pop()
            while topToken != '(' :
                postfixList.append(topToken)
                topToken = opStack.pop()

        elif token == '!' :
            opStack.push(token)

        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty() :
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

def postfixEval(postfixExpr) :
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList :
        if token in "0123456789" :
            operandStack.push(int(token))

        elif (token == "!") :
            operand = operandStack.pop()
            result = factorial(operand)
            operandStack.push(result)

        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    
    return operandStack.pop()

def doMath(op, op1, op2) :
    if op == "*" :
        return op1 * op2
    elif op == "/" :
        return op1 / op2
    elif op == "+" :
        return op1 + op2
    else:
        return op1 - op2

def factorial(n) :
    if n == 1 :
        return n
    else :
        return n * factorial(n - 1)

def infixToPostfixEval(expression) :
    if expression == "" :
        return "Empty expression"

    postfix = infixToPostfix(expression)
    evaluation = postfixEval(postfix)

    return str(postfix) + "\nEvaluates to: " + str(evaluation)