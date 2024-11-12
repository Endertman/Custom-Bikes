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