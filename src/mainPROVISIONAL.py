from gestorAplicacion.Persona import Persona
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Orden import Orden
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Producto import Producto
import Intento_serializar

#creamos listas para serializar los elementos 
Lista_supermercados= Supermercado.get_supermercados


#Funcionalidades

#F1
supermercado1 = Supermercado(nombre="Supermercado Central", saldo=5000.0)
clientes = [Cliente(nombre="Julian", cedula="1"), Cliente("Julio", "2")]
empleado1 = [Empleado(nombre="Guzman", cedula="2", supermercado=supermercado1, cargo="Empleado", salario="100"), Empleado(nombre="David", cedula="22", supermercado=supermercado1, cargo="Empleado", salario="100")]
supermercado1.agregar_empleado(empleado1)

def crearOrden():
    supermercados = Supermercado.get_supermercados()
    personas = Persona.get_personas()
    clientes = [persona for persona in personas if persona.get_cargo() == "Cliente"]

    while True:
        print("\n=== Lista de Supermercados ===")
        for i, sup in enumerate(supermercados, 1):
            print(f"{i}. {sup.get_nombre()}")

        try:
            opcion = int(input("Seleccione un supermercado: "))
            if 1 <= opcion <= len(supermercados):
                supermercado = supermercados[opcion - 1]
                print(f"\n- Supermercado {supermercado.get_nombre()} seleccionado.")
                break
            else:
                print("- Opción inválida, por favor intente de nuevo.")
        except ValueError:
            print("- Opción inválida, por favor intente de nuevo.")

    empleados = supermercado.get_empleados()

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
                print(f"\n- {empleado.get_cargo()} {empleado.get_nombre()} seleccionado.")
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
                        print(f"\n- {cliente.get_cargo()} {cliente.get_nombre()} con cédula {cliente.get_cedula()} seleccionado.")
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
                print("agregar_producto")
                agregar_producto(orden)
            elif opcion == 2:
                print("quitar_producto")
                quitar_producto(orden)
            elif opcion == 3:
                print("mostrar_orden")
                mostrar_orden(orden)
            elif opcion == 4:
                    if len(orden.get_productos()) != 0:
                        orden.completar_orden()
                        print("______________________________________________________________________________________________________")
                        print("---Orden Completa---")
                    else:
                        print("______________________________________________________________________________________________________")
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

def agregar_producto(orden):
    tipo = None
    exit = False

    while not exit:
        print("______________________________________________________________________________________________________")
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
                print("______________________________________________________________________________________________________")
                print("- Opción inválida, por favor intente de nuevo.")
        except ValueError:
            print("______________________________________________________________________________________________________")
            print("- Opción inválida, por favor intente de nuevo.")

    lista1 = orden.get_supermercado().productos_por_tipo(tipo)
    
    if len(lista1) == 0:
        print("______________________________________________________________________________________________________")
        print("No hay productos disponibles del tipo seleccionado.")
    else:
        print("______________________________________________________________________________________________________")
        print("=== Productos disponibles ===\n")
        for i, producto in enumerate(lista1, start=1):
            print(f"{i}. {producto.get_nombre()}")

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

            for unidad in lista1[opcionproducto - 1].get_unidades(orden.get_supermercado()):
                if unidad.is_oferta():
                    unienof.append(unidad)
                else:
                    unisinof.append(unidad)

            print("______________________________________________________________________________________________________")
            print("=== Unidades disponibles=== \n")
            i = 0
            if unisinof:
                i += 1
                print(f"{i}. Sin oferta - ${lista1[opcionproducto - 1].get_precio()} cantidad disponible: {len(unisinof)}")
            for unidad in unienof:
                i += 1
                print(f"{i}. {unidad.calcular_oferta().get_nombre()}({unidad.calcular_oferta().get_porcentaje_descuento()}%) ${unidad.calcular_precio()}")

            opcionstr2 = input("Desea agregar alguna unidad? (s/n): ").lower()
            while opcionstr2 not in ["s", "n"]:
                print("______________________________________________________________________________________________________")
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
                                orden.agregar_producto(orden.get_supermercado(), lista1[opcionproducto - 1], cantidad)
                                print("Producto(s) agregado(s) a la orden.")
                                break
                            else:
                                print("- Opción inválida, por favor intente de nuevo.")
                        except ValueError:
                            print("- Opción inválida, por favor intente de nuevo.")
                else:
                    orden.agregar_unidad(unienof[opcion - 2 if unisinof else opcion - 1])
                    print("Producto agregado a la orden.")

