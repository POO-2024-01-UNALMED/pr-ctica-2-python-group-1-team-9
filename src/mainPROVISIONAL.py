from gestorAplicacion.Persona import Persona
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Orden import Orden
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Unidad import Unidad
import Intento_serializar

barraDeSeparacion = "______________________________________________________________________________________________________"
#creamos listas para serializar los elementos 
Lista_supermercados= Supermercado.getSupermercados


#Funcionalidades

#F1
supermercado1 = Supermercado(nombre="Supermercado Central", saldo=5000.0)
clientes = [Cliente(nombre="Julian", cedula="1"), Cliente("Julio", "2")]
empleado1 = [Empleado(nombre="Guzman", cedula="2", supermercado=supermercado1, cargo="Empleado", salario="100"), Empleado(nombre="David", cedula="22", supermercado=supermercado1, cargo="Empleado", salario="100")]
supermercado1.agregarEmpleado(empleado1)

def crearOrden():
    supermercados = Supermercado.getSupermercados()
    personas = Persona.getPersonas()
    clientes = [persona for persona in personas if persona.getCargo() == "Cliente"]

    while True:
        print("\n=== Lista de Supermercados ===")
        for i, sup in enumerate(supermercados, 1):
            print(f"{i}. {sup.getNombre()}")

        try:
            opcion = int(input("Seleccione un supermercado: "))
            if 1 <= opcion <= len(supermercados):
                supermercado = supermercados[opcion - 1]
                print(f"\n- Supermercado {supermercado.getNombre()} seleccionado.")
                break
            else:
                print("- Opción inválida, por favor intente de nuevo.")
        except ValueError:
            print("- Opción inválida, por favor intente de nuevo.")

    empleados = supermercado.getEmpleados()

    while True:
        print("\n=== Lista de Empleados ===")
        for i, persona in enumerate(empleados, start=1):
            print(f"{i}. {persona.informacion()}")
            if i == len(empleado1):
                break

        try:
            opcion = int(input("Seleccione empleado encargado: "))
            if 1 <= opcion <= len(empleados):
                empleado = empleados[opcion - 1]
                print(f"\n- {empleado.getCargo()} {empleado.getNombre()} seleccionado.")
                break
            else:
                print("- Opción inválida, por favor intente de nuevo.")
        except ValueError:
            print("- Opción inválida, por favor intente de nuevo.")
    while True:
        registrado = input("El cliente ya está registrado? (s/n): ").strip().lower()
        if registrado == 's':
            while True:
                print("\n=== Lista de Clientes ===")
                print("Clientes en la lista:")
                for i, cliente in enumerate(clientes, start=1):
                    print(f"{i}. {cliente.informacion()}")

                try:
                    opcion = int(input("Seleccione el cliente: "))
                    if 1 <= opcion <= len(clientes):
                        cliente = clientes[opcion - 1]
                        print(f"\n- {cliente.getCargo()} {cliente.getNombre()} con cédula {cliente.getCedula()} seleccionado.")
                        break
                    else:
                        print("- Opción inválida, por favor intente de nuevo.")
                except ValueError:
                    print("- Opción inválida, por favor intente de nuevo.")
            break
        elif registrado == 'n':
            nombre = input("Ingrese el nombre del cliente: ")
            cedula = int(input("Ingrese la cédula del cliente: "))
            nuevo_cliente = Cliente(nombre, cedula)
            clientes.append(nuevo_cliente)
            print(f"\nCliente {nombre} con cédula {cedula} creado con éxito.")
            break
        else:
            print("- Opción inválida, por favor intente de nuevo.")
    orden = Orden(supermercado, empleado, cliente)

    while True:
        print("\n=== Qué desea hacer? ===")
        print("1. Agregar producto a la orden")
        print("2. Remover producto de la orden")
        print("3. Ver productos en la orden")
        print("4. Finalizar orden")
        print("5. Cancelar orden")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                print("agregarProducto")
                agregarProducto(orden)
            elif opcion == 2:
                print("quitar_producto")
                quitarProducto(orden)
            elif opcion == 3:
                print("mostrar_orden")
                mostrarOrden(orden)
            elif opcion == 4:
                    if len(orden.getProductos()) != 0:
                        orden.completarOrden()
                        print(barraDeSeparacion)
                        print("---Orden Completa---")
                    else:
                        print(barraDeSeparacion)
                        print("---La Orden no contiene productos---")
                        print("---Orden Cancelada---")
                    exit = True
                    break
            elif opcion == 5:
                print("--- Orden Cancelada ---")
                exit = True
                break
            else:
                print("- Opción inválida, por favor intente de nuevo.")
        except ValueError:
            print("- Opción inválida, por favor intente de nuevo.")
    pass

