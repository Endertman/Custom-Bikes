def menu_empleados():
    seleccion = 0

    print('1. Agregar empleado')
    print('2. Eliminar empleado')
    print('3. Modificar empleado')
    print('4. Buscar empleado')
    print('5. Mostrar empleados')
    print('6. Volver al menú principal')

    seleccion = int(input('Seleccione una opción: '))

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

    elif seleccion == 6:
        print('Volver al menú principal')
        return menu_principal()

    else:
        print('Opción inválida')

def agregar_empleado():
    nombre = input('Ingrese el nombre del empleado: ')

menu_empleados()