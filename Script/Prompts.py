import tkinter as tk
from tkinter import *
from tkinter.font import Font
import pyperclip
from tkinter import messagebox
import webbrowser

def Créditos():
    webbrowser.open("https://github.com/Electrum10")

def gaming():
    webbrowser.open("https://60hercios.com/")
    
def OberturaVisual():
    webbrowser.open("https://oberturavisual.com/")

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
    FuenteTexto = Font(family = "Montserrat", size = 40, weight = "bold")
    FuenteSubtexto = Font(family = "Montserrat", size = 13, weight = "normal")
    FuenteCerrar = Font(family = "Montserrat", size = 9, weight = "bold")

    #Entrada para poner la cámara
    Objeto = tk.Entry(ventana_fotografia, width = 30, font = FuenteCámara)
    Objeto.place(x = 180, y = 150)

    #Titulo para saber donde poner la Camara
    CámaraTitulo = tk.Label(ventana_fotografia, font=FuenteTexto, text="Cámaras", background = "lightblue").place(x = 180, y = 35)
    CámaraSubtitulo = tk.Label(ventana_fotografia, font=FuenteSubtexto, text="Pon la cámara con la que quieras hacer una reseña:", background = "lightblue").place(x = 104, y = 108)

    #Botón para las características
    CaracterísticasBotón = tk.Button(ventana_fotografia, text = "Características", background = "blue", width = 20, height = 3, font= FuenteBotón, command= Características).place(x = 150, y = 200)
    AtributosBotón = tk.Button(ventana_fotografia, text = "Atributos", background = "pink", width = 20, height = 3, font= FuenteBotón, command= Atributos).place(x = 150, y = 320)
    ProsContrasBotón = tk.Button(ventana_fotografia, text = "Pros/contras", background = "yellow", width = 20, height = 3, font= FuenteBotón, command= ProsContras).place(x = 150, y = 450)
    CerrarMenuFotos = tk.Button(ventana_fotografia, text= "Cerrar", command=ventana_fotografia.destroy, font=FuenteCerrar,width = 10, height = 3).place(x=470, y=300)

def Editores():
    ventana_editores = tk.Frame(ventana, bg= "lightblue", bd=2, relief="raised")
    ventana_editores.place(x=10, y=10, width=580, height=580)
    Fondo = "#9b9b9b"
    
    #Función para el botón de características
    def Características():
        R = Objeto.get()
        RR = f"Actúa como un experto en fotografía. Dime si se puede trabajar con capas, Si se pueden usar mascaras, si hay filtros y efectos, si se pueden editar las curvas y colores, si tiene IA, si se pueden editar fotos RAW, si soporta l'uso de presets y si tiene soporte para plugins de este editor de fotografías:  " + R + ". En catalán"
        print(RR)
        pyperclip.copy(RR)

    #Función para el botón de atributos
    def Atributos():
        R = Objeto.get()
        RS = f"Actúa como un experto en fotografía. Dime los siguientes atributos del editor de fotografia  " + R + ": Precio, Facilidad de uso y rendimiento/potencia. Hazlo en catalán"
        print(RS)
        pyperclip.copy(RS)


    def ProsContras():
        R = Objeto.get()
        RS = f"Actúa como un experto en fotografía. Dime los pros y los contras del editor de fotografías " + R + ", pero haz unos pros y contras que demuestren tanto lo bueno como lo malo del editor. Hazlo en catalán"
        print(RS)
        pyperclip.copy(RS)

    #Fuentes
    FuenteBotón = Font(family = "Montserrat", size = 16, weight = "bold")
    FuenteCámara = Font(family = "Montserrat", size = 10, weight = "bold")
    FuenteTexto = Font(family = "Montserrat", size = 40, weight = "bold")
    FuenteSubtexto = Font(family = "Montserrat", size = 13, weight = "normal")
    FuenteCerrar = Font(family = "Montserrat", size = 9, weight = "bold")

    #Entrada para poner la cámara
    Objeto = tk.Entry(ventana_editores, width = 30, font = FuenteCámara)
    Objeto.place(x = 180, y = 150)

    #Titulo para saber donde poner la Camara
    EditorTitulo = tk.Label(ventana_editores, font=FuenteTexto, text="Editores", background = "lightblue").place(x = 180, y = 35)
    EditorSubtitulo = tk.Label(ventana_editores, font=FuenteSubtexto, text="Pon el editor que quieras hacer una reseña:", background = "lightblue").place(x = 124, y = 108)

    #Botón para las características
    CaracterísticasBotón = tk.Button(ventana_editores, text = "Características", background = "blue", width = 20, height = 3, font= FuenteBotón, command= Características).place(x = 150, y = 200)
    AtributosBotón = tk.Button(ventana_editores, text = "Atributos", background = "pink", width = 20, height = 3, font= FuenteBotón, command= Atributos).place(x = 150, y = 320)
    ProsContrasBotón = tk.Button(ventana_editores, text = "Pros/contras", background = "yellow", width = 20, height = 3, font= FuenteBotón, command= ProsContras).place(x = 150, y = 450)
    CerrarMenuFotos = tk.Button(ventana_editores, text= "Cerrar", command=ventana_editores.destroy, font=FuenteCerrar,width = 10, height = 3).place(x=470, y=300)

