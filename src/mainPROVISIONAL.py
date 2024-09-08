from gestorAplicacion.Persona import Persona
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Orden import Orden

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

    #orden = Orden(supermercado, empleado, cliente)

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
                print("agregar_producto")  #Aca va agregar_producto
            elif opcion == 2:
                print("quitar_producto")  #Aca va quitar_producto
            elif opcion == 3:
                print("mostrar_orden")  #Aca va mostrar_orden
            elif opcion == 4:
                    print("--- Orden Completa ---")
                    break
            elif opcion == 5:
                print("--- Orden Cancelada ---")
                break
            else:
                print("- Opción inválida, por favor intente de nuevo.")
        except ValueError:
            print("- Opción inválida, por favor intente de nuevo.")
    pass





#F2
def administarInventario():
    print("F2")
    pass





#F3
def intercambioProductos():
    print("F3")
    pass










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