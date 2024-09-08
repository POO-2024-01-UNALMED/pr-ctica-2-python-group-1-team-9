import os
import tkinter as tk
from PIL import Image, ImageTk
#------------------------------------------------------------------------
# Variables para la logica en el manejo de las fotos
fotoP61 = None
fotoP62 = None
fotoP63 = None
fotoP64 = None
fotoP4 = None

imagenRedimensionadaP61 = None
imagenRedimensionadaP62 = None
imagenRedimensionadaP63 = None
imagenRedimensionadaP64 = None
imagenRedimensionadaP4 = None

imagenTkP61 = None
imagenTkP62 = None
imagenTkP63 = None
imagenTkP64 = None
imagenTkP4 = None

booleanaP61 = True
booleanaP62 = True
booleanaP63 = True
booleanaP64 = True
booleanaP4 = True

contador = 0
contador2 = 0

# Funciones para ajustar las fotos a los frames
def llamarATodas(event, indice):

    cambiarTamañoFotoP61(event, indice)
    cambiarTamañoFotoP62(event, indice)
    cambiarTamañoFotoP63(event, indice)
    cambiarTamañoFotoP64(event, indice)
    cambiarTamañoFotoP4(event, contador2)

def cambiarTamañoFotoP61(event, indice):
    global booleanaP61

    if booleanaP61:
        pass

    else:
        global fotoP61
        global imagenRedimensionadaP61
        global imagenTkP61

        anchoP61 = p61.winfo_width()
        altoP61 = p61.winfo_height()

        fotoP61 = Image.open(rutasFotos[indice][0])
        
        imagenRedimensionadaP61 = fotoP61.resize((anchoP61, altoP61), Image.Resampling.LANCZOS)

        imagenTkP61 = ImageTk.PhotoImage(imagenRedimensionadaP61)
    
        labelP61.config(image=imagenTkP61)

def cambiarTamañoFotoP62(event, indice):
    global booleanaP62

    if booleanaP62:
        pass

    else:
        global fotoP62
        global imagenRedimensionadaP62
        global imagenTkP62

        anchoP62 = p61.winfo_width()
        altoP62 = p61.winfo_height()

        fotoP62 = Image.open(rutasFotos[indice][1])
        
        imagenRedimensionadaP62 = fotoP62.resize((anchoP62, altoP62), Image.Resampling.LANCZOS)

        imagenTkP62 = ImageTk.PhotoImage(imagenRedimensionadaP62)
    
        labelP62.config(image=imagenTkP62)

def cambiarTamañoFotoP63(event, indice):
    global booleanaP63

    if booleanaP63:
        pass

    else:
        global fotoP63
        global imagenRedimensionadaP63
        global imagenTkP63

        anchoP63 = p61.winfo_width()
        altoP63 = p61.winfo_height()

        fotoP63 = Image.open(rutasFotos[indice][2])
        
        imagenRedimensionadaP63 = fotoP63.resize((anchoP63, altoP63), Image.Resampling.LANCZOS)

        imagenTkP63 = ImageTk.PhotoImage(imagenRedimensionadaP63)
    
        labelP63.config(image=imagenTkP63)

def cambiarTamañoFotoP64(event, indice):
    global booleanaP64

    if booleanaP64:
        pass

    else:
        global fotoP64
        global imagenRedimensionadaP64
        global imagenTkP64

        anchoP64 = p61.winfo_width()
        altoP64 = p61.winfo_height()

        fotoP64 = Image.open(rutasFotos[indice][3])
        
        imagenRedimensionadaP64 = fotoP64.resize((anchoP64, altoP64), Image.Resampling.LANCZOS)

        imagenTkP64 = ImageTk.PhotoImage(imagenRedimensionadaP64)
    
        labelP64.config(image=imagenTkP64)

def cambiarTamañoFotoP4(event, indice2):

    global fotoP4
    global imagenRedimensionadaP4
    global imagenTkP4

    anchoLabelP4 = labelP4.winfo_width()
    altoLabelP4 = labelP4.winfo_height()

    fotoP4 = Image.open(rutasFotosP4[indice2])
        
    imagenRedimensionadaP4 = fotoP4.resize((anchoLabelP4, altoLabelP4), Image.Resampling.LANCZOS)

    imagenTkP4 = ImageTk.PhotoImage(imagenRedimensionadaP4)

    labelP4.config(image=imagenTkP4)

