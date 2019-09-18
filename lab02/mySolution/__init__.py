import matplotlib.pyplot as plot
import timeit
import random

def getUpdateTime() :
    timeGet = []
    timeUpdate = []
    count = []
    size = 10000

    for i in range(1, size) :
        dic = {x: random.randrange(size) for x in range(i)}

        if i % 100 == 0:
            timeGet.append(timeit.Timer("dic.get('x')"))
            timeUpdate.append(timeit.Timer("dic.update(%d, random.randrange(size))" % i ,"from __main__ import random"))
            count.append(i)

    plot.scatter(count, timeGet, color = 'r', marker = '+')
    plot.scatter(count, timeUpdate, color = 'b', marker = '+')
    plot.xlabel("Size")
    plot.ylabel("Time")
    plot.show()

def deleteTime() :
    ok = 0

getUpdateTime()