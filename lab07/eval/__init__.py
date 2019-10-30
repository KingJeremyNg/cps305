alpha = "abcdefghijklmnopqrstuvwxyz"


def expressionChild(tree, env):
    if (tree[0] in alpha):
        return checkEnv(tree[0], env)
    elif tree[0] == "0":
        return 0
    elif str.isdigit(tree[0]):
        return float(tree[0])
    elif tree == [] or tree[1] == [] or tree[2] == []:
        return None
    elif (expressionChild(tree[1], env)) == None or (expressionChild(tree[2], env)) == None:
        return None
    elif tree[0] == "+":
        return (expressionChild(tree[1], env)) + (expressionChild(tree[2], env))
    elif tree[0] == "-":
        return (expressionChild(tree[1], env)) - (expressionChild(tree[2], env))
    elif tree[0] == "*":
        return (expressionChild(tree[1], env)) * (expressionChild(tree[2], env))
    elif tree[0] == "/":
        divider = (expressionChild(tree[2], env))
        if divider == 0:
            return None
        else:
            return (expressionChild(tree[1], env)) / divider
    else:
        return None


def checkEnv(value, env):
    if len(env) == 1 :
        if env[0] == value:
            return env[1]
    for element in env:
        if element[0] == value:
            return element[1]
    return None


def evalTree(tree, env):
    if tree == [[], [], []]:
        return None
    elif str.isdigit(tree[0]):
        return float(tree[0])
    elif tree[1] == [] and tree[2] == []:
        check = checkEnv(tree[0], env)
        if check == None:
            return tree[0]
        else:
            return check
    elif (expressionChild(tree[1], env)) == None or (expressionChild(tree[2], env)) == None:
        return None
    elif tree[0] == "+":
        return (expressionChild(tree[1], env)) + (expressionChild(tree[2], env))
    elif tree[0] == "-":
        return (expressionChild(tree[1], env)) - (expressionChild(tree[2], env))
    elif tree[0] == "*":
        return (expressionChild(tree[1], env)) * (expressionChild(tree[2], env))
    elif tree[0] == "/":
        divider = (expressionChild(tree[2], env))
        if divider == 0:
            return None
        else:
            return (expressionChild(tree[1], env)) / divider
    else:
        return tree[0]