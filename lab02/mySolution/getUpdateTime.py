import matplotlib.pyplot as plot
import timeit
import random

timeGet = []
timeUpdate = []
count = []
size = 1000000
for i in range(0, size, 50000) :
    dic = {x: None for x in range(i)}
    rand = random.randint(0, i)

    timerGet = timeit.Timer("dic.get(rand)" ,"from __main__ import dic, rand")
    timerUpdate = timeit.Timer("dic.update({rand: 1})" ,"from __main__ import dic, rand")

    timeGet.append(timerGet.timeit(number = 100))
    timeUpdate.append(timerUpdate.timeit(number = 100))
    count.append(i)

plot.scatter(count, timeGet, color = 'r', marker = '+')
plot.scatter(count, timeUpdate, color = 'b', marker = '+')
plot.xlabel("Size")
plot.ylabel("Time")
plot.show()