def agregarProducto(orden):
    tipo = None
    exit = False

    while not exit:
        print(barraDeSeparacion)
        print("=== Seleccione el tipo de producto a buscar ===\n")
        print("1. Aseo")
        print("2. Alimento")
        print("3. Bebida")
        print("4. Cuidado personal")
        print("5. Productos para mascotas")
        print("6. Otro")
        print("")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                tipo = TipoProducto.ASEO
                exit = True
            elif opcion == 2:
                tipo = TipoProducto.ALIMENTO
                exit = True
            elif opcion == 3:
                tipo = TipoProducto.BEBIDA
                exit = True
            elif opcion == 4:
                tipo = TipoProducto.CUIDADOPERSONAL
                exit = True
            elif opcion == 5:
                tipo = TipoProducto.MASCOTA
                exit = True
            elif opcion == 6:
                tipo = TipoProducto.OTRO
                exit = True
            else:
                print(barraDeSeparacion)
                print("- Opción inválida, por favor intente de nuevo.")
        except ValueError:
            print(barraDeSeparacion)
            print("- Opción inválida, por favor intente de nuevo.")

    lista1 = orden.getSupermercado().productosPorTipo(tipo)
    
    if len(lista1) == 0:
        print(barraDeSeparacion)
        print("No hay productos disponibles del tipo seleccionado.")
    else:
        print(barraDeSeparacion)
        print("=== Productos disponibles ===\n")
        for i, producto in enumerate(lista1, start=1):
            print(f"{i}. {producto.getNombre()}")

        opcionstr = input("\nDesea agregar algún producto al carrito? (s/n): ").lower()
        while opcionstr not in ["s", "n"]:
            opcionstr = input("- Opción inválida, por favor intente de nuevo: ").lower()

        if opcionstr == "s":
            while True:
                try:
                    opcionproducto = int(input("Seleccione el producto a agregar: "))
                    if 1 <= opcionproducto <= len(lista1):
                        break
                    else:
                        print("- Opción inválida, por favor intente de nuevo.")
                except ValueError:
                    print("- Opción inválida, por favor intente de nuevo.")

            unienof = []
            unisinof = []

            for unidad in lista1[opcionproducto - 1].getUnidades(orden.getSupermercado()):
                if unidad.isOferta():
                    unienof.append(unidad)
                else:
                    unisinof.append(unidad)

            print(barraDeSeparacion)
            print("=== Unidades disponibles=== \n")
            i = 0
            if unisinof:
                i += 1
                print(f"{i}. Sin oferta - ${lista1[opcionproducto - 1].getPrecio()} cantidad disponible: {len(unisinof)}")
            for unidad in unienof:
                i += 1
                print(f"{i}. {unidad.calcularOferta().getNombre()}({unidad.calcularOferta().getPorcentajeDescuento()}%) ${unidad.calcularPrecio()}")

            opcionstr2 = input("Desea agregar alguna unidad? (s/n): ").lower()
            while opcionstr2 not in ["s", "n"]:
                print(barraDeSeparacion)
                print("- Opción inválida, por favor intente de nuevo.")
                opcionstr2 = input("Desea agregar alguna unidad? (s/n): ").lower()

            if opcionstr2 == "s":
                while True:
                    try:
                        opcion = int(input("Seleccione la unidad a agregar: "))
                        if 1 <= opcion <= i:
                            break
                        else:
                            print("- Opción inválida, por favor intente de nuevo.")
                    except ValueError:
                        print("- Opción inválida, por favor intente de nuevo.")

                if opcion == 1 and unisinof:
                    while True:
                        try:
                            cantidad = int(input("Ingrese el número de unidades a agregar: "))
                            if 0 <= cantidad <= len(unisinof):
                                orden.agregarProducto(orden.getSupermercado(), lista1[opcionproducto - 1], cantidad)
                                print("Producto(s) agregado(s) a la orden.")
                                break
                            else:
                                print("- Opción inválida, por favor intente de nuevo.")
                        except ValueError:
                            print("- Opción inválida, por favor intente de nuevo.")
                else:
                    orden.agregarUnidad(unienof[opcion - 2 if unisinof else opcion - 1])
                    print("Producto agregado a la orden.")

