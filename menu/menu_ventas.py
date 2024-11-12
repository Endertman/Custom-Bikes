def menu_ventas():
    seleccion = 0

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
        menu_principal()

    else:
        print('Opción inválida')