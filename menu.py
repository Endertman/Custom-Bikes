def menu_principal():
    seleccion = 0

    print('1. Ventas')
    print('2. Garantías')
    print('3. Empleados')
    print('4. Stock')

    seleccion = input('Seleccione una opción: ')
    
    if seleccion == 1:
        menu_ventas()

    elif seleccion == 2:
        menu_garantias()

    elif seleccion == 3:
        menu_empleados()

    elif seleccion == 4:
        menu_stock()
        
    else:
        print('Opción inválida')

def menu_ventas():
    seleccion = 0

    print('1. Agregar venta')
    print('2. Eliminar venta')
    print('3. Modificar venta')
    print('4. Buscar venta')
    print('5. Mostrar ventas')
    print('6. Volver al menú principal')

    seleccion = input('Seleccione una opción: ')

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

def menu_garantias():
    seleccion = 0

    print('1. Agregar garantía')
    print('2. Eliminar garantía')
    print('3. Modificar garantía')
    print('4. Buscar garantía')
    print('5. Mostrar garantías')
    print('6. Volver al menú principal')

    seleccion = input('Seleccione una opción: ')

    if seleccion == 1:
        print('Agregar garantía')
        agregar_garantia()

    elif seleccion == 2:
        print('Eliminar garantía')
        eliminar_garantia()

    elif seleccion == 3:
        print('Modificar garantía')
        modificar_garantia()

    elif seleccion == 4:
        print('Buscar garantía')
        buscar_garantia()

    elif seleccion == 5:
        print('Mostrar garantías')
        mostrar_garantias()
    
    elif seleccion == 6:
        menu_principal()
    
    else:
        print('Opción inválida')

def menu_empleados():
    seleccion = 0

    print('1. Agregar empleado')
    print('2. Eliminar empleado')
    print('3. Modificar empleado')
    print('4. Buscar empleado')
    print('5. Mostrar empleados')
    print('6. Volver al menú principal')

    seleccion = input('Seleccione una opción: ')

    if seleccion == 1:
        print('Agregar empleado')
        agregar_empleado()
    
    elif seleccion == 2:
        print('Eliminar empleado')
        eliminar_empleado()

    elif seleccion == 3:
        print('Modificar empleado')
        modificar_empleado()
    
    elif seleccion == 4:
        print('Buscar empleado')
        buscar_empleado()
    
    elif seleccion == 5:
        print('Mostrar empleados')
        mostrar_empleados()

    

def menu_stock():
    seleccion = 0

    print('1. Agregar producto')
    print('2. Eliminar producto')
    print('3. Modificar producto')
    print('4. Buscar producto')
    print('5. Mostrar stock')
    print('6. Volver al menú principal')

    seleccion = input('Seleccione una opción: ')