def Objetivos():
    ventana_objetivos = tk.Frame(ventana, bg= "lightblue", bd=2, relief="raised")
    ventana_objetivos.place(x=10, y=10, width=580, height=580)
    Fondo = "#9b9b9b"
    
    #Función para el botón de características
    def Características():
        R = Objeto.get()
        RR = f"Actúa como un experto en fotografía. Dime si se puede trabajar con capas, Si se pueden usar mascaras, si hay filtros y efectos, si se pueden editar las curvas y colores, si tiene IA, si se pueden editar fotos RAW, si soporta l'uso de presets y si tiene soporte para plugins de este editor de fotografías:  " + R + ". En catalán"
        print(RR)
        pyperclip.copy(RR)

    #Función para el botón de atributos
    def Atributos():
        R = Objeto.get()
        RS = f"Actúa como un experto en fotografía. Dime los siguientes atributos del editor de fotografia  " + R + ": Precio, Facilidad de uso y rendimiento/potencia. Hazlo en catalán"
        print(RS)
        pyperclip.copy(RS)


    def ProsContras():
        R = Objeto.get()
        RS = f"Actúa como un experto en fotografía. Dime los pros y los contras del editor de fotografías " + R + ", pero haz unos pros y contras que demuestren tanto lo bueno como lo malo del editor. Hazlo en catalán"
        print(RS)
        pyperclip.copy(RS)

    #Fuentes
    FuenteBotón = Font(family = "Montserrat", size = 16, weight = "bold")
    FuenteCámara = Font(family = "Montserrat", size = 10, weight = "bold")
    FuenteTexto = Font(family = "Montserrat", size = 40, weight = "bold")
    FuenteSubtexto = Font(family = "Montserrat", size = 13, weight = "normal")
    FuenteCerrar = Font(family = "Montserrat", size = 9, weight = "bold")

    #Entrada para poner la cámara
    Objeto = tk.Entry(ventana_objetivos, width = 30, font = FuenteCámara)
    Objeto.place(x = 180, y = 150)

    #Titulo para saber donde poner la Camara
    EditorTitulo = tk.Label(ventana_objetivos, font=FuenteTexto, text="Editores", background = "lightblue").place(x = 180, y = 35)
    EditorSubtitulo = tk.Label(ventana_objetivos, font=FuenteSubtexto, text="Pon el editor que quieras hacer una reseña:", background = "lightblue").place(x = 124, y = 108)

    #Botón para las características
    CaracterísticasBotón = tk.Button(ventana_objetivos, text = "Características", background = "blue", width = 20, height = 3, font= FuenteBotón, command= Características).place(x = 150, y = 200)
    AtributosBotón = tk.Button(ventana_objetivos, text = "Atributos", background = "pink", width = 20, height = 3, font= FuenteBotón, command= Atributos).place(x = 150, y = 320)
    ProsContrasBotón = tk.Button(ventana_objetivos, text = "Pros/contras", background = "yellow", width = 20, height = 3, font= FuenteBotón, command= ProsContras).place(x = 150, y = 450)
    CerrarMenuFotos = tk.Button(ventana_objetivos, text= "Cerrar", command=ventana_objetivos.destroy, font=FuenteCerrar,width = 10, height = 3).place(x=470, y=300)

