# -*- coding: cp1251 -*-
import matplotlib.pyplot as plt
import matplotlib.backend_bases


def onMouseClick(event: matplotlib.backend_bases.MouseEvent) -> None:
    







x = [0,0,0,0,0]
y = [10,30,50,70,90]
plt.plot(x,y, color='Blue', marker='o', markersize='6')
x = [100,100,100,100,100]
y = [10,30,50,70,90]
plt.plot(x,y, color='Blue', marker='o', markersize='6')

x = [10,30,50,70,90]
y = [0,0,0,0,0]
plt.plot(x,y, color='Red', marker='o', markersize='6')
x = [10,30,50,70,90]
y = [100,100,100,100,100]
plt.plot(x,y, color='Red', marker='o', markersize='6')
x, y = 20, 10
while y<=90:
    x = 20
    while x<=80:
        plt.plot(x,y, color='Blue', marker='o', markersize='6')
        x+=20
    y+=20

x, y = 10, 20
while x<=90:
    y = 20
    while y<=80:
        plt.plot(x,y, color='Red', marker='o', markersize='6')
        y+=20
    x+=20
plt.show()