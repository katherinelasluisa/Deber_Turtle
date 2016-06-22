#POLIGONO 2
#eventos de teclado
from tkinter import*
tk= Tk()
tk.title("EVENTO 3")
canvas= Canvas(tk, width=400, height=200) # EL PRIMER PARAMETRO DE CANVAS.MOVE ES EL IDENTIFICADOR DE LA FIGURA DIBUJADA
canvas.pack() # EL SEGUNDO PARAMETRO ES EL VALOR DE X
canvas.create_polygon(70,60, 40,60,30,20)

def moverpoligono3(event):
	if event.keysym=='Up':
		canvas.move(1,0,-3)
	elif event.keysym=='Down':
		canvas.move(1,0,3)
	elif event.keysym=='Left':
		canvas.move(1,3,0)
	else:
		canvas.move(1,3,0)

canvas.bind_all('<KeyPress-Up>',moverpoligono3)
canvas.bind_all('<KeyPress-Down>',moverpoligono3)
canvas.bind_all('<KeyPress-Left>',moverpoligono3)
canvas.bind_all('<KeyPress-Right>',moverpoligono3)
tk.mainloop()
