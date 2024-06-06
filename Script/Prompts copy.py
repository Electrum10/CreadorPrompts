import tkinter as tk
from tkinter import *
from tkinter.font import Font
import pyperclip
from tkinter import messagebox

def Fotografia():
    ventana_fotografia = tk.Frame(ventana, bg= "lightblue", bd=2, relief="raised")
    ventana_fotografia.place(x=10, y=10, width=580, height=580)
    Fondo = "#9b9b9b"
    
    #Función para el botón de características
    def Características():
        R = Objeto.get()
        RR = f"Actúa como un experto en fotografía. Dime la Resolución/ISO, el Sensor, los puntos d'enfoque, el estabilizador, el Video, la conectividad, el Visor, las dimensiones i Peso, la Batería (mAh) i la Resistencia de la cámara. " + R + ". En español"
        print(RR)
        pyperclip.copy(RR)

    #Función para el botón de atributos
    def Atributos():
        R = Objeto.get()
        RS = f"Actúa como un experto en fotografía. Dime los siguientes atributos de la cámara " + R + ": Precio, Empuñadura, Facilidad de uso i portabilidad. Español"
        print(RS)
        pyperclip.copy(RS)


    def ProsContras():
        R = Objeto.get()
        RS = f"Actúa como un experto en fotografía. Dime los pros y los contras de la cámara" + R + ", pero haz unos pros y contras que demuestren tanto lo bueno como lo malo de la cámara. Español"
        print(RS)
        pyperclip.copy(RS)

    #Fuentes
    FuenteBotón = Font(family = "Montserrat", size = 16, weight = "bold")
    FuenteCámara = Font(family = "Montserrat", size = 10, weight = "bold")
    FuenteTexto = Font(family = "Montserrat", size = 15, weight = "bold")

    #Entrada para poner la cámara
    Objeto = tk.Entry(ventana_fotografia, width = 30, font = FuenteCámara).place(x = 180, y = 150)

    #Titulo para saber donde poner la Camara
    CámaraTitulo = tk.Label(ventana_fotografia, font=FuenteTexto, text="Cámara:", background = "lightblue").place(x = 250, y = 115)

    #Botón para las características
    CaracterísticasBotón = tk.Button(ventana_fotografia, text = "Características", background = "blue", width = 20, height = 3, font= FuenteBotón, command= Características).place(x = 150, y = 200)
    AtributosBotón = tk.Button(ventana_fotografia, text = "Atributos", background = "pink", width = 20, height = 3, font= FuenteBotón, command= Atributos).place(x = 150, y = 320)
    ProsContrasBotón = tk.Button(ventana_fotografia, text = "Pros/contras", background = "yellow", width = 20, height = 3, font= FuenteBotón, command= ProsContras).place(x = 150, y = 450)
    CerrarMenuFotos = tk.Button(ventana_fotografia, text= "Cerrar", command=ventana_fotografia.destroy).place(x=470, y=300)


#Configuración básica de la ventana principal
ventana = Tk()
ventana.geometry("600x600")
ventana.title("Automatizador de prompts")
ventana.configure(background = "#9b9b9b")

#Variables básicas
FuenteTitulo = Font(family = "Montserrat", size = 27, weight = "bold")
FuenteContexto = Font(family = "Montserrat", size = 9, weight = "bold")
Fondo = "#9b9b9b"

#Declaramos menú
menu = tk.Menu(ventana)
ventana.config(menu=menu)
#Configuramos categoría de menú
NichoMenu = tk.Menu(menu, tearoff=False)
NichoMenu.add_command(label= "Cámaras")
NichoMenu.add_command(label= "Objetivos")
NichoMenu.add_separator()
NichoMenu.add_command(label= "Sillas Gamers")
NichoMenu.add_command(label= "Ratones Gamers")
NichoMenu.add_command(label= "Teclados Gamers")
AcercaDeMenu = tk.Menu(menu, tearoff=0)
AcercaDeMenu.add_command(label="si")
#Asignamos menú
menu.add_cascade(label="Nicho", menu=NichoMenu)
menu.add_cascade(label= "Creador", menu=AcercaDeMenu)

#Titulo y contexto
Titulo = tk.Label(ventana, font=FuenteTitulo, text="Automatizador de prompts", background = Fondo)
Titulo.place(x=70, y=30)
Contexto = tk.Label(ventana, text="Pequeño programa para acelerar mis prompts para mi pagina web", font = FuenteContexto, background=Fondo).place(x = 120, y = 83)

#Botones para abrir las ventanas
BotónAbrirFotos = tk.Button(ventana, text = "Fotos", command=Fotografia).place(x=200, y=200)



#Mainloop ;-)
ventana.mainloop()