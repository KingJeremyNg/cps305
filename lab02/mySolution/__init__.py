import matplotlib.pyplot as plot
import timeit
import random

def getUpdate() :
    timeGet = []
    timeUpdate = []
    number = []
    size = 1000000

    for i in range(size) :
        dic = {x: None for x in range(i)}
        rand = random.randrange(size)

        if i % 10000 :
            timeGet.append(timeit.Timer("dic[%d]" % i,"from __main__ import dic"))
            timeUpdate.append(timeit.Timer("dic[%d] = random.randrange(size)" % i,"from __main__ import random, dic"))
            number.append(i)

    plot.scatter(number, timeGet)
    plot.scatter(number, timeUpdate)
    plot.xlabel("Size")
    plot.ylabel("Time")
    plot.show()

def delete() :
    ok = 0