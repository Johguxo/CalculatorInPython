from tkinter import*
from PIL import Image
from PIL import ImageTk
from tkinter import font

bsuma = 1 ; bmul = 1 ; bdiv = 1 ; bresta = 1
op = 0 ; m = 0
suma = 0 ; mul = 1 ; div = 1 ; resta = 0 ; raiz = 1
def Boton1():
	pantalla.insert(END,"1")
	pantalla.get()
def Boton2():
	pantalla.insert(END,"2")
	pantalla.get()
def Boton3():
	pantalla.insert(END,"3")
	pantalla.get()
def Boton4():
	pantalla.insert(END,"4")
	pantalla.get()
def Boton5():
	pantalla.insert(END,"5")
	pantalla.get()
def Boton6():
	pantalla.insert(END,"6")
	pantalla.get()
def Boton7():
	pantalla.insert(END,"7")
	pantalla.get()
def Boton8():
	pantalla.insert(END,"8")
	pantalla.get()
def Boton9():
	pantalla.insert(END,"9")
	pantalla.get()
def Boton0():
	pantalla.insert(END,"0")
	pantalla.get()
def Punto():
	pantalla.insert(END,".")
	pantalla.get()
def Suma():
	global suma, op , bsuma
	if bsuma == 1:
		suma = float(pantalla.get())
		pantalla.delete(0,END)
		bsuma = 0
	else:
		suma = suma + float(pantalla.get())
		pantalla.delete(0,END)
	op = 1
def Mul():
	global mul , op , bmul
	if bmul == 1:
		mul = float(pantalla.get())
		pantalla.delete(0,END)
		bmul = 0
	else:
		mul = mul * float(pantalla.get())
		pantalla.delete(0,END)
	op = 2
def Div():
	global div, op , bdiv
	if bdiv == 1:
		div = float(pantalla.get())
		pantalla.delete(0,END)
		bdiv = 0
	else:
		div = div / float(pantalla.get())
		pantalla.delete(0,END)
	op = 3
def Resta():
	global resta, op , bresta
	if bresta == 1:
		resta = float(pantalla.get())
		pantalla.delete(0,END)
		bresta = 0
	else:
		resta = resta - float(pantalla.get())
		pantalla.delete(0,END)
	op = 4
def Raiz():
	global raiz
	raiz = float(pantalla.get())**(1/2)
	pantalla.delete(0,END)
	pantalla.insert(END,raiz)
def Igual():
	global suma , mul , div, resta, op, bsuma , bmul , bdiv , bresta
	if op == 1:
		suma = suma + float(pantalla.get())
		pantalla.delete(0,END)
		pantalla.insert(END,suma)
		bsuma = 1
	if op == 2:
		mul = mul * float(pantalla.get())
		pantalla.delete(0,END)
		pantalla.insert(END,mul)
		bmul = 1
	if op == 3:
		div = div / float(pantalla.get())
		pantalla.delete(0,END)
		pantalla.insert(END,div)
		bdiv = 1
	if op == 4:
		resta = resta - float(pantalla.get())
		pantalla.delete(0,END)
		pantalla.insert(END,resta)
		bresta = 1

def Mrestar():
	global m
	m = m - float(pantalla.get())
def Msumar():
	global m
	m = m + float(pantalla.get())
def MR():
	global m
	pantalla.delete(0,END)
	pantalla.insert(END,m)
def MC():
	global m
	m = 0
def Borrar():
	global suma , mul
	pantalla.delete(0,END)
	pantalla.get()
	suma = 0
	mul = 1
	resta = 0
	div = 1
def Off():
	ventana.destroy()

ventana = Tk()
ventana.title("Calculadora")
ventana.config(bg="#013D93")
ventana.geometry("235x260")

futura = font.Font(family = "Comic Sans MS", size = 8, weight="bold")
negrita = font.Font(size = 8 , weight="bold")

img1=PhotoImage(file="casio.gif")
img2 = img1.subsample(8, 8) 
casio = Label(ventana, image=img2)

pantalla = Entry(ventana, width = 36)

