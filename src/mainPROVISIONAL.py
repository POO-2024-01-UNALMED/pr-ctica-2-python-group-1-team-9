from gestorAplicacion.Persona import Persona
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Orden import Orden
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Unidad import Unidad
from gestorAplicacion.Descuento import Descuento
from gestorAplicacion.Bodega import Bodega
import pickle

barraDeSeparacion = "______________________________________________________________________________________________________"

#Funcionalidades

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
            if i == len(empleados):
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
            cliente = nuevo_cliente
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
                agregarProducto(orden)
            elif opcion == 2:
                quitarProducto(orden)
            elif opcion == 3:
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
                orden.cancelarOrden()
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

            for unidad in lista1[opcionproducto - 1].getUnidadesDelSupermercado(orden.getSupermercado()):
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
    if len(orden.getProductos()) == 0:
        print("\n---No hay productos en la orden---")
    else:
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
                print(f"{barraDeSeparacion}\n- Opción inválida, por favor intente de nuevo.")
        
        # Intercambio de productos
        productosenv = []
        for bodega in envia.getBodegas():
            for unidad in bodega.getProductos():
                TipoAVerificar = unidad.getTipo()
                if TipoAVerificar not in productosenv:
                    productosenv.append(TipoAVerificar)

        print(f"{barraDeSeparacion}\n=== Productos disponibles para enviar ===\n")
        for i, p in enumerate(productosenv, 1):
            print(f"{i}. {p.getNombre()}")

        opcion = int(input("\nSeleccione una opción: "))
        seleccionado = productosenv[opcion - 1]

        unidades = [unidad for bodega in envia.getBodegas() for unidad in bodega.getProductos() if unidad.getTipo() == seleccionado]

        print(f"{barraDeSeparacion}\n=== Unidades disponibles para enviar ===\n")
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





def deserializar():
    pkldescuentos = open("src/tmp/descuentos.pkl", "rb")
    pklpersonas = open("src/tmp/personas.pkl", "rb")
    pklproductos = open("src/tmp/productos.pkl", "rb")
    pklsupermercados = open("src/tmp/supermercados.pkl", "rb")
    try:
        Descuento.setDescuentos(pickle.load(pkldescuentos))
    except EOFError:
        print("El archivo de descuentos está vacio")
    try:
        Persona.setPersonas(pickle.load(pklpersonas))
    except EOFError:
        print("El archivo de personas está vacio")
    try:
        Producto.setListaProductos(pickle.load(pklproductos))
    except EOFError:
        print("El archivo de productos está vacio")
    try:
        Supermercado.setSupermercados(pickle.load(pklsupermercados))
    except EOFError:
        print("El archivo de supermercados está vacio")
    pkldescuentos.close()
    pklpersonas.close()
    pklproductos.close()
    pklsupermercados.close()
    
def serializar():
    pkldescuentos = open("src/tmp/descuentos.pkl", "wb")
    pklpersonas = open("src/tmp/personas.pkl", "wb")
    pklproductos = open("src/tmp/productos.pkl", "wb")
    pklsupermercados = open("src/tmp/supermercados.pkl", "wb")
    descuentos = Descuento.getDescuentos()
    personas = Persona.getPersonas()
    productos = Producto.getListaProductos()
    supermercados = Supermercado.getSupermercados()
    pickle.dump(descuentos, pkldescuentos)
    pickle.dump(personas, pklpersonas)
    pickle.dump(productos, pklproductos)
    pickle.dump(supermercados, pklsupermercados)
    pkldescuentos.close()
    pklpersonas.close()
    pklproductos.close()
    pklsupermercados.close()




