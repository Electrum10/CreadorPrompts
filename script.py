import tkinter as tk
from tkinter import *
from tkinter.font import Font
import pyperclip

#Fondo
Fondo = "#9b9b9b"


#Configuración básica
ventana = Tk()
ventana.geometry("600x600")
ventana.title("Automatizador de prompts")
ventana.configure(background = Fondo)

#Función para el botón de características
def Características():
    R = Cámara.get()
    RR = f"Actua como un experto en fotografia. Dime la Resolució/ISO, el Sensor, el Estabilitzador, el Video, la Conectivitat, el Visor, las dimensiones i Peso, la Bateria i la Resistencia de la cámara " + R
    print(RR)
    pyperclip.copy(RR)

#Función para el botón de atributos
def Atributos():
    R = Cámara.get()
    RS = f"Actua como un experto en fotografia. Dime los siguientes atributos de la cámara " + R + ": Precio, Empuñadura, Facilidad de uso i portabilidad"
    print(RS)
    pyperclip.copy(RS)

#Fuentes
FuenteTitulo = Font(family = "Montserrat", size = 27, weight = "bold")
FuenteBotón = Font(family = "Montserrat", size = 16, weight = "bold")
FuenteCámara = Font(family = "Montserrat", size = 10, weight = "bold")
FuenteTexto = Font(family = "Montserrat", size = 15, weight = "bold")

#Titulo
Titulo = tk.Label(ventana, font=FuenteTitulo, text="Automatizador de prompts", background = Fondo)
Titulo.place(x=70, y=50)

#Entrada para poner la cámara
Cámara = tk.Entry(ventana, width = 30, font = FuenteCámara)
Cámara.place(x = 180, y = 150)

#Titulo para saber donde poner la camara
CámaraTitulo = tk.Label(ventana, font=FuenteTexto, text="Cámara:", background = Fondo)
CámaraTitulo.place(x = 250, y = 115)

#Botón para las características
CatacteristicasBotón = tk.Button(ventana, text = "Caracteristicas", background = "blue", width = 20, height = 3, font= FuenteBotón, command= Características)
CatacteristicasBotón.place(x = 150, y = 200)

AtributosBotón = tk.Button(ventana, text = "Atributos", background = "pink", width = 20, height = 3, font= FuenteBotón, command= Características)
AtributosBotón.place(x = 150, y = 320)

ProsContrasBotón = tk.Button(ventana, text = "Pros/contras", background = "yellow", width = 20, height = 3, font= FuenteBotón, command= Características)
ProsContrasBotón.place(x = 150, y = 450)


#Mainloop :)
ventana.mainloop()