def quitarProducto(orden):
    exit = False
    while not exit:
        unidades = orden.getProductos()
        print(barraDeSeparacion)
        print("=== Producto(s) actualmente en la orden ===\n")
        for i, unidad in enumerate(unidades, start=1):
            if unidad.isOferta():
                print(f"{i}. {unidad.getTipo().getNombre()} {unidad.calcularOferta().getNombre()}({unidad.calcularOferta().getPorcentajeDescuento()}%) ${unidad.calcularPrecio()}")
            else:
                print(f"{i}. {unidad.getTipo().getNombre()} ${unidad.calcularPrecio()}")

        i += 1
        print(f"{i}. Cancelar")

        try:
            opcion = int(input("Seleccione un producto para remover: "))
            if 1 <= opcion <= len(unidades):
                orden.quitarUnidad(unidades[opcion - 1])
                print("El producto se removió con éxito.")
            elif opcion == i:
                exit = True
        except ValueError:
            print("Opción inválida, por favor intente de nuevo.")

def mostrarOrden(orden):
    print(barraDeSeparacion)
    print(f"Orden id: {orden.getId()}")
    print(f"Supermercado: {orden.getSupermercado().getNombre()}")
    print(f"Empleado: {orden.getEmpleado().getNombre()}")
    print(f"Cliente: {orden.getCliente().getNombre()}")
    print("\nProductos en la orden:")
    for i, unidad in enumerate(orden.getProductos(), start=1):
        if unidad.isOferta():
            print(f"{i}. {unidad.getTipo().getNombre()} {unidad.calcularOferta().getNombre()}({unidad.calcularOferta().getPorcentajeDescuento()}%) ${unidad.calcularPrecio()}")
        else:
            print(f"{i}. {unidad.getTipo().getNombre()} ${unidad.calcularPrecio()}")
    print(f"\nPrecio total: ${orden.calcularPrecioTotal()}")
    print(barraDeSeparacion)

#F2
def administarInventario():
    print("F2")
    pass


#F3
def intercambioProductos():
    supermercados = []
    sci = input  # Para capturar entradas del usuario
    scni = input  # Se usará para las opciones

    for supermercado in Supermercado.getSupermercados():
        supermercados.append(supermercado)

    supermercado1 = None
    supermercado2 = None

    while True:
        print(barraDeSeparacion)
        print("=== Lista de Supermercados ===\n")
        for i, sup in enumerate(supermercados, 1):
            print(f"{i}. {sup.getNombre()}")
        
        print("")
        opcion = int(input("Seleccione el primer supermercado: "))
        
        # Validación de la opción
        while opcion < 1 or opcion > len(supermercados):
            print(barraDeSeparacion)
            print("- Opción inválida, por favor intente de nuevo.")
            for i, sup in enumerate(supermercados, 1):
                print(f"{i}. {sup.getNombre()}")
            print("")
            opcion = int(input("Seleccione el primer supermercado: "))

        supermercado1 = supermercados.pop(opcion - 1)
        print(f"{barraDeSeparacion}\n- Supermercado {supermercado1.getNombre()} seleccionado.")
        break

    while True:
        print(barraDeSeparacion)
        print("=== Lista de Supermercados ===\n")
        for i, sup in enumerate(supermercados, 1):
            print(f"{i}. {sup.getNombre()}")
        
        print("")
        opcion = int(input("Seleccione el segundo supermercado: "))
        
        # Validación de la opción
        while opcion < 1 or opcion > len(supermercados):
            print(barraDeSeparacion)
            print("- Opción inválida, por favor intente de nuevo.")
            for i, sup in enumerate(supermercados, 1):
                print(f"{i}. {sup.getNombre()}")
            print("")
            opcion = int(input("Seleccione el segundo supermercado: "))

        supermercado2 = supermercados.pop(opcion - 1)
        print(f"{barraDeSeparacion}\n- Supermercado {supermercado2.getNombre()} seleccionado.")
        break

    # Mostrar productos en cada supermercado
    for prod in Producto.getListaProductos():
        i = sum(1 for bodega in supermercado1.getBodegas() for unidad in bodega.getProductos() if unidad.getTipo().getNombre() == prod.getNombre())
        print(f"{barraDeSeparacion}\nEn {supermercado1.getNombre()} había(n) inicialmente {supermercado1.numeroUnidades(prod)} unidades de {prod.getNombre()}")
        print(f"Actualmente hay {i} unidades")

    for producto in Producto.getListaProductos():
        i = sum(1 for bodega in supermercado2.getBodegas() for unidad in bodega.getProductos() if unidad.getTipo().getNombre() == producto.getNombre())
        print(f"{barraDeSeparacion}\nEn {supermercado2.getNombre()} había(n) inicialmente {supermercado2.numeroUnidades(producto)} unidades de {producto.getNombre()}")
        print(f"Actualmente hay {i} unidades")

    # Confirmar intercambio de productos
    select = input("\n¿Desea intercambiar productos entre los supermercados? (s/n): ").strip().lower()
    while select not in ['s', 'n']:
        select = input("- Opción inválida, por favor intente de nuevo: ").strip().lower()

    if select == 's':
        envia, recibe = None, None
        while True:
            print(f"{barraDeSeparacion}\n=== Supermercado que enviará los productos ===\n1. {supermercado1.getNombre()}\n2. {supermercado2.getNombre()}\n")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                envia = supermercado1
                recibe = supermercado2
                break
            elif opcion == 2:
                envia = supermercado2
                recibe = supermercado1
                break
            else:
                print("{barraDeSeparacion}\n- Opción inválida, por favor intente de nuevo.")
        
        # Intercambio de productos
        productosenv = [unidad.getTipo() for bodega in envia.getBodegas() for unidad in bodega.getProductos() if unidad.getTipo() not in productosenv]

        print("{barraDeSeparacion}\n=== Productos disponibles para enviar ===\n")
        for i, p in enumerate(productosenv, 1):
            print(f"{i}. {p.getNombre()}")

        opcion = int(input("\nSeleccione una opción: "))
        seleccionado = productosenv[opcion - 1]

        unidades = [unidad for bodega in envia.getBodegas() for unidad in bodega.getProductos() if unidad.getTipo() == seleccionado]

        print("{barraDeSeparacion}\n=== Unidades disponibles para enviar ===\n")
        for i, unidad in enumerate(unidades, 1):
            if not unidad.isOferta():
                print(f"{i}. {unidad.getTipo().getNombre()} Sin oferta")
            else:
                oferta = unidad.calcularOferta()
                print(f"{i}. {unidad.getTipo().getNombre()} {oferta.getNombre()}({oferta.getPorcentajeDescuento()}%)")
        
        opcion = int(input("\nSeleccione una opción: "))
        unienv = unidades[opcion - 1]

        print(f"{barraDeSeparacion}\n{unienv.getTipo().getNombre()} con código {unienv.getCodigo()} enviado de {unienv.getUbicacion().getNombre()} a {recibe.getNombre()}")
        recibe.getBodegas()[0].agregarProducto(unienv)
        unienv.getUbicacion().quitarProducto(unienv)
        unienv.setUbicacion(recibe.getBodegas()[0])