def quitar_producto(orden):
    exit = False
    while not exit:
        unidades = orden.get_productos()
        print("______________________________________________________________________________________________________")
        print("=== Producto(s) actualmente en la orden ===\n")
        for i, unidad in enumerate(unidades, start=1):
            if unidad.is_oferta():
                print(f"{i}. {unidad.get_tipo().get_nombre()} {unidad.calcular_oferta().get_nombre()}({unidad.calcular_oferta().get_porcentaje_descuento()}%) ${unidad.calcular_precio()}")
            else:
                print(f"{i}. {unidad.get_tipo().get_nombre()} ${unidad.calcular_precio()}")

        i += 1
        print(f"{i}. Cancelar")

        try:
            opcion = int(input("Seleccione un producto para remover: "))
            if 1 <= opcion <= len(unidades):
                orden.quitar_unidad(unidades[opcion - 1])
                print("El producto se removió con éxito.")
            elif opcion == i:
                exit = True
        except ValueError:
            print("Opción inválida, por favor intente de nuevo.")

def mostrar_orden(orden):
    print("______________________________________________________________________________________________________")
    print(f"Orden id: {orden.get_id()}")
    print(f"Supermercado: {orden.get_supermercado().get_nombre()}")
    print(f"Empleado: {orden.get_empleado().get_nombre()}")
    print(f"Cliente: {orden.get_cliente().get_nombre()}")
    print("\nProductos en la orden:")
    for i, unidad in enumerate(orden.get_productos(), start=1):
        if unidad.is_oferta():
            print(f"{i}. {unidad.get_tipo().get_nombre()} {unidad.calcular_oferta().get_nombre()}({unidad.calcular_oferta().get_porcentaje_descuento()}%) ${unidad.calcular_precio()}")
        else:
            print(f"{i}. {unidad.get_tipo().get_nombre()} ${unidad.calcular_precio()}")
    print(f"\nPrecio total: ${orden.calcular_precio_total()}")
    print("______________________________________________________________________________________________________")

#F2
def administarInventario():
    print("F2")
    pass


