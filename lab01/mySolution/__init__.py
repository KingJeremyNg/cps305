import random
import matplotlib.pyplot as plot

def monkeyTypist() :

    target = "methinks it is like a weasel"
    alphabet = "abcdefghijklmnopqrstuvwxyz "

    lenS = len(target)
    lenA = len(alphabet)

    scores = []
    counter = []

    count = 0
    epoch = 0

    newStr = [None] * lenS

    for i in range(lenS) :
        newStr[i] = alphabet[random.randint(0, lenA - 1)]

    bestStr = generate(target, alphabet, 0, lenS, lenA, newStr)
    bestScore = calcScore(newStr, target, lenS)
    count += 1
    epoch += 1

    print("String\t\t\t\t\tScore")

    while bestScore < 100 :

        for i in range(lenS) :
            if newStr[i] != target[i] :
                index = i
                break
        
        newStr = generate(target, alphabet, index, lenS, lenA, newStr)
        newScore = calcScore(newStr, target, lenS)

        count += 1
        epoch += 1

        if newScore > bestScore :
            bestScore = newScore
            bestStr = newStr
            scores.append(bestScore)
            counter.append(count)

        if epoch == 100 :
            print("%s\t\t%f\t\t%d" % ("".join(bestStr), bestScore, count))
            scores.append(bestScore)
            counter.append(count)
            epoch = 0

        if bestScore >= 100 :
            print("%s\t\t%f\t\t%d" % ("".join(bestStr), bestScore, count))
            scores.append(bestScore)
            counter.append(count)
            break

        if count >= 3000 :
            break
    
    plot.scatter(counter, scores, color = 'r', marker = '+')
    plot.xlabel("Iterations")
    plot.ylabel("Scores")
    plot.show()

def generate(target, alphabet, index, lenS, lenA, newStr) :
    if newStr == [] :
        return []
    temp = list(newStr)
    for n in range(index, lenS) :
        if newStr[n] != target[n] :
            temp[n] = alphabet[random.randint(0, lenA - 1)]
            break
    return temp

def calcScore(newStr, target, lenS) :
    if newStr == [] :
        return 100
    count = 0
    for n in range(lenS) :
        if newStr[n] == target[n] :
            count += 1
    return (float(count) / float(lenS)) * 100

monkeyTypist()