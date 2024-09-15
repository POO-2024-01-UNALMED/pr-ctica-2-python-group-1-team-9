import os
import tkinter as tk
from PIL import Image, ImageTk
from uiMain.VentanaPrincipal import VentanaPrincipal
from baseDatos.Serializacion import Serializacion

class VentanaInicio(tk.Tk):

    def __init__(self):
        super().__init__()
        # Configuración basica de la ventana
        self.title("Ventana Principal de Inicio")
        self.geometry("1000x550+284+72")
        self.grid_propagate(False) # grid_propagate o pack_propagate hace que el contenedor se ajuste o no a su contenido"
        self.protocol("WM_DELETE_WINDOW", self.serializarAlCerrarLaVentana)

        self.hojasDeVida = [
            "Soy Jose Manuel, tengo 20 años, soy de Pueblorrico, un pequeño municipio de Antioquia, me gusta mucho salir a caminar y pasar tiempo en familia, este es mi primer semestre en la carrera (me traslade desde mecánica) y estoy entusiamado por aprender 😀",
            "Mi nombre es Oscar Daniel, nací en el municipio de Itaguí y estoy en el segundo semestre de Ingeniería de sistemas en la Universidad Nacional de Colombia sede Medellín, mi objetivo es convertirme en el mejor entrenador pokem... digo aprender mucho...", 
            "Hoja de vida de Simon", 
            "Hoja de vida de Julian"
        ]
        
        # Variables para la logica en el manejo de las fotos
        self.fotoP61 = None
        self.fotoP62 = None
        self.fotoP63 = None
        self.fotoP64 = None
        self.fotoP4 = None

        self.imagenTkP61 = None
        self.imagenTkP62 = None
        self.imagenTkP63 = None
        self.imagenTkP64 = None
        self.imagenTkP4 = None

        self.imagenRedimensionadaP61 = None
        self.imagenRedimensionadaP62 = None
        self.imagenRedimensionadaP63 = None
        self.imagenRedimensionadaP64 = None
        self.imagenRedimensionadaP4 = None

        self.contador = 0
        self.contador2 = 0
        self.booleanaP61 = True
        self.booleanaP62 = True
        self.booleanaP63 = True
        self.booleanaP64 = True
        self.booleanaP4 = True

        # Para indicar la ruta donde están las fotos
        self.directorioActual = os.path.dirname(os.path.dirname(__file__))
        self.rutaFotos = os.path.join(self.directorioActual, "fotos")

        self.inicializarRutasFotos() # Se inicializa la lista que contiene las rutas a las fotos

        # Creación de la interfaza
        self.crearMenu()
        self.crearFrames()
        self.configurarGrid()

        # Evento para redimensionar imágenes
        self.bind("<Configure>", lambda event: self.llamarATodas(event, (self.contador-1)))

    def crearMenu(self): # Función para crear el menú
        menuBar = tk.Menu(self)
        self.config(menu=menuBar)
        menuInicio = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Inicio", menu=menuInicio)
        menuInicio.add_command(label="Salir de la aplicación", command=self.serializarAlCerrarLaVentana)
        menuInicio.add_command(label="Descripción del sistema", command=lambda: self.labelP4.config(image="", font=("Arial"), wraplength=420,
                                text="'Plataforma Super Usable Para Supermercados'\nle permite administar su inventario, generar ordenenes de compra, hacer registro de clientes, además de realizar seguimiento a los procesos llevados a cabo en la operación del supermercado."))

    def inicializarRutasFotos(self): # Funcion para crear todas las rutas a las fotos que van en el frameP6
        self.rutasFotos = [
            [os.path.join(self.rutaFotos, f"p61{nombre}.jpg") for nombre in ["Jose", "Oscar", "Simon", "Julian"]],
            [os.path.join(self.rutaFotos, f"p62{nombre}.jpg") for nombre in ["Jose", "Oscar", "Simon", "Julian"]],
            [os.path.join(self.rutaFotos, f"p63{nombre}.jpg") for nombre in ["Jose", "Oscar", "Simon", "Julian"]],
            [os.path.join(self.rutaFotos, f"p64{nombre}.jpg") for nombre in ["Jose", "Oscar", "Simon", "Julian"]],
        ]
        self.rutasFotosP4 = [os.path.join(self.rutaFotos, f"p4{i}.jpg") for i in range(1,6)]

    def crearFrames(self): # Se crean los dos frames grandes p1 y p2 y luego se llaman las funciones para los frames internos
        # Frame P1 (izquierda)
        self.frameP1 = tk.Frame(self, bg="black")
        self.frameP1.grid(row=0, column=0, padx=(10,5), pady=(10,7), sticky="nsew")
        self.frameP1.grid_propagate(False)

        self.frameP1.grid_columnconfigure(0, weight=1)
        self.frameP1.grid_rowconfigure(0, weight=1)
        self.frameP1.grid_rowconfigure(1, weight=2)

        # Frame P2 (derecha)
        self.frameP2 = tk.Frame(self, bg="black")
        self.frameP2.grid(row=0, column=1, padx=(5,10), pady=(10,7), sticky="nsew")
        self.frameP2.grid_propagate(False)

        self.frameP2.grid_columnconfigure(0, weight=1)
        self.frameP2.grid_rowconfigure(0, weight=1)
        self.frameP2.grid_rowconfigure(1, weight=2)

        # Se crean los frames internos de p1 y p2
        self.crearFramesInternosP1()
        self.crearFramesInternosP2()

    def configurarGrid(self): # Configuración para la disposicion de los frames p1 y p2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def crearFramesInternosP1(self):
        # Frame p3 el que va dentro de p1 en la parte superior
        self.frameP3 = tk.Frame(self.frameP1, bg="white")
        self.frameP3.grid(row=0, column=0, padx=7, pady=(7,5), sticky="nsew")
        self.frameP3.pack_propagate(False)
        
        self.labelP3 = tk.Label(self.frameP3, bg="white", text="Bienvenido a PSUPS, con nuestro sistema, administar su supermercado,\n¡Nunca fue tan facil!", 
                                font=("Arial"), wraplength=420, anchor="center", border=5)
        self.labelP3.pack(expand=True, fill="both")

        # Frame p4 el que va dentro de p1 en la parte inferior
        self.frameP4 = tk.Frame(self.frameP1, bg="white")
        self.frameP4.grid(row=1, column=0, padx=7, pady=(5,7), sticky="nsew")
        self.frameP4.grid_propagate(False)
        
        # Configuración para que lo que vaya dentro de p4  (labelP4 y botonP4 crezcan como se necesita)
        self.frameP4.grid_columnconfigure(0, weight=1)
        self.frameP4.grid_rowconfigure(0, weight=1)
        self.frameP4.grid_rowconfigure(1, weight=0)

        # Label para la foto que cambia al pasar el mouse por encima (este label va dentro de p4 en la parte superior)
        self.labelP4 = tk.Label(self.frameP4, bg="white")
        self.labelP4.grid(row=0, column=0, sticky="nsew")
        self.labelP4.bind("<Leave>", self.cambiarP4) # Evento para el cambio de la foto
        self.cambiarP4(self.contador2) # Se llama a esta funcio para que aparezca una imagen en labelP4 de una vez se inicia el programa

        # Botón para ir al programa principal (va dentro de p4 en la parte inferior)
        self.botonP4 = tk.Button(self.frameP4, text="Programa principal",
                                 font=("Arial"), bg="gray90")
        self.botonP4.grid(row=1, column=0, sticky="ew", ipady=15)

    def crearFramesInternosP2(self):
        # Frame p5 el que va dentro de p2 en la parte superior, el que tiene las hojas de vida
        self.frameP5 = tk.Frame(self.frameP2, bg="white")
        self.frameP5.grid(row=0, column=0, padx=7, pady=(7,5), sticky="nsew")
        self.frameP5.pack_propagate(False)

        # Boton p5 es el que está dentro de p5 y se encarga de cambiar las hojas de vida y las fotos de p6
        self.botonP5 = tk.Button(self.frameP5, text="Hojas de vida de los desarrolladores", wraplength=420  ,
                                 font=("Arial"), bg="gray90", command=self.cambioHojaDeVida)
        self.botonP5.pack(expand=True, fill="both")

        # Frame p6 en este van las 4 fotos de cada uno de los desarrolladores, va dentro de p2 en la parte inferior
        self.frameP6 = tk.Frame(self.frameP2, bg="gray50")
        self.frameP6.grid(row=1, column=0, padx=7, pady=(5,7), sticky="nsew")
        self.frameP6.grid_propagate(False)

        # Configuración para que los frames que contendran las fotos crezcan igual
        self.frameP6.grid_rowconfigure(0,weight=1)
        self.frameP6.grid_rowconfigure(1,weight=1)
        self.frameP6.grid_columnconfigure(0,weight=1)
        self.frameP6.grid_columnconfigure(1,weight=1)

        self.crearCuadrantesFotos() # Para crear los frames que tendran las fotos de los desarrolladores

    def crearCuadrantesFotos(self): # Crea los 4 frames que contendran las fotos de los desarroladores

        # Frames para las fotos, van todos dentro de p6 (nombrados como por cuadrantes)
        #  ------------------------ ----------------------
        # | p61: arriba izquierda, | p62: arriba derecha, |
        #  ------------------------ ----------------------
        # | p63: abajo izquierda,  | p64: abajo derecha.  |
        #  ------------------------ ----------------------

        self.frameP61 = tk.Frame(self.frameP6, bg="gray50")
        self.frameP61.grid(row=0, column=0, padx=(5, 2.5), pady=(5, 2.5), sticky="nsew")
        self.frameP61.pack_propagate(False)

        self.labelP61 = tk.Label(self.frameP61, bg="gray50")
        self.labelP61.pack(fill="both", expand=True)

        self.frameP62 = tk.Frame(self.frameP6, bg="gray50")
        self.frameP62.grid(row=0, column=1, padx=(2.5, 5), pady=(5, 2.5), sticky="nsew")
        self.frameP62.pack_propagate(False)

        self.labelP62 = tk.Label(self.frameP62, bg="gray50")
        self.labelP62.pack(fill="both", expand=True)

        self.frameP63 = tk.Frame(self.frameP6, bg="gray50")
        self.frameP63.grid(row=1, column=0, padx=(5, 2.5), pady=(2.5, 5), sticky="nsew")
        self.frameP63.pack_propagate(False)

        self.labelP63 = tk.Label(self.frameP63, bg="gray50")
        self.labelP63.pack(fill="both", expand=True)

        self.frameP64 = tk.Frame(self.frameP6, bg="gray50")
        self.frameP64.grid(row=1, column=1, padx=(2.5, 5), pady=(2.5, 5), sticky="nsew")
        self.frameP64.pack_propagate(False)

        self.labelP64 = tk.Label(self.frameP64, bg="gray50")
        self.labelP64.pack(fill="both", expand=True)

    def llamarATodas(self, event, contador): # Esta funcion se encarga de llamar todas las funciones encargadas de redimensionar las imagenes (hay una funcion por imagen)

        self.cambiarTamañoFotoP61(event, contador)
        self.cambiarTamañoFotoP62(event, contador)
        self.cambiarTamañoFotoP63(event, contador)
        self.cambiarTamañoFotoP64(event, contador)
        self.cambiarTamañoFotoP4(event, self.contador2)

    def cambiarTamañoFotoP61(self, event, indice): # Se encarga de cambiar el tamaño de la fotoP61 según el tamaño del frame

        if self.booleanaP61:
            pass

        else:

            anchoP61 = self.frameP61.winfo_width()
            altoP61 = self.frameP61.winfo_height()

            self.fotoP61 = Image.open(self.rutasFotos[0][indice])

            self.imagenRedimensionadaP61 = self.fotoP61.resize((anchoP61, altoP61), Image.Resampling.LANCZOS)

            self.imagenTkP61=ImageTk.PhotoImage(self.imagenRedimensionadaP61)

            self.labelP61.config(image=self.imagenTkP61)

    def cambiarTamañoFotoP62(self, event, indice): # Se encarga de cambiar el tamaño de la fotoP62 según el tamaño del frame


        if self.booleanaP62:
            pass

        else:

            anchoP62 = self.frameP62.winfo_width()
            altoP62 = self.frameP62.winfo_height()

            self.fotoP62 = Image.open(self.rutasFotos[1][indice])

            self.imagenRedimensionadaP62 = self.fotoP62.resize((anchoP62, altoP62), Image.Resampling.LANCZOS)

            self.imagenTkP62=ImageTk.PhotoImage(self.imagenRedimensionadaP62)

            self.labelP62.config(image=self.imagenTkP62)

    def cambiarTamañoFotoP63(self, event, indice): # Se encarga de cambiar el tamaño de la fotoP63 según el tamaño del frame

        if self.booleanaP63:
            pass

        else:

            anchoP63 = self.frameP63.winfo_width()
            altoP63 = self.frameP63.winfo_height()

            self.fotoP63 = Image.open(self.rutasFotos[2][indice])

            self.imagenRedimensionadaP63 = self.fotoP63.resize((anchoP63, altoP63), Image.Resampling.LANCZOS)

            self.imagenTkP63=ImageTk.PhotoImage(self.imagenRedimensionadaP63)

            self.labelP63.config(image=self.imagenTkP63)

    def cambiarTamañoFotoP64(self, event, indice): # Se encarga de cambiar el tamaño de la fotoP64 según el tamaño del frame

        if self.booleanaP64:
            pass

        else:

            anchoP64 = self.frameP64.winfo_width()
            altoP64 = self.frameP64.winfo_height()

            self.fotoP64 = Image.open(self.rutasFotos[3][indice])

            self.imagenRedimensionadaP64 = self.fotoP64.resize((anchoP64, altoP64), Image.Resampling.LANCZOS)

            self.imagenTkP64=ImageTk.PhotoImage(self.imagenRedimensionadaP64)

            self.labelP64.config(image=self.imagenTkP64)

    def cambiarP4(self, event): # Se encarga de llamar a "cambiarTamañoFotoP4" cuando es necesario

        if self.booleanaP4:
            self.booleanaP4 = False
            
        else:
            self.contador2 = (self.contador2 + 1) % 5
            self.cambiarTamañoFotoP4(event, self.contador2)

    def cambiarTamañoFotoP4(self, event, indice2): # Se encarga de cambiar el tamaño de la fotoP4 (la que cambia con pasar el mouse) según el tamaño del label

        anchoP4 = self.labelP4.winfo_width()
        altoP4 = self.labelP4.winfo_height()

        self.fotoP4 = Image.open(self.rutasFotosP4[indice2])

        self.imagenRedimensionadaP4 = self.fotoP4.resize((anchoP4, altoP4), Image.Resampling.LANCZOS)

        self.imagenTkP4 = ImageTk.PhotoImage(self.imagenRedimensionadaP4)

        self.labelP4.config(image=self.imagenTkP4)

    def cambioHojaDeVida(self): # Se encarga de cambiar variables y hace llamados a funciones cuando se apreta el boton p5 (el de cambio hoja de vida)
        
        self.botonP5.config(text=self.hojasDeVida[self.contador])

        self.labelP61.config(bg="white", relief="groove", borderwidth=8)
        self.labelP62.config(bg="white", relief="groove", borderwidth=8)
        self.labelP63.config(bg="white", relief="groove", borderwidth=8)
        self.labelP64.config(bg="white", relief="groove", borderwidth=8)
    
        self.booleanaP61 = False
        self.booleanaP62 = False
        self.booleanaP63 = False
        self.booleanaP64 = False

        self.llamarATodas(None, self.contador)

        self.contador = (self.contador + 1) % 4
    
    def serializarAlCerrarLaVentana(self):
        #Serializacion.serializar()
        self.destroy()