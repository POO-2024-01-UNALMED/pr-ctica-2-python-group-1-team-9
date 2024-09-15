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
from baseDatos.Serializacion import Serializacion

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
def contarTiposDiferentes(unidades):
    tipos_unicos = []
    for unidad in unidades:
        if unidad.getTipo().getTipo() not in tipos_unicos:
            tipos_unicos.append(unidad.getTipo().getTipo())
    print("Retornando:", len(tipos_unicos))
    return len(tipos_unicos)


def administrarInventario():
    supermercados = Supermercado.getSupermercados()
    personas = Persona.getPersonas()
    empleados = []

    print("______________________________________________________________________________________________________")
    print("Lista de Supermercados:\n")
    for idx, supermercado in enumerate(supermercados, start=1):
        print(f"{idx}. {supermercado.getNombre()}")

    opcion = int(input("Seleccione un supermercado: "))
    while opcion < 1 or opcion > len(supermercados):
        opcion = int(input("- Opción inválida, por favor intente de nuevo: "))

    supermercado = supermercados[opcion - 1]
    empleados = supermercado.getEmpleados()
    print(f"- Supermercado {supermercado.getNombre()} seleccionado.")

    print("\nLista de Empleados:")
    for idx, empleado in enumerate(empleados, start=1):
        print(f"{idx}. {empleado.getCargo()} {empleado.getNombre()}")

    opcion = int(input("\nSeleccione empleado encargado: "))
    while opcion < 1 or opcion > len(empleados):
        opcion = int(input("- Opción inválida, por favor intente de nuevo: "))

    empleado = empleados[opcion - 1]
    print(f"- {empleado.getCargo()} {empleado.getNombre()} seleccionado.\n")

    eleccion1 = int(input("Ingrese los días para la búsqueda: "))
    while eleccion1 < 0:
        eleccion1 = int(input("- Opción inválida, por favor intente de nuevo: "))

    bodegas = supermercado.getBodegas()
    unidades = []
    avencer = []

    for bodega in bodegas:
        unidades.extend(bodega.getProductos())

    for unidad in unidades:
        dias = unidad.diasParaVencimiento()
        if dias <= eleccion1:
            avencer.append(unidad)

    avencer.sort(key=lambda u: u.diasParaVencimiento())

    if not avencer:
        print("No hay productos próximos a vencer en ese plazo.")
    else:
        print("______________________________________________________________________________________________________\nEstos son los productos vencidos o próximos a vencer:\n")
        for unidad in avencer:
            if unidad.diasParaVencimiento() <= 0:
                print(f"Nombre: {unidad.getTipo().getNombre()}, Código: {unidad.getCodigo()}, Ubicación: {unidad.getUbicacion().getNombre()}, VENCIDO")
                unidad.getUbicacion().quitarProducto(unidad)
            else:
                print(f"Nombre: {unidad.getTipo().getNombre()}, Código: {unidad.getCodigo()}, Ubicación: {unidad.getUbicacion().getNombre()}, Días para vencer: {unidad.diasParaVencimiento()}")

        disponibles = sum(1 for unidad in avencer if unidad.diasParaVencimiento() > 0)
        if disponibles > 0:
            print("______________________________________________________________________________________________________\nProductos disponibles para hacerle descuentos:")
        else:
            print("No hay productos disponibles para hacer descuentos.")

        for unidad in avencer:
            if unidad.diasParaVencimiento() > 0:
                print(f"\n->Nombre: {unidad.getTipo().getNombre()}, Código: {unidad.getCodigo()}, Días para vencer: {unidad.diasParaVencimiento()}")
                if not unidad.getDescuentos():
                    eleccion2 = input("  No tiene descuentos disponibles ¿desea crear uno? (s/n): ").lower()
                    while eleccion2 not in ['s', 'n']:
                        eleccion2 = input("- Opción inválida, por favor intente de nuevo: ").lower()
                    if eleccion2 == 's':
                        nombreDescuento = input("  Ingrese el nombre del descuento: ")
                        porcentajeDescuento = int(input("  Ingrese el porcentaje de descuento: "))
                        Descuento(nombreDescuento, unidad, porcentajeDescuento)
                else:
                    mejorOferta = unidad.calcularOferta()
                    print(f"  Mejor descuento: Nombre del descuento: '{mejorOferta.getNombre()}', Descuento: {mejorOferta.getPorcentajeDescuento()}% (Antes: {unidad.getTipo().getPrecio()} Ahora: {unidad.calcularPrecio()})")
                    eleccion3 = input("  ¿Desea agregar un mejor descuento? (s/n): ").lower()
                    while eleccion3 not in ['s', 'n']:
                        eleccion3 = input("- Opción inválida, por favor intente de nuevo: ").lower()
                    if eleccion3 == 's':
                        nombreDescuento = input("  Ingrese el nombre del descuento: ")
                        porcentajeDescuento = int(input("  Ingrese el porcentaje de descuento: "))
                        Descuento(nombreDescuento, unidad, porcentajeDescuento)

        disponiblesParaPaquetes = [unidad for unidad in avencer if unidad.diasParaVencimiento() > 0]
        tipos = set(unidad.getTipo().getTipo() for unidad in disponiblesParaPaquetes)

        if len(tipos) > 1:
            eleccion4 = input("\n¿Desea crear paquetes de promociones? (s/n): ").lower()
            while eleccion4 not in ['s', 'n']:
                eleccion4 = input("- Opción inválida, por favor intente de nuevo: ").lower()
            if eleccion4 == 's':
                while True:
                    paquete = []
                    tiposDisp = list(tipos)
                    for unidad in disponiblesParaPaquetes:
                        if unidad.getTipo().getTipo() in tiposDisp and not unidad.getEnPaquete():
                            paquete.append(unidad)
                            unidad.setEnPaquete(True)
                            unidad.getUbicacion().getProductos().remove(unidad)
                            tiposDisp.remove(unidad.getTipo().getTipo())
                    if len(paquete) > 1:
                        supermercado.agregarPaquetePromocion(paquete)
                    else:
                        for uni in paquete:
                            uni.setEnPaquete(False)
                            uni.getUbicacion().getProductos().append(uni)
                        break
                print("______________________________________________________________________________________________________")
                print("Paquetes creados.")
                for i, paquete in enumerate(supermercado.getPaquetesPromocion(), start=1):
                    valorPromo = sum(u.calcularPrecio() for u in paquete)
                    print(f"______________________________________________________________________________________________________\nPaquete #{i} Precio: {valorPromo}")
                    for u in paquete:
                        print(f"Producto: {u.getTipo().getNombre()} Código: {u.getCodigo()}")
                    eleccion5 = input("\n¿Desea hacer descuento al precio? (s/n): ").lower()
                    while eleccion5 not in ['s', 'n']:
                        eleccion5 = input("- Opción inválida, por favor intente de nuevo: ").lower()
                    if eleccion5 == 's':
                        descuentoPaquete = int(input("Ingrese el descuento que desea: "))
                        for u in paquete:
                            if u.calcularPrecio() == u.getTipo().getPrecio():
                                Descuento(None, u, descuentoPaquete)
                            else:
                                u.calcularOferta().setPorcentajeDescuento(
                                    (u.calcularOferta().getPorcentajeDescuento() * descuentoPaquete / 100) + u.calcularOferta().getPorcentajeDescuento()
                                )
                        valorPromo = sum(u.calcularPrecio() for u in paquete)
                        print(f"______________________________________________________________________________________________________\nPaquete #{i} Precio con descuento: {valorPromo}")
        else:
            print("No hay suficientes productos para crear paquetes promocionados.")




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

    uni1 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod1)
    uni2 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod1)
    uni3 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod1)
    uni4 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod2)
    uni5 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod2)
    uni6 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod3)
    uni7 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod3)
    uni8 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod3)
    uni9 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod4)
    uni10 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod4)
    uni11 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod4)
    uni12 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod4)
    uni13 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod4)
    uni14 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod5)
    uni15 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod5)
    uni16 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod5)
    uni17 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod5)
    uni18 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod6)
    uni19 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod6)
    uni20 = Unidad(Unidad.generarFechaVencimiento(), prod1, bod6)

    uni21 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod1)
    uni22 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod1)
    uni23 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod1)
    uni24 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod1)
    uni25 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod2)
    uni26 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod3)
    uni27 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod3)
    uni28 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod4)
    uni29 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod4)
    uni30 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod4)
    uni31 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod4)
    uni32 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod4)
    uni33 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod4)
    uni34 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod5)
    uni35 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod5)
    uni36 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod5)
    uni37 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod5)
    uni38 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod5)
    uni39 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod6)
    uni40 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod6)
    uni41 = Unidad(Unidad.generarFechaVencimiento(), prod2, bod7)
    
    uni42 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod1)
    uni43 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod1)
    uni44 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod1)
    uni45 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod2)
    uni46 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod2)
    uni47 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod2)
    uni48 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod3)
    uni49 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod3)
    uni50 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod3)
    uni51 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod4)
    uni52 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod4)
    uni53 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod5)
    uni54 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod5)
    uni55 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod5)
    uni56 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod6)
    uni57 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod6)
    uni58 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod7)
    uni59 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod7)
    uni60 = Unidad(Unidad.generarFechaVencimiento(), prod3, bod7)

    uni61 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod1)
    uni62 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod1)
    uni63 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod1)
    uni64 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod2)
    uni65 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod2)
    uni66 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod2)
    uni67 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod3)
    uni68 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod3)
    uni69 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod3)
    uni70 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod3)
    uni71 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod4)
    uni72 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod4)
    uni73 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod5)
    uni74 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod5)
    uni75 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod5)
    uni76 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod6)
    uni77 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod6)
    uni78 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod7)
    uni79 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod7)
    uni80 = Unidad(Unidad.generarFechaVencimiento(), prod4, bod7)

    uni81 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod2)
    uni82 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod2)
    uni83 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod2)
    uni84 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod2)
    uni85 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod3)
    uni86 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod3)
    uni87 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod3)
    uni88 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod3)
    uni89 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod4)
    uni90 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod4)
    uni91 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod4)
    uni92 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod4)
    uni93 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod5)
    uni94 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod5)
    uni95 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod6)
    uni96 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod6)
    uni97 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod6)
    uni98 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod7)
    uni99 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod7)
    uni100 = Unidad(Unidad.generarFechaVencimiento(), prod5, bod7)

    uni101 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod1)
    uni102 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod1)
    uni103 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod1)
    uni104 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod1)
    uni105 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod2)
    uni106 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod3)
    uni107 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod3)
    uni108 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod4)
    uni109 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod4)
    uni110 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod5)
    uni111 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod5)
    uni112 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod5)
    uni113 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod6)
    uni114 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod6)
    uni115 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod6)
    uni116 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod6)
    uni117 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod7)
    uni118 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod7)
    uni119 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod7)
    uni120 = Unidad(Unidad.generarFechaVencimiento(), prod6, bod7)

    uni131 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod1)
    uni132 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod1)
    uni133 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod1)
    uni134 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod2)
    uni135 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod2)
    uni136 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod3)
    uni137 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod3)
    uni138 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod4)
    uni139 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod4)
    uni140 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod5)
    uni141 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod5)
    uni142 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod5)
    uni143 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod6)
    uni144 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod6)
    uni145 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod6)
    uni146 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod7)
    uni147 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod7)
    uni148 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod7)
    uni149 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod7)
    uni150 = Unidad(Unidad.generarFechaVencimiento(), prod7, bod7)

    uni151 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod1)
    uni152 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod1)
    uni153 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod1)
    uni154 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod1)
    uni155 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod2)
    uni156 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod3)
    uni157 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod3)
    uni158 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod4)
    uni159 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod4)
    uni160 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod4)
    uni161 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod4)
    uni162 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod4)
    uni163 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod6)
    uni164 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod6)
    uni165 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod6)
    uni166 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod6)
    uni167 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod6)
    uni168 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod6)
    uni169 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod7)
    uni170 = Unidad(Unidad.generarFechaVencimiento(), prod8, bod7)
    
    #descuento_uno = Descuento("Refrescantes y baratas", TipoProducto.BEBIDA, 10)
    #descuento_dos = Descuento("Borrachera económica", prod2, 15)
    '''

    Serializacion.deserializar()
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
                    administrarInventario()
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
            Serializacion.serializar()
            exit = True
        else:
            print("Opción inválida, por favor intente de nuevo.")