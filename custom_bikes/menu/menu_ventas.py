from custom_bikes.funciones.funciones_clientes import agregar_cliente_csv
from custom_bikes.funciones.funciones_ventas import agregar_venta_csv, agregar_venta_cliente_nuevo, agregar_venta_cliente_existente, eliminar_venta, modificar_venta, buscar_venta, mostrar_ventas

def menu_ventas():
    
    while True:
        print('Ventas')
        print('1. Agregar venta')
        print('2. Eliminar venta')
        print('3. Modificar venta')
        print('4. Buscar venta')
        print('5. Mostrar ventas')
        print('6. Volver al menú principal')

        seleccion = int(input('Seleccione una opción: '))

        if seleccion == 1:
            print('Agregar venta')
            agregar_venta()

        elif seleccion == 2:
            print('Eliminar venta')
            pedido_id_seleccionado = input("Ingrese el ID del pedido a eliminar: ")
            eliminar_venta(pedido_id_seleccionado)

        elif seleccion == 3:
            print('Modificar venta')
            pedido_id_seleccionado = input("Ingrese el ID del pedido a modificar: ")
            modificar_venta(pedido_id_seleccionado)

        elif seleccion == 4:
            print('Buscar venta')
            pedido_id_seleccionado = input("Ingrese el ID del pedido a buscar: ")
            buscar_venta(pedido_id_seleccionado)

        elif seleccion == 5:
            print('Mostrar ventas')
            mostrar_ventas()

        elif seleccion == 6:
            print('Volver al menú principal')
            break
    
        else:
            print('Opción inválida')

def agregar_venta():

    print('1. Agregar venta (csv)')
    print('2. Generar venta')
    seleccion_ingreso_data = int(input('Seleccione una opción: '))

    if seleccion_ingreso_data == 1:
        print('Agregar ventas (csv)')
        agregar_cliente_csv()
        agregar_venta_csv()
        print('Ventas agregadas exitosamente')
    
    elif seleccion_ingreso_data == 2:
        print('Generar venta')

        while True:
            print('Seleccione el cliente')
            print('1. Cliente nuevo')
            print('2. Cliente existente')

            seleccion_cliente = int(input('Seleccione una opción: '))

            if seleccion_cliente == 1:

                print('Cliente nuevo')
                agregar_venta_cliente_nuevo()
                break

            elif seleccion_cliente == 2:

                print('Cliente existente')
                agregar_venta_cliente_existente()
                break
        
            else:
                print('Opción inválida')