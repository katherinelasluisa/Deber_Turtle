#ESTRELLA DE n PUNTAS

import turtle
t= turtle.Pen()
n= int(input('ingrese un numero'))
for x in range (1,n+1):
	t.forward(100)
	t.left(360/2 + (180/n))
turtle.getscreen()._root.mainloop()