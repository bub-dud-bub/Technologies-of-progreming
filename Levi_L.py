import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(-100, 0)
turtle.pendown()

axiom, tempAx, paste, i = 'F', '', '-F++F-', 16

for i in range(i):
    for j in axiom:
        if j == 'F':
            tempAx += paste
        else:
            tempAx += j
    axiom, tempAx = tempAx, ''

for k in axiom:
    if k == '+':
        turtle.right(45)
    elif k == '-':
        turtle.left(45)
    else:
        turtle.forward(1)

turtle.update()
turtle.mainloop()