#Switch principal
if __name__ == "__main__":

    '''
    sup1 = Supermercado("MercaChicles", 1000000)
    sup2 = Supermercado("El Gangazo", 12000000)
    sup3 = Supermercado("Mercatodo", 900000)
    emp1 = Empleado("Pepe Pineda", 12345, sup1, "Ventas", 2000000)
    emp2 = Empleado("Pancho Alzate", 65485, sup1, "Asesor", 2500000)
    emp3 = Empleado("Juanito Alimana", 666999, sup1, "Ventas", 2100000)
    emp4 = Empleado("Pedro Navaja", 963258, sup2, "Ventas", 2000000)
    emp5 = Empleado("Betty Lafea", 467852, sup2, "Secretaria", 2400000)
    emp6 = Empleado("Jose Rodriguez", 643816, sup2, "Asesor", 2450000)
    emp7 = Empleado("Lucho Diaz", 4736512, sup3, "Ventas", 2010000)
    emp8 = Empleado("Betty Lafea", 467852, sup3, "Ventas", 1950000)
    emp9 = Empleado("Willie Colon", 864325, sup3, "Caja", 2005000)
    cli1 = Cliente("Jaimito Maravilla", 23456)
    cli2 = Cliente("Pedro Escamoso", 411359)
    cli3 = Cliente("Lucas Tadeo", 435864)
    cli4 = Cliente("Alfredo Mercurio", 943567)
    cli5 = Cliente("Axel Rosas", 73465)
    bod1 = Bodega("Bodega Principal", "Cordoba", sup1)
    bod2 = Bodega("Bodega Secundaria", "La Piedra", sup1)
    bod3 = Bodega("Bodega Terciaria", "El Monte", sup1)
    bod4 = Bodega("Bodega La Esquinita", "La Esquina", sup2)
    bod5 = Bodega("Bodega Medieval", "El pasado", sup2)
    bod6 = Bodega("Bodega El colchon", "La cama", sup3)
    bod7 = Bodega("Bodega Pollito", "Kokoriko", sup3)

    prod1 = Producto("leche Colanta", TipoProducto.ALIMENTO, 3000, 2000)
    prod2 = Producto("vodka Absoluti", TipoProducto.BEBIDA, 90000, 50000)
    prod3 = Producto("leche Alqueria", TipoProducto.ALIMENTO, 3100, 2100)
    prod4 = Producto("detergente Fav", TipoProducto.ASEO, 6500, 5000)
    prod5 = Producto("jabón Dove", TipoProducto.CUIDADOPERSONAL, 18900, 13450)
    prod6 = Producto("cuido Dog Chow", TipoProducto.MASCOTA, 125000, 98000)
    prod7 = Producto("spray Raid", TipoProducto.OTRO, 17000, 15100)
    prod8 = Producto("cepillo Pro 425", TipoProducto.CUIDADOPERSONAL, 4700, 3000)

    uni1 = Unidad("2024-09-20", prod1, bod1)
    uni2 = Unidad("2024-08-01", prod1, bod1)
    uni3 = Unidad("2024-10-05", prod1, bod1)
    uni4 = Unidad("2024-09-20", prod1, bod2)
    uni5 = Unidad("2024-08-01", prod1, bod2)
    uni6 = Unidad("2024-10-05", prod1, bod3)
    uni7 = Unidad("2024-09-20", prod1, bod3)
    uni8 = Unidad("2024-08-01", prod1, bod3)
    uni9 = Unidad("2024-10-05", prod1, bod4)
    uni10 = Unidad("2024-09-20", prod1, bod4)
    uni11 = Unidad("2024-08-01", prod1, bod4)
    uni12 = Unidad("2024-08-01", prod1, bod4)
    uni13 = Unidad("2024-10-05", prod1, bod4)
    uni14 = Unidad("2024-09-20", prod1, bod5)
    uni15 = Unidad("2024-08-01", prod1, bod5)
    uni16 = Unidad("2024-10-05", prod1, bod5)
    uni17 = Unidad("2024-09-20", prod1, bod5)
    uni18 = Unidad("2024-08-01", prod1, bod6)
    uni19 = Unidad("2024-10-05", prod1, bod6)
    uni20 = Unidad("2024-10-05", prod1, bod6)

    uni21 = Unidad("2024-09-20", prod2, bod1)
    uni22 = Unidad("2024-08-01", prod2, bod1)
    uni23 = Unidad("2024-10-05", prod2, bod1)
    uni24 = Unidad("2024-09-20", prod2, bod1)
    uni25 = Unidad("2024-08-01", prod2, bod2)
    uni26 = Unidad("2024-10-05", prod2, bod3)
    uni27 = Unidad("2024-09-20", prod2, bod3)
    uni28 = Unidad("2024-08-01", prod2, bod4)
    uni29 = Unidad("2024-10-05", prod2, bod4)
    uni30 = Unidad("2024-09-20", prod2, bod4)
    uni31 = Unidad("2024-08-01", prod2, bod4)
    uni32 = Unidad("2024-10-05", prod2, bod4)
    uni33 = Unidad("2024-10-05", prod2, bod4)
    uni34 = Unidad("2024-09-20", prod2, bod5)
    uni35 = Unidad("2024-08-01", prod2, bod5)
    uni36 = Unidad("2024-10-05", prod2, bod5)
    uni37 = Unidad("2024-09-20", prod2, bod5)
    uni38 = Unidad("2024-08-01", prod2, bod5)
    uni39 = Unidad("2024-10-05", prod2, bod6)
    uni40 = Unidad("2024-10-05", prod2, bod6)

    uni10 = Unidad("2024-09-30", prod4, bod2)
    uni11 = Unidad("2024-07-08", prod4, bod1)
    uni12 = Unidad("2024-11-27", prod4, bod1)
    uni13 = Unidad("2024-12-08", prod5, bod2)
    uni14 = Unidad("2024-10-20", prod5, bod1)
    uni15 = Unidad("2024-09-27", prod6, bod2)
    uni16 = Unidad("2025-01-30", prod6, bod1)

    descuento_uno = Descuento("Refrescantes y baratas", TipoProducto.BEBIDA, 10)
    descuento_dos = Descuento("Borrachera económica", prod2, 15)
    '''

    deserializar()
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
            serializar()
            exit = True
        else:
            print("Opción inválida, por favor intente de nuevo.")