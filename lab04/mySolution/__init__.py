import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        if branchLen > 45 :
            t.pencolor("brown")
        elif branchLen > 15 :
            t.pencolor("green")
        else :
            t.pencolor("lightgreen")

        t.pendown()
        t.pensize(branchLen / 10)

        rand = random.randint(15, 45)
        t.forward(branchLen)
        t.right(rand)

        randLen = random.randint(5, 15)
        tree(branchLen - randLen, t)
        t.left(rand * 2)

        randLen = random.randint(5, 15)
        tree(branchLen - randLen, t)
        t.right(rand)

        t.penup()
        t.backward(branchLen)

def main() :
    t = turtle.Turtle()
    t._tracer(0)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(350)
    t.down()
    t.color("green")
    tree(120,t)
    myWin.exitonclick()

def power(x, n, acc = 1) :
    if n == 0 :
        return acc
    elif n < 0 :
        return "Invalid input"
    else :
        acc *= x
        return power(x, n - 1, acc)

def powerH(x ,n) :
    if n < 0 :
        return "Invalid input"
    elif n == 1 :
        return x
    elif n == 0 :
        return 1
    else :
        div = int(n / 2)
        mod = int(n % 2)
        return powerH(x, div) * powerH(x, div) * powerH(x, mod)

def bCoefficient(n, k) :
    if k > n or k < 0:
        return "Invalid input"
    elif k == 0 or k == n:
        return 1
    else :
        return bCoefficient(n - 1, k) + bCoefficient(n - 1, k - 1)