def cambiarP4(event):
    global booleanaP4

    if booleanaP4:
        booleanaP4 = False
    
    else:
        global contador2
        global fotoP4
        global imagenRedimensionadaP4
        global imagenTkP4

        contador2 = contador2 + 1
        contador2 = contador2 % 5

        cambiarTamañoFotoP4(event, contador2)

# Funcion para el cambio de hojas de vida y fotos de los desarrolladores
def cambioHojaDeVida():
    global contador
    global booleanaP61
    global booleanaP62
    global booleanaP63
    global booleanaP64

    botonP5.config(text= hojasDeVida[contador])

    labelP61.config(image=fotos[contador][0], bg="white", relief="groove", borderwidth=8)
    labelP62.config(image=fotos[contador][1], bg="white", relief="groove", borderwidth=8)
    labelP63.config(image=fotos[contador][2], bg="white", relief="groove", borderwidth=8)
    labelP64.config(image=fotos[contador][3], bg="white", relief="groove", borderwidth=8)
    
    booleanaP61 = False
    booleanaP62 = False
    booleanaP63 = False
    booleanaP64 = False

    llamarATodas(None, contador)
    #cambiarTamañoFotoP61(None,contador)
    #cambiarTamañoFotoP62(None,contador)
    
    contador = contador + 1
    contador = contador % 4

#------------------------------------------------------------------------
ventanaInicio = tk.Tk()
ventanaInicio.title("Ventana Principal de inicio")
ventanaInicio.geometry("768x432+384+172")
ventanaInicio.grid_propagate(False)  # "grid_propagate o pack_propagate hace que el contenedor se ajuste o no a su contenido"

menuBarVentanaInicio = tk.Menu(ventanaInicio)
ventanaInicio.config(menu=menuBarVentanaInicio)
menuInicio = tk.Menu(menuBarVentanaInicio)
menuInicio.config(tearoff=0)  # Para que no añada esos guiones que desplegan el menú en una ventana nueva
menuBarVentanaInicio.add_cascade(label="Inicio", menu=menuInicio)
menuInicio.add_command(label="Salir de la aplicación", command=lambda: ventanaInicio.destroy())
menuInicio.add_command(label="Descripción del sistema")

hojasDeVida = [
    "Hoja de vida de Jose",
    "Hoja de vida de Oscar",
    "Hoja de vida de Simon",
    "Hoja de vida de Julian"
]

directorioActual = os.path.dirname(__file__)  # Para indicar las rutas de los archivos, con base en donde se esté ejecutando el programa.
rutaFotos = os.path.join(directorioActual,"fotos") # Ruta a la carpeta de fotos

rutaP61Jose = f"{rutaFotos}/p61Jose.jpg"
rutaP62Jose = f"{rutaFotos}/p62Jose.jpg"
rutaP63Jose = f"{rutaFotos}/p63Jose.jpg"
rutaP64Jose = f"{rutaFotos}/p64Jose.jpg"

rutaP61Oscar = f"{rutaFotos}/p61Oscar.jpg"
rutaP62Oscar = f"{rutaFotos}/p62Oscar.jpg"
rutaP63Oscar = f"{rutaFotos}/p63Oscar.jpg"
rutaP64Oscar = f"{rutaFotos}/p64Oscar.jpg"

rutaP61Simon = f"{rutaFotos}/p61Simon.jpg"
rutaP62Simon = f"{rutaFotos}/p62Simon.jpg"
rutaP63Simon = f"{rutaFotos}/p63Simon.jpg"
rutaP64Simon = f"{rutaFotos}/p64Simon.jpg"

rutaP61Julian = f"{rutaFotos}/p61Julian.jpg"
rutaP62Julian = f"{rutaFotos}/p62Julian.jpg"
rutaP63Julian = f"{rutaFotos}/p63Julian.jpg"
rutaP64Julian = f"{rutaFotos}/p64Julian.jpg"

rutaP41 = f"{rutaFotos}/p41.jpg"
rutaP42 = f"{rutaFotos}/p42.jpg"
rutaP43 = f"{rutaFotos}/p43.jpg"
rutaP44 = f"{rutaFotos}/p44.jpg"
rutaP45 = f"{rutaFotos}/p45.jpg"