def verificarVencimiento(supermercado, dias=0):
    for bodega in supermercado.getBodegas():
        for unidad in bodega.getProductos():
            dias_para_vencimiento = unidad.diasParaVencimiento()
            if dias_para_vencimiento <= dias:
                if dias_para_vencimiento > 0:
                    print(f"Al producto {unidad.getTipo().getNombre()} con código {unidad.getCodigo()}, ubicado en {bodega.getNombre()} le quedan {dias_para_vencimiento} días para vencer.")
                elif dias_para_vencimiento == 0:
                    print(f"El producto {unidad.getTipo().getNombre()} con código {unidad.getCodigo()}, ubicado en {bodega.getNombre()} se vence hoy.")
                else:
                    print(f"El producto {unidad.getTipo().getNombre()} con código {unidad.getCodigo()}, ubicado en {bodega.getNombre()} se venció hace {-dias_para_vencimiento} días.")










#Switch principal

exit = False
while not exit:
    print(barraDeSeparacion)
    print("=== Menú Principal ===\n")
    print("1. Nueva orden de compra")
    print("2. Manejo de Inventario")
    print("3. Salir")
    print("")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor ingrese un número entero.")
        continue

    if opcion == 1:
        crearOrden()
    elif opcion == 2:
        et = False
        while not et:
            print(barraDeSeparacion)
            print("=== Que desea hacer ===\n")
            print("1. Descuentos por vencimiento")
            print("2. Intercambio de productos entre supermercados")
            print("3. Surtir")
            print("")
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Por favor ingrese un número entero.")
                continue

            if opcion == 1:
                et = True
            elif opcion == 2:
                intercambioProductos()
                et = True
            elif opcion == 3:
                #surtir()
                et = True
            else:
                print(barraDeSeparacion)
                print("- Opción inválida, por favor intente de nuevo.")
    elif opcion == 3:
        exit = True
    else:
        print("Opción inválida, por favor intente de nuevo.")