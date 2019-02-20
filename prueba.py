from tkinter import*

op = 1
terminasuma = 1
def Boton1():
	global terminasuma
	if terminasuma == 1:
		pantalla.delete(0,END)
		pantalla.insert(END,"1")
		pantalla.get()
		terminasuma = 0
	else :
		pantalla.insert(END,"1")
		pantalla.get()
def Boton2():
	global terminasuma
	if terminasuma == 1:
		pantalla.delete(0,END)
		pantalla.insert(END,"2")
		pantalla.get()
		terminasuma = 0
	else :
		pantalla.insert(END,"2")
		pantalla.get()
def Boton3():
	global terminasuma
	if terminasuma == 1:
		pantalla.delete(0,END)
		pantalla.insert(END,"3")
		pantalla.get()
		terminasuma = 0
	else :
		pantalla.insert(END,"3")
		pantalla.get()
def borrar():
	pantalla.delete(0,END)
	pantalla.get()
def Suma():
	global terminasuma, op,a,b
	if op == 1: 
		a = pantalla.get()
		pantalla.delete(0,END)
		op = 0
	else :	
		b = pantalla.get()
		pantalla.delete(0,END)
		suma = int(a) + int(b)
		pantalla.insert(END,suma)
		terminasuma = 1
		op = 1
	

ventana = Tk()
ventana.title("Calculadora")

pantalla = Entry(ventana)
boton1 = Button(ventana,text = "1", command = Boton1,background = "white",width = 1,height=1)
boton2 = Button(ventana,text = "2", command = Boton2,background = "white",width = 1,height=1)
boton3 = Button(ventana,text = "3", command = Boton3,background = "white",width = 1,height=1)
botonSuma = Button(ventana,text = "+", command = Suma,background = "white",width = 1,height=1)
botonC = Button(ventana,text = "C", command = borrar,background = "white",width = 1,height=1)
etiqueta = Label(ventana,text = "Johguxo")


pantalla.pack()
boton1.pack()
boton2.pack()
boton3.pack()
botonC.pack()
botonSuma.pack()
etiqueta.pack()

ventana.mainloop()
