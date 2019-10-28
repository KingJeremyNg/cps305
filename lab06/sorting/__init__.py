import matplotlib.pyplot as plot
import timeit
import random


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def mo3_quickSort(alist):
    mo3_quickSortHelper(alist, 0, len(alist) - 1)


def mo3_quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = mo3_partition(alist, first, last)

        mo3_quickSortHelper(alist, first, splitpoint - 1)
        mo3_quickSortHelper(alist, splitpoint + 1, last)


def mo3_partition(alist, first, last):

    array = [alist[first], alist[len(alist) // 2], alist[last]]
    
    if (array[1] > array[0] and array[1] < array[2]) or (array[1] > array[2] and array[1] < array[0]):
        alist[first] = array[1]
        alist[((last - first) // 2 + first)] = array[0]
        pivotvalue = array[1]

    elif (array[2] > array[0] and array[2] < array[1]) or (array[2] > array[1] and array[2] < array[0]):
        alist[first] = array[2]
        alist[last] = array[0]
        pivotvalue = array[2]
    else:
        pivotvalue = array[0]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
