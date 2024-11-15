from custom_bikes.funciones.funciones_clientes import insert_cliente, seleccionar_cliente, agregar_cliente_csv
from custom_bikes.funciones.funciones_ventas import seleccionar_componentes, agregar_cliente_csv
from custom_bikes.funciones.funciones_pedido import id_pedido

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
            eliminar_venta()

        elif seleccion == 3:
            print('Modificar venta')
            modificar_venta()

        elif seleccion == 4:
            print('Buscar venta')
            buscar_venta()

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
    
    elif seleccion_ingreso_data == 2:
        print('Generar venta')

        while True:
            print('Seleccione el cliente')
            print('1. Cliente nuevo')
            print('2. Cliente existente')

            seleccion_cliente = int(input('Seleccione una opción: '))

            if seleccion_cliente == 1:

                print('Cliente nuevo')

                rut_id = insert_cliente()
                pedido_id = id_pedido(rut_id)
                seleccionar_componentes(pedido_id)
                
                break

            elif seleccion_cliente == 2:
                cliente = seleccionar_cliente()
                rut_id = cliente[0]
                id_pedido_actual = id_pedido(rut_id)
                seleccionar_componentes(id_pedido_actual)

                break
        
            else:
                print('Opción inválida')




