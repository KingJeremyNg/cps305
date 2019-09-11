import random

def generate(lenS, LenA, alphabet) :
    string = ""
    for x in range(lenS) :
        string += alphabet[random.randint(0, len(LenA) + 1) - 1]
    return string
    

def calcScore(newStr, target) :
    for i in range(target) :
        str = generate(lenS, LenA, alphabet)
        print("%s\t%d" % ("".join(str), calcScore(str, target)))

def monkeyTypist() :
    target = list("methinks it is like a weasel")
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    lenS = len(target)
    lenA = len(alphabet)
    epoch = 0

    bestStr = generate(lenS, lenA, alphabet)
    bestScore = calcScore(bestStr, target)

    print("String Score")

    while bestScore < 100 :
        if bestScore == 100 :
            break
        newStr = generate(lenS, lenA, alphabet)
        newScore = calcScore(newStr, target)
        if newScore > bestscore :
            bestScore = newScore
            bestStr = newStr
        if epoch == 100000 :
            print("%s\t\t\t%d" % ("".join(bestStr), bestScore))
            epoch = 0
        epoch += 1