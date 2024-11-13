from custom_bikes.funciones.funciones_clientes import insert_cliente, seleccionar_cliente 
from custom_bikes.funciones.funciones_ventas import seleccionar_componentes

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
                insert_cliente()
                seleccionar_componentes()
                

            elif seleccion_cliente == 2:
                cliente = seleccionar_cliente()
                if cliente is None:
                    print('Cliente no encontrado')
                    continue
                else:
                    print('Cliente existente')
                
                seleccionar_cliente()
                seleccionar_productos(cliente)
            
            else:
                print('Opción inválida')




