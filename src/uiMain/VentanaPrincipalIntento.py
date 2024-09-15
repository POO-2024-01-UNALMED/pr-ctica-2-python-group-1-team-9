import tkinter as tk

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Supermercado")
        self.root.geometry("800x400")
        
        self.supermercado_seleccionado = None
        self.producto_seleccionado = None
        
        # Crear el marco principal
        self.marco_principal = tk.Frame(self.root)
        self.marco_principal.pack(fill=tk.BOTH, expand=True)

        # Crear el marco para la barra de navegación
        self.marco_navbar = tk.Frame(self.marco_principal, bg="#f0f0f0", padx=10, pady=10)
        self.marco_navbar.pack(side=tk.TOP, fill=tk.X)

        # Crear botones en la barra de navegación
        self.boton1 = tk.Button(self.marco_navbar, text="Supermercado A", command=lambda: self.seleccionar_supermercado("Supermercado A"))
        self.boton2 = tk.Button(self.marco_navbar, text="Supermercado B", command=lambda: self.seleccionar_supermercado("Supermercado B"))
        self.boton3 = tk.Button(self.marco_navbar, text="Supermercado C", command=lambda: self.seleccionar_supermercado("Supermercado C"))

        # Organizar los botones en la barra de navegación
        self.boton1.pack(side=tk.LEFT, padx=5)
        self.boton2.pack(side=tk.LEFT, padx=5)
        self.boton3.pack(side=tk.LEFT, padx=5)

        # Crear un marco para el contenido principal
        self.marco_contenido = tk.Frame(self.marco_principal)
        self.marco_contenido.pack(fill=tk.BOTH, expand=True)

        # Crear un marco para la lista de productos y el área de selección
        self.marco_lista = tk.Frame(self.marco_contenido, padx=10, pady=10)
        self.marco_lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear una etiqueta para el texto
        self.etiqueta = tk.Label(self.marco_lista, text="Seleccione un supermercado", font=("Arial", 16))
        self.etiqueta.pack(pady=10)

        # Crear una lista para mostrar los productos
        self.lista_box = tk.Listbox(self.marco_lista, width=40, height=10)
        self.lista_box.pack(pady=10)
        self.lista_box.bind("<<ListboxSelect>>", self.on_lista_select)

        # Crear una etiqueta para mostrar el elemento seleccionado
        self.etiqueta_seleccion = tk.Label(self.marco_lista, text="", font=("Arial", 14))
        self.etiqueta_seleccion.pack(pady=10)

        # Crear un marco para mostrar los productos del supermercado seleccionado
        self.marco_productos = tk.Frame(self.marco_contenido, padx=10, pady=10)
        self.marco_productos.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Crear una etiqueta para mostrar los productos
        self.etiqueta_productos = tk.Label(self.marco_productos, text="Detalles del Producto", font=("Arial", 16))
        self.etiqueta_productos.pack(pady=10)

        # Crear una lista para mostrar los detalles del producto seleccionado
        self.lista_productos = tk.Listbox(self.marco_productos, width=40, height=10)
        self.lista_productos.pack(pady=10)
        
    def seleccionar_supermercado(self, supermercado):
        self.supermercado_seleccionado = supermercado
        self.etiqueta.config(text=f"Supermercado Seleccionado: {supermercado}")
        self.actualizar_lista(supermercado)
        self.boton_mostrar_productos.config(state=tk.NORMAL)

    def actualizar_lista(self, texto):
        # Limpiar la lista actual
        self.lista_box.delete(0, tk.END)
        
        # Dependiendo del supermercado seleccionado, mostrar diferentes productos
        supermercados = {
            "Supermercado A": ["Carnes Perez", "Verduras Verduras la 45", "65 Quesos"],
            "Supermercado B": ["Deberían estar las funcionalidades"],
            "Supermercado C": ["Funcionalidades"]
        }
        
        # Actualizar lista según el supermercado seleccionado
        if texto in supermercados:
            for item in supermercados[texto]:
                self.lista_box.insert(tk.END, item)

    def on_lista_select(self, event):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.producto_seleccionado = self.lista_box.get(seleccion[0])
            self.etiqueta_seleccion.config(text=f"Seleccionaste: {self.producto_seleccionado}")
            self.mostrar_detalles()

    def mostrar_productos(self):
        if self.supermercado_seleccionado:
            productos = {
                "Supermercado A": ["Carnes Perez", "Verduras Verduras la 45", "65 Quesos"],
                "Supermercado B": ["Deberían estar las funcionalidades"],
                "Supermercado C": ["Funcionalidades"]
            }
            productos_lista = productos.get(self.supermercado_seleccionado, [])
            self.lista_box.delete(0, tk.END)  # Limpiar la lista actual
            for producto in productos_lista:
                self.lista_box.insert(tk.END, producto)

    def mostrar_detalles(self):
        if self.producto_seleccionado:
            detalles = {
                "Carnes Perez": ["Chuleta de cerdo", "Bondiola", "Costilla", "Espalda"],
                "Verduras Verduras la 45": ["Papa", "Calabaza", "Pepino"],
                "65 Quesos": ["Queso Manchego", "Queso Cheddar", "Queso Azul", "Queso Brie"]
            }
            detalles_lista = detalles.get(self.producto_seleccionado, [])
            self.lista_productos.delete(0, tk.END)  # Limpiar la lista actual
            for detalle in detalles_lista:
                self.lista_productos.insert(tk.END, detalle)

# Crear la ventana principal
ventana = tk.Tk()
app = Aplicacion(ventana)

# Ejecutar el bucle principal
ventana.mainloop()

