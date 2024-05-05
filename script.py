import tkinter as tk
from tkinter import *
from tkinter.font import Font

#Fondo
Fondo = "#9b9b9b"


#Configuración básica
ventana = Tk()
ventana.geometry("600x600")
ventana.title("Automatizador de prompts")
ventana.configure(background = Fondo)




#Fuentes
FuenteTitulo = Font(family = "Montserrat", size = 27, weight = "bold")



#Titulo
Titulo = tk.Label(ventana, font=FuenteTitulo, text="Automatizador de prompts", background = Fondo)
Titulo.place(x=70, y=50)



ventana.mainloop()