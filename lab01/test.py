def generate(lenS, LenA, alphabet) :
    target = ""

def calcScore() :
    ok = 0;

def monkeyTypist():
    target = list("methinks it is like a weasel")
    lenS = len(target)
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")
    lenA = len(alphabet)
    epoch = 0
    bestStr = generate(lenS, lenA, alphabet)
    bestScore = calcScore(bestStr, target)
    print("String Score")
    while bestScore < 100:
        if bestScore == 100:
            break
        newStr = generate(lenS, lenA, alphabet)
        newScore = calcScore(newStr, target)
        if newScore > bestScore:
            bestScore = newScore
            bestStr = newStr
        if epoch == 100000:
            print("%s %d" % ("".join(bestStr), bestScore))
            epoch = 0
        epoch = epoch + 1