import os
import tkinter as tk
from PIL import Image, ImageTk
#------------------------------------------------------------------------

fotoP61 = 1
fotoP62 = 1
fotoP63 = 1
fotoP64 = 1

imagenRedimensionadaP61 = 1
imagenRedimensionadaP62 = 1
imagenRedimensionadaP63 = 1
imagenRedimensionadaP64 = 1

imagenTkP61 = 1
imagenTkP62 = 1
imagenTkP63 = 1
imagenTkP64 = 1

booleanaP61 = True
booleanaP62 = True
booleanaP63 = True
booleanaP64 = True

contador = 0

#Funciones para ajustar las fotos a los frames
def llamarATodas(event, indice):

    cambiarTamañoFotoP61(event, indice)
    cambiarTamañoFotoP62(event, indice)
    cambiarTamañoFotoP63(event, indice)
    cambiarTamañoFotoP64(event, indice)

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

#Funcion para el cambio de hojas de vida y fotos de los desarrolladores
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
ventanaInicio.wm_state("zoomed") #hace que la ventana aparezca maximizada
ventanaInicio.geometry("768x432+384+172")

hojasDeVida = [
    "Hoja de vida de Jose",
    "Hoja de vida de Oscar",
    "Hoja de vida de Simon",
    "Hoja de vida de Julian"
]

directorioActual = os.path.dirname(__file__)
rutaFotos = os.path.join(directorioActual,"fotos")

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

rutasFotos = [
    [rutaP61Jose, rutaP62Jose, rutaP63Jose, rutaP64Jose],
    [rutaP61Oscar, rutaP62Oscar, rutaP63Oscar, rutaP64Oscar],
    [rutaP61Simon, rutaP62Simon, rutaP63Simon, rutaP64Simon],
    [rutaP61Julian, rutaP62Julian, rutaP63Julian, rutaP64Julian]
]

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

#Frame grande izquierdo
p1 = tk.Frame(ventanaInicio,background="black")
p1.grid(row=0, column=0, padx=(10,5), pady=(10,7), sticky="nsew")

#Frame grande derecho
p2 = tk.Frame(ventanaInicio, background="black")
p2.grid(row=0, column=1, padx=(5,10), pady=(10,7), sticky="nsew")

#Configuracion para que los frames p1 y p2 crezcan proporcinalmente
ventanaInicio.grid_rowconfigure(0,weight=1)
ventanaInicio.grid_columnconfigure(0,weight=1)
ventanaInicio.grid_columnconfigure(1,weight=1)

#Frame superior interno de p1
p3 = tk.Frame(p1,background="white")
p3.grid(row=0, column=0, padx=7, pady=(7,5), sticky="snew")

#Frame inferior interno de p1
p4 = tk.Frame(p1,background="white")
p4.grid(row=1, column=0, padx=7, pady=(5,7), sticky="snew")

#Configuracion para que los frames p3 y p4 crezcan con una proporcion 1 a 2
p1.grid_columnconfigure(0, weight=1)
p1.grid_rowconfigure(0,weight=1)
p1.grid_rowconfigure(1, weight=2)

#Frame superior interno de p2
p5 = tk.Frame(p2,background="white")
p5.grid(row=0, column=0, padx=7, pady=(7,5), sticky="snew")

##Boton para el cambio de hoja de vida
botonP5 = tk.Button(p5, text="Hojas de vida de los desarrolladores", font=("Arial"), wraplength= 700, anchor= "center", bg="gray90",border=5, command=cambioHojaDeVida)
p5.pack_propagate(False)    #Esto hace que el frame p5 no se adapte al tamño del botón, manteniendo la estetica.
botonP5.pack(expand=True, fill="both")

#Frame inferior interno de p2
p6 = tk.Frame(p2,background="gray50")
p6.grid(row=1, column=0, padx=7, pady=(5,7), sticky="snew")

#Configuracion para que los frames p3 y p4 crezcan con una proporcion 1 a 2
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

#Configuracion para que los frames dentro de p6 crezcan proporcionalmente
p6.grid_rowconfigure(0,weight=1)
p6.grid_rowconfigure(1,weight=1)
p6.grid_columnconfigure(0,weight=1)
p6.grid_columnconfigure(1,weight=1)

#Labes para las fotos
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

ventanaInicio.bind("<Configure>", lambda event: llamarATodas(event, contador-1))

ventanaInicio.mainloop()