boton1 = Button(ventana,text = "1", command = Boton1,background = "#99FFFF",width = 5 , height=1)
boton2 = Button(ventana,text = "2", command = Boton2,background = "#99FFFF",width = 5,height=1)
boton3 = Button(ventana,text = "3", command = Boton3,background = "#99FFFF",width = 5,height=1)
boton4 = Button(ventana,text = "4", command = Boton4,background = "#99FFFF",width = 5,height=1)
boton5 = Button(ventana,text = "5", command = Boton5,background = "#99FFFF",width = 5,height=1)
boton6 = Button(ventana,text = "6", command = Boton6,background = "#99FFFF",width = 5,height=1)
boton7 = Button(ventana,text = "7", command = Boton7,background = "#99FFFF",width = 5,height=1)
boton8 = Button(ventana,text = "8", command = Boton8,background = "#99FFFF",width = 5,height=1)
boton9 = Button(ventana,text = "9", command = Boton9,background = "#99FFFF",width = 5,height=1)
boton0 = Button(ventana,text = "0", command = Boton0,background = "#99FFFF",width = 5,height=1)

botonSuma = Button(ventana,text = "+", command = Suma,background = "#9900FF",width = 5,height=3)
botonMul = Button(ventana,text = "X", command = Mul,background = "#9900FF",width = 5,height=1)
botonDiv = Button(ventana,text = "/", command = Div,background = "#9900FF",width = 5,height=1)
botonResta = Button(ventana,text = "-", command = Resta,background = "#9900FF",width = 5,height=1)
botonRaiz = Button(ventana,text = "√", command = Raiz,background = "#9900FF",width = 5,height=1)
botonIgual = Button(ventana,text = "=", command = Igual,background = "#9900FF",width = 5,height=1)
botonMrestar = Button(ventana,text = "M-", command = Mrestar,background = "#C6C770",width = 5,height=1)
botonMsumar = Button(ventana,text = "M+", command = Msumar,background = "#C6C770",width = 5,height=1)
botonMR = Button(ventana,text = "MR", command = MR,background = "#C6C770",width = 5,height = 1)
botonMC = Button(ventana,text = "MC", command = MC,background = "#C6C770",width = 5,height = 1)
botonC = Button(ventana,text = "ON/C",font = negrita ,command = Borrar,background = "#FF6600",borderwidth = 4 , width = 5,height=3)
botonOff = Button(ventana,text = "OFF",font = negrita ,command = Off,background = "#FF6600",borderwidth = 4 , width = 5 ,height=1)
botonPunto = Button(ventana,text = ".", command = Punto,background = "#99FFFF",width = 5 , height=1)
etiqueta = Label(ventana,text = "Hecho por: Johguxo" , font = futura)


casio.grid(padx=5, pady=5,row = 0 , column = 0, columnspan = 5)
pantalla.grid(padx=2, pady=2,row = 1 ,column = 0 , columnspan = 5)
botonOff.grid(padx=1, pady=1,row = 2 ,column = 0)
botonMR.grid(padx=1, pady=1,row = 2 ,column = 1)
botonMC.grid(padx=1, pady=1,row = 2 ,column = 2)
botonMsumar.grid(padx=1, pady=1,row = 2 ,column = 3)
botonMrestar.grid(padx = 1 , pady = 1 , row = 2 ,column = 4)
botonDiv.grid(padx = 1 , pady = 1 , row = 3 ,column = 0)
boton7.grid(padx = 1 , pady = 1 , row = 3 ,column = 1)
boton8.grid(padx = 1 , pady = 1 , row = 3 ,column = 2)
boton9.grid(padx = 1 , pady = 1 , row = 3 ,column = 3)
botonMul.grid(padx = 1 , pady = 1 , row = 3 ,column = 4)
botonRaiz.grid(padx = 1 , pady = 1 , row = 4 ,column = 0)
boton4.grid(padx = 1 , pady = 1 , row = 4 ,column = 1)
boton5.grid(padx = 1 , pady = 1 , row = 4 ,column = 2)
boton6.grid(padx = 1 , pady = 1 , row = 4 ,column = 3)
botonResta.grid(padx = 1 , pady = 1 , row = 4 ,column = 4)
botonC.grid(padx = 1 , pady = 1 , row = 5 ,column = 0 , rowspan = 2)
boton1.grid(padx = 1 , pady = 1 , row = 5 ,column = 1)
boton2.grid(padx = 1 , pady = 1 , row = 5 ,column = 2)
boton3.grid(padx = 1 , pady = 1 , row = 5 ,column = 3)
botonSuma.grid(padx = 1 , pady = 1 , row = 5 ,column = 4 , rowspan = 2)
boton0.grid(padx = 1 , pady = 1 , row = 6 ,column = 1)
botonPunto.grid(padx = 1 , pady = 1 , row = 6 ,column = 2)
botonIgual.grid(padx = 1 , pady = 1 , row = 6 ,column = 3)
etiqueta.grid(padx = 1, pady = 2 , row = 7 ,column = 0,columnspan = 5)

ventana.mainloop()
