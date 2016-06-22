#EVENTO 2
#eventos de teclado
from tkinter import*
tk= Tk()
tk.title("EVENTO 2")
canvas= Canvas(tk, width=400, height=200) # EL PRIMER PARAMETRO DE CANVAS.MOVE ES EL IDENTIFICADOR DE LA FIGURA DIBUJADA
canvas.pack() # EL SEGUNDO PARAMETRO ES EL VALOR DE X
canvas.create_polygon(70,80, 10,130,120,90) # EL TERCER PARAMETRO ES EL VALOR DE Y

def moverpoligono2(event):
	if event.keysym=='Up':
		canvas.move(1,0,-3)
	elif event.keysym=='Down':
		canvas.move(1,0,3)
	elif event.keysym=='Left':
		canvas.move(1,3,0)
	else:
		canvas.move(1,3,0)

canvas.bind_all('<KeyPress-Up>',moverpoligono2)
canvas.bind_all('<KeyPress-Down>',moverpoligono2)
canvas.bind_all('<KeyPress-Left>',moverpoligono2)
canvas.bind_all('<KeyPress-Right>',moverpoligono2)
tk.mainloop()
