import turtle
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
pen = turtle.Pen()
turtle.bgcolor("black")
for i in range (360):
    pen.pencolor(colors[i%6])
    pen.width(i/100+1)
    pen.forward(i)
    pen.left(59)
    