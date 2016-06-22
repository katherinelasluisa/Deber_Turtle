import time
from tkinter import*
t= Tk()
t.title("RELOJ")

cuadro = Frame(t, height=180, width=200) # Creamos un frame en nuestro contenedor ventana
cuadro.pack(padx=10, pady=10)

x=1

def contador():
	label1 = Label (cuadro, text="RELOJ EN PYTHON").place(x=0, y=0)
	t = time.localtime()
	hora=t[3]
	minuto =t[4]
	segundo = t[5]
	label2 = Label (cuadro, text=str(hora)).place(x=0, y=20)
	label3 = Label (cuadro, text=":").place(x=20, y=20)
	label4 = Label (cuadro, text=str(minuto)).place(x=30, y=20)
	label5 = Label (cuadro, text=":").place(x=50, y=20)
	label6 = Label (cuadro, text=str(segundo)).place(x=60, y=20)
	
while x == 1:
	contador()
	t.update()
t.mainloop()