rutasFotos = [  # Rutas a las fotos de los desarrolladores (las que van en p6)
    [rutaP61Jose, rutaP62Jose, rutaP63Jose, rutaP64Jose],
    [rutaP61Oscar, rutaP62Oscar, rutaP63Oscar, rutaP64Oscar],
    [rutaP61Simon, rutaP62Simon, rutaP63Simon, rutaP64Simon],
    [rutaP61Julian, rutaP62Julian, rutaP63Julian, rutaP64Julian]
]

rutasFotosP4 = [rutaP41, rutaP42, rutaP43, rutaP44, rutaP45] # Rutas a las fotos que se muestran en p4

# Imagenes en el formato que usa tkinter
fotoP61Jose = ImageTk.PhotoImage(Image.open(rutaP61Jose))
fotoP62Jose = ImageTk.PhotoImage(Image.open(rutaP62Jose))
fotoP63Jose = ImageTk.PhotoImage(Image.open(rutaP63Jose))
fotoP64Jose = ImageTk.PhotoImage(Image.open(rutaP64Jose))

fotoP61Oscar = ImageTk.PhotoImage(Image.open(rutaP61Oscar))
fotoP62Oscar = ImageTk.PhotoImage(Image.open(rutaP62Oscar))
fotoP63Oscar = ImageTk.PhotoImage(Image.open(rutaP63Oscar))
fotoP64Oscar = ImageTk.PhotoImage(Image.open(rutaP64Oscar))

fotoP61Simon = ImageTk.PhotoImage(Image.open(rutaP61Simon))
fotoP62Simon = ImageTk.PhotoImage(Image.open(rutaP62Simon))
fotoP63Simon = ImageTk.PhotoImage(Image.open(rutaP63Simon))
fotoP64Simon = ImageTk.PhotoImage(Image.open(rutaP64Simon))

fotoP61Julian = ImageTk.PhotoImage(Image.open(rutaP61Julian))
fotoP62Julian = ImageTk.PhotoImage(Image.open(rutaP62Julian))
fotoP63Julian = ImageTk.PhotoImage(Image.open(rutaP63Julian))
fotoP64Julian = ImageTk.PhotoImage(Image.open(rutaP64Julian))

fotos = [
    [fotoP61Jose, fotoP62Jose, fotoP63Jose, fotoP64Jose],
    [fotoP61Oscar, fotoP62Oscar, fotoP63Oscar, fotoP64Oscar],
    [fotoP61Simon, fotoP62Simon, fotoP63Simon, fotoP64Simon],
    [fotoP61Julian, fotoP62Julian, fotoP63Julian, fotoP64Julian]
]

# Frame grande izquierdo
p1 = tk.Frame(ventanaInicio,background="black")
p1.grid(row=0, column=0, padx=(10,5), pady=(10,7), sticky="nsew")
p1.grid_propagate(False)

# Frame grande derecho
p2 = tk.Frame(ventanaInicio, background="black")
p2.grid(row=0, column=1, padx=(5,10), pady=(10,7), sticky="nsew")
p2.grid_propagate(False)

# Configuracion para que los frames p1 y p2 crezcan proporcinalmente
ventanaInicio.grid_rowconfigure(0,weight=1)
ventanaInicio.grid_columnconfigure(0,weight=1)
ventanaInicio.grid_columnconfigure(1,weight=1)

# Frame superior interno de p1
p3 = tk.Frame(p1,background="white")
p3.grid(row=0, column=0, padx=7, pady=(7,5), sticky="snew")
p3.pack_propagate(False)

# Mensaje de bienvenida al sistema
labelP3 = tk.Label(p3, bg="white",text="Mensaje de bienvenida al sistema :)", font=("Arial"), wraplength= 400, anchor= "center", border=5)
labelP3.pack(expand=True, fill="both")

# Frame inferior interno de p1
p4 = tk.Frame(p1,background="white")
p4.grid(row=1, column=0, padx=7, pady=(5,7), sticky="snew")
p4.grid_propagate(False)

