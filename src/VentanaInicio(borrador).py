import tkinter as tk

ventanaInicio = tk.Tk()
ventanaInicio.title("Ventana Principal de inicio")
ventanaInicio.geometry("600x600")
ventanaInicio.config(background="red")

#Frame grande izquierdo
p1 = tk.Frame(ventanaInicio,background="black")
p1.grid(row=0, column=0, padx=(10,5), pady=(10,7), sticky="nsew")

#Frame grande derecho
p2 = tk.Frame(ventanaInicio, background="blue")
p2.grid(row=0, column=1, padx=(5,10), pady=(10,7), sticky="nsew")

#Configuracion para que los frames p1 y p2 crezcan proporcinalmente
ventanaInicio.grid_rowconfigure(0,weight=1)
ventanaInicio.grid_columnconfigure(0,weight=1)
ventanaInicio.grid_columnconfigure(1,weight=1)

#Frame superior interno de p1
p3 = tk.Frame(p1,background="purple")
p3.grid(row=0, column=0, padx=7, pady=(7,5), sticky="snew")

#Frame inferior interno de p1
p4 = tk.Frame(p1,background="green")
p4.grid(row=1, column=0, padx=7, pady=(5,7), sticky="snew")

#Configuracion para que los frames p3 y p4 crezcan con una proporcion 1 a 2
p1.grid_columnconfigure(0, weight=1)
p1.grid_rowconfigure(0,weight=1)
p1.grid_rowconfigure(1, weight=2)

#Frame superior interno de p2
p5 = tk.Frame(p2,background="gold")
p5.grid(row=0, column=0, padx=7, pady=(7,5), sticky="snew")

#Frame inferior interno de p2
p6 = tk.Frame(p2,background="aquamarine")
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

p61 = tk.Frame(p6)
p61.grid(row=0, column=0, padx=(5,2.5), pady=(5,2.5), sticky="snew")

p62 = tk.Frame(p6)
p62.grid(row=0, column=1, padx=(2.5,5), pady=(5,2.5), sticky="snew")

p63 = tk.Frame(p6)
p63.grid(row=1, column=0, padx=(5,2.5), pady=(2.5,5), sticky="snew")

p64 = tk.Frame(p6)
p64.grid(row=1, column=1, padx=(2.5,5), pady=(2.5,5), sticky="snew")

#Configuracion para que los frames dentro de p6 crezcan proporcionalmente
p6.grid_rowconfigure(0,weight=1)
p6.grid_rowconfigure(1,weight=1)
p6.grid_columnconfigure(0,weight=1)
p6.grid_columnconfigure(1,weight=1)


ventanaInicio.mainloop()