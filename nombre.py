import turtle
import os
win=turtle.Screen()
win.bgcolor("pink")
t = turtle.Pen()
t.reset()
t.color(1,0,0)
t.begin_fill()

t.forward(25)
t.left(90)

t.forward(40)
t.left(-160)

t.forward(40)
t.left(70)

t.forward(25)
t.right(40)

t.left(160)
t.forward(80)

t.right(70)
t.forward(80)

t.left(130)
t.forward(25)

t.right(-60)
t.forward(50)

t.right(155)
t.forward(50)


t.left(100)
t.forward(40)

t.left(90)
t.forward(140)

turtle.getscreen()._root.mainloop()