#F3
def intercambioProductos():
    supermercados = []
    sci = input  # Para capturar entradas del usuario
    scni = input  # Se usará para las opciones

    for supermercado in Supermercado.get_supermercados():
        supermercados.append(supermercado)

    supermercado1 = None
    supermercado2 = None

    while True:
        print("______________________________________________________________________________________________________")
        print("=== Lista de Supermercados ===\n")
        for i, sup in enumerate(supermercados, 1):
            print(f"{i}. {sup.get_nombre()}")
        
        print("")
        opcion = int(input("Seleccione el primer supermercado: "))
        
        # Validación de la opción
        while opcion < 1 or opcion > len(supermercados):
            print("______________________________________________________________________________________________________")
            print("- Opción inválida, por favor intente de nuevo.")
            for i, sup in enumerate(supermercados, 1):
                print(f"{i}. {sup.get_nombre()}")
            print("")
            opcion = int(input("Seleccione el primer supermercado: "))

        supermercado1 = supermercados.pop(opcion - 1)
        print(f"______________________________________________________________________________________________________\n- Supermercado {supermercado1.get_nombre()} seleccionado.")
        break

    while True:
        print("______________________________________________________________________________________________________")
        print("=== Lista de Supermercados ===\n")
        for i, sup in enumerate(supermercados, 1):
            print(f"{i}. {sup.get_nombre()}")
        
        print("")
        opcion = int(input("Seleccione el segundo supermercado: "))
        
        # Validación de la opción
        while opcion < 1 or opcion > len(supermercados):
            print("______________________________________________________________________________________________________")
            print("- Opción inválida, por favor intente de nuevo.")
            for i, sup in enumerate(supermercados, 1):
                print(f"{i}. {sup.get_nombre()}")
            print("")
            opcion = int(input("Seleccione el segundo supermercado: "))

        supermercado2 = supermercados.pop(opcion - 1)
        print(f"______________________________________________________________________________________________________\n- Supermercado {supermercado2.get_nombre()} seleccionado.")
        break

    # Mostrar productos en cada supermercado
    for prod in Producto.get_lista_productos():
        i = sum(1 for bodega in supermercado1.get_bodegas() for unidad in bodega.get_productos() if unidad.get_tipo().get_nombre() == prod.get_nombre())
        print(f"______________________________________________________________________________________________________\nEn {supermercado1.get_nombre()} había(n) inicialmente {supermercado1.numero_unidades(prod)} unidades de {prod.get_nombre()}")
        print(f"Actualmente hay {i} unidades")

    for producto in Producto.get_lista_productos():
        i = sum(1 for bodega in supermercado2.get_bodegas() for unidad in bodega.get_productos() if unidad.get_tipo().get_nombre() == producto.get_nombre())
        print(f"______________________________________________________________________________________________________\nEn {supermercado2.get_nombre()} había(n) inicialmente {supermercado2.numero_unidades(producto)} unidades de {producto.get_nombre()}")
        print(f"Actualmente hay {i} unidades")

    # Confirmar intercambio de productos
    select = input("\n¿Desea intercambiar productos entre los supermercados? (s/n): ").strip().lower()
    while select not in ['s', 'n']:
        select = input("- Opción inválida, por favor intente de nuevo: ").strip().lower()

    if select == 's':
        envia, recibe = None, None
        while True:
            print(f"______________________________________________________________________________________________________\n=== Supermercado que enviará los productos ===\n1. {supermercado1.get_nombre()}\n2. {supermercado2.get_nombre()}\n")
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
                print("______________________________________________________________________________________________________\n- Opción inválida, por favor intente de nuevo.")
        
        # Intercambio de productos
        productosenv = [unidad.get_tipo() for bodega in envia.get_bodegas() for unidad in bodega.get_productos() if unidad.get_tipo() not in productosenv]

        print("______________________________________________________________________________________________________\n=== Productos disponibles para enviar ===\n")
        for i, p in enumerate(productosenv, 1):
            print(f"{i}. {p.get_nombre()}")

        opcion = int(input("\nSeleccione una opción: "))
        seleccionado = productosenv[opcion - 1]

        unidades = [unidad for bodega in envia.get_bodegas() for unidad in bodega.get_productos() if unidad.get_tipo() == seleccionado]

        print("______________________________________________________________________________________________________\n=== Unidades disponibles para enviar ===\n")
        for i, unidad in enumerate(unidades, 1):
            if not unidad.is_oferta():
                print(f"{i}. {unidad.get_tipo().get_nombre()} Sin oferta")
            else:
                oferta = unidad.calcular_oferta()
                print(f"{i}. {unidad.get_tipo().get_nombre()} {oferta.get_nombre()}({oferta.get_porcentaje_descuento()}%)")
        
        opcion = int(input("\nSeleccione una opción: "))
        unienv = unidades[opcion - 1]

        print(f"______________________________________________________________________________________________________\n{unienv.get_tipo().get_nombre()} con código {unienv.get_codigo()} enviado de {unienv.get_ubicacion().get_nombre()} a {recibe.get_nombre()}")
        recibe.get_bodegas()[0].agregar_producto(unienv)
        unienv.get_ubicacion().quitar_producto(unienv)
        unienv.set_ubicacion(recibe.get_bodegas()[0])


def verificar_vencimiento(supermercado, dias=0):
    for bodega in supermercado.get_bodegas():
        for unidad in bodega.get_productos():
            dias_para_vencimiento = unidad.dias_para_vencimiento()
            if dias_para_vencimiento <= dias:
                if dias_para_vencimiento > 0:
                    print(f"Al producto {unidad.get_tipo().get_nombre()} con código {unidad.get_codigo()}, ubicado en {bodega.get_nombre()} le quedan {dias_para_vencimiento} días para vencer.")
                elif dias_para_vencimiento == 0:
                    print(f"El producto {unidad.get_tipo().get_nombre()} con código {unidad.get_codigo()}, ubicado en {bodega.get_nombre()} se vence hoy.")
                else:
                    print(f"El producto {unidad.get_tipo().get_nombre()} con código {unidad.get_codigo()}, ubicado en {bodega.get_nombre()} se venció hace {-dias_para_vencimiento} días.")










#Switch principal

exit = False
while not exit:
    print("______________________________________________________________________________________________________")
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
            print("______________________________________________________________________________________________________")
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
                print("______________________________________________________________________________________________________")
                print("- Opción inválida, por favor intente de nuevo.")
    elif opcion == 3:
        exit = True
    else:
        print("Opción inválida, por favor intente de nuevo.")