# Configuracion para crezacan de distintas maneras labelP4 (el de la imagene que cambia al entrar y salir) y botonP4 (lleva a la otra ventana)
p4.grid_columnconfigure(0, weight=1)
p4.grid_rowconfigure(0,weight=1)
p4.grid_rowconfigure(1, weight=0)

# Label para las fotos que entran y salen
labelP4 = tk.Label(p4, bg="White")
labelP4.grid(row=0, column=0, sticky="nsew")

labelP4.bind("<Enter>", cambiarP4) # Evento para que la imagen cambie al pasar el mouse por ahí

cambiarP4(contador2) # Se llama a la fucion para poner una imagen por primera vez al iniciar el programa

# Boton para abrir la otra ventana
botonP4 = tk.Button(p4, cursor="hand2", text="Programa principal", font=("Arial"), wraplength=400, anchor= "center", bg="gray90") #AGREGAR FUNCION PARA LA NUEVA VENTANA
botonP4.grid(row=1, column=0, sticky="ew", ipady=15)

# Configuracion para que los frames p3 y p4 crezcan con una proporcion 1 a 2
p1.grid_columnconfigure(0, weight=1)
p1.grid_rowconfigure(0,weight=1)
p1.grid_rowconfigure(1, weight=2)

# Frame superior interno de p2
p5 = tk.Frame(p2,background="white")
p5.grid(row=0, column=0, padx=7, pady=(7,5), sticky="snew")
p5.pack_propagate(False)

# Boton para el cambio de hoja de vida
botonP5 = tk.Button(p5, cursor="hand2", text="Hojas de vida de los desarrolladores", font=("Arial"), wraplength= 400, anchor= "center", bg="gray90",border=5, command=cambioHojaDeVida)
botonP5.pack(expand=True, fill="both")

# Frame inferior interno de p2
p6 = tk.Frame(p2,background="gray50")
p6.grid(row=1, column=0, padx=7, pady=(5,7), sticky="snew")
p6.grid_propagate(False)

# Configuracion para que los frames p3 y p4 crezcan con una proporcion 1 a 2
p2.grid_columnconfigure(0, weight=1)
p2.grid_rowconfigure(0,weight=1)
p2.grid_rowconfigure(1, weight=2)

# Frames para las fotos, van todos dentro de p6 (nombrados como por cuadrantes)
#  ------------------------ ----------------------
# | p61: arriba izquierda, | p62: arriba derecha, |
#  ------------------------ ----------------------
# | p63: abajo izquierda,  | p64: abajo derecha.  |
#  ------------------------ ----------------------

p61 = tk.Frame(p6, bg="gray50")
p61.grid(row=0, column=0, padx=(5,2.5), pady=(5,2.5), sticky="snew")

p62 = tk.Frame(p6, bg="gray50")
p62.grid(row=0, column=1, padx=(2.5,5), pady=(5,2.5), sticky="snew")

p63 = tk.Frame(p6, bg="gray50")
p63.grid(row=1, column=0, padx=(5,2.5), pady=(2.5,5), sticky="snew")

p64 = tk.Frame(p6, bg="gray50")
p64.grid(row=1, column=1, padx=(2.5,5), pady=(2.5,5), sticky="snew")

# Configuracion para que los frames dentro de p6 crezcan proporcionalmente
p6.grid_rowconfigure(0,weight=1)
p6.grid_rowconfigure(1,weight=1)
p6.grid_columnconfigure(0,weight=1)
p6.grid_columnconfigure(1,weight=1)

# Labes para las fotos
p61.pack_propagate(False)
p62.pack_propagate(False)
p63.pack_propagate(False)
p64.pack_propagate(False)

labelP61 = tk.Label(p61, bg="gray50")
labelP61.pack(fill="both",expand=True, anchor="center")
labelP62 = tk.Label(p62, bg="gray50")
labelP62.pack(fill="both",expand=True, anchor="center")
labelP63 = tk.Label(p63, bg="gray50")
labelP63.pack(fill="both",expand=True, anchor="center")
labelP64 = tk.Label(p64, bg="gray50")
labelP64.pack(fill="both",expand=True, anchor="center")

ventanaInicio.bind("<Configure>", lambda event: llamarATodas(event, contador-1)) # Evento para reajustar las imagenes al tamaño de la ventana

ventanaInicio.mainloop()