#Configuración básica de la ventana principal
ventana = Tk()
ventana.geometry("600x600")
ventana.title("Automatizador de prompts")
ventana.configure(background = "#9b9b9b")

#Variables básicas
FuenteTitulo = Font(family = "Montserrat", size = 27, weight = "bold")
FuenteContexto = Font(family = "Montserrat", size = 9, weight = "bold")
FuenteBotón = Font(family = "Montserrat", size = 14, weight = "bold")
FuenteSubmenú = Font(family = "Montserrat", size = 17, weight = "bold")
Fondo = "#9b9b9b"


#Declaramos menú
menu = tk.Menu(ventana)
ventana.config(menu=menu)
#Configuramos categoría de menú
NichoMenu = tk.Menu(menu, tearoff=False)
AcercaDeMenu = tk.Menu(menu, tearoff=0)
PaginasWebMenu = tk.Menu(menu, tearoff=False)
#Botones de menú
NichoMenu.add_command(label= "Cámaras", command=Fotografia)
NichoMenu.add_command(label= "Objetivos")
NichoMenu.add_separator()
NichoMenu.add_command(label= "Sillas Gamers")
NichoMenu.add_command(label= "Ratones Gamers")
NichoMenu.add_command(label= "Teclados Gamers")

AcercaDeMenu.add_command(label="GitHub", command=Créditos)

PaginasWebMenu.add_command(label="60Hercios (Gaming i Tecnología)", command=gaming)
PaginasWebMenu.add_command(label="OberturaVisual (Mundo de la fotografia)", command=OberturaVisual)

#Asignamos menú
menu.add_cascade(label="Nicho", menu=NichoMenu)
menu.add_cascade(label= "Creador", menu=AcercaDeMenu)
menu.add_cascade(label="Mis Paginas web", menu=PaginasWebMenu)


#Fondos
FondoFoto = Frame(ventana)
FondoFoto.place(x = 20, y = 110)
FondoFoto.config(bg="Lightblue", width=560,height=150, cursor="", relief="solid", bd=2)

#Titulo y contexto
Titulo = tk.Label(ventana, font=FuenteTitulo, text="Automatizador de prompts", background = Fondo).place(x=70, y=30)
Contexto = tk.Label(ventana, text="Pequeño programa para acelerar mis prompts para mi pagina web", font = FuenteContexto, background=Fondo).place(x = 120, y = 83)
FotografiaNicho = tk.Label(ventana, text="Fotografia", font=FuenteSubmenú, bg="lightblue").place(x=250, y = 120)
SetUpNicho = tk.Label(ventana, text="Gaming", font=FuenteSubmenú, bg=Fondo).place(x=255, y = 270)


#Botones para abrir las ventanas
BotónAbrirCamara = tk.Button(ventana, text = "Fotos", command=Fotografia, width = 10, height = 2, font = FuenteBotón)
BotónAbrirCamara.place(x=40, y=170)
BotónAbrirEditores = tk.Button(ventana, text = "Editores", command=Editores, width = 10, height = 2, font = FuenteBotón)
BotónAbrirEditores.place(x=230, y=170)
BotónAbrirObjetivos = tk.Button(ventana, text = "Objetivos", command=Objetivos, width = 10, height = 2, font = FuenteBotón)
BotónAbrirObjetivos.place(x=420, y=170)
BotónAbrirSillas= tk.Button(ventana, text = "Sillas", width = 10, height = 2, font = FuenteBotón)
BotónAbrirSillas.place(x=40, y=300)

#Mainloop ;-)
ventana.mainloop()