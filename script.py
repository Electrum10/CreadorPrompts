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
FuenteBotón = Font(family = "Montserrat", size = 16, weight = "bold")
FuenteCámara = Font(family = "Montserrat", size = 10, weight = "bold")
FuenteTexto = Font(family = "Montserrat", size = 15, weight = "bold")

#Titulo
Titulo = tk.Label(ventana, font=FuenteTitulo, text="Automatizador de prompts", background = Fondo)
Titulo.place(x=70, y=50)

Cámara = tk.Entry(ventana, width = 30, font = FuenteCámara)
Cámara.place(x = 180, y = 150)

CámaraTitulo = tk.Label(ventana, font=FuenteTexto, text="Cámara:", background = Fondo)
CámaraTitulo.place(x = 250, y = 115)

Catacteristicas = tk.Button(ventana, text = "Caracteristicas", background = "blue", width = 20, height = 3, font= FuenteBotón)
Catacteristicas.place(x = 150, y = 200)



ventana.mainloop()