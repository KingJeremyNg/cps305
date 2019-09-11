import random

def monkeyTypist() :

    target = list("methinks it is like a weasel")
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    lenS = len(target)

    bestStr = generate(lenS, alphabet)
    bestScore = calcScore(bestStr, target)

    print("String\t\t\t\t\tScore")

    while bestScore < 100 :
        if bestScore == 100 :
            break
        newStr = generate(lenS, alphabet)
        newScore = calcScore(newStr, target)
        if newScore > bestScore :
            bestScore = newScore
            bestStr = newStr
        if epoch == 100000 :
            print ("%s\t\t%d" % ("".join(bestStr), bestScore))
            epoch = 0
        epoch += 1

def generate(lenS, alphabet) :
    string = []
    for i in range(lenS) :
        string.append(alphabet[random.randint(0, len(alphabet) - 1)])
    return string

def calcScore(newStr, target) :
    count = 0
    for i in range(len(target)) :
        if newStr[i] == target[i] :
            count += 1
    return (count (float) / target (float))

monkeyTypist()