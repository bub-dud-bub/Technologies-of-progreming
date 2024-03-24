import turtle
import wx
import time
x = [0, 100, 200]
y = [0, 100, 0]
turtle.pendown()
turtle.goto(100,100)
turtle.goto(200,0)
turtle.speed(0)
for i in range(10):
    turtle.clear()
    n = 0
    p = 1
    while n < (len(x)-1):
        if (x[n]==x[p]) and (y[n]<y[p]): #N
            x.insert(n+1, x[n]-(y[n+1]-y[n])/2)
            y.insert(n+1, y[n]+(y[n+1]-y[n])/2)
        elif (x[n]==x[p]) and (y[n]>y[p]): #S
            x.insert(n+1, x[n]+(y[n]-y[n+1])/2)
            y.insert(n+1, y[n]-(y[n]-y[n+1])/2)
        elif (x[n]<x[p]) and (y[n]==y[p]): #E
            x.insert(n+1, x[n]+(x[n+1]-x[n])/2)
            y.insert(n+1, y[n]+(x[n+1]-x[n]))
        elif (x[n]>x[p]) and (y[n]==y[p]): #W
            x.insert(n+1, x[n]-(x[n]-x[n+1])/2)
            y.insert(n+1, y[n]-(x[n]-x[n+1]))
        elif (x[n]<x[p]) and (y[n]<y[p]): #NE
            x.insert(n+1, x[n])
            y.insert(n+1, y[n+1])
        elif (x[n]<x[p]) and (y[n]>y[p]): #SE
            x.insert(n+1, x[n+1])
            y.insert(n+1, y[n])
        elif (x[n]>x[p]) and (y[n]>y[p]): #SW
            x.insert(n+1, x[n])
            y.insert(n+1, y[n+1])
        elif (x[n]>x[p]) and (y[n]<y[p]): #NW
            x.insert(n+1, x[n+1])
            y.insert(n+1, y[n])
        n+=2
        p+=2
    turtle.penup()
    for c in range(len(x)):
        turtle.goto(x[c], y[c])
        if c==0:
            turtle.pendown()
    i+=1
turtle.exitonclick()
