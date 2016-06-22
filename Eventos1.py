#POLIGONO 2
#eventos de teclado
from tkinter import*
tk= Tk()
tk.title("EVENTO 1")
canvas= Canvas(tk, width=400, height=200) # EL PRIMER PARAMETRO DE CANVAS.MOVE ES EL IDENTIFICADOR DE LA FIGURA DIBUJADA
canvas.pack() # EL SEGUNDO PARAMETRO ES EL VALOR DE X
canvas.create_polygon(150,120, 90,160,100,90)

def moverpoligono1(event):
	if event.keysym=='Up':
		canvas.move(1,0,-3)
	elif event.keysym=='Down':
		canvas.move(1,0,3)
	elif event.keysym=='Left':
		canvas.move(1,3,0)
	else:
		canvas.move(1,3,0)

canvas.bind_all('<KeyPress-Up>',moverpoligono1)
canvas.bind_all('<KeyPress-Down>',moverpoligono1)
canvas.bind_all('<KeyPress-Left>',moverpoligono1)
canvas.bind_all('<KeyPress-Right>',moverpoligono1)
tk.mainloop()
