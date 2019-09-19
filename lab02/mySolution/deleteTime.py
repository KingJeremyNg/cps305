import matplotlib.pyplot as plot
import timeit
import random

timeDeleteDict = []
timeDeleteList = []
count = []
size = 2000000

for i in range(10000, size, 50000) :
    rand = random.randint(0, i)
    dic = {x: random.randint(0, i) for x in range(i)}
    lis = [x for x in range(i)]
    keys = list(dic.keys())

    dictTimer = timeit.Timer("del dic[keys[random.randint(0, len(keys) - 1)]]", "from __main__ import dic, keys, random")
    listTimer = timeit.Timer("del lis[random.randint(0, i)]", "from __main__ import lis, random, i")
    
    timeDeleteDict.append(dictTimer.timeit(number = 10))
    timeDeleteList.append(listTimer.timeit(number = 10))
    count.append(i)

plot.scatter(count, timeDeleteDict, color = 'r', marker = '+')
plot.scatter(count, timeDeleteList, color = 'b', marker = '+')
plot.xlabel("Size")
plot.ylabel("Time")
plot.show()