from custom_bikes.funciones.funciones_empleados import agregar_empleados_csv, generar_empleado, eliminar_empleado, modificar_empleado, buscar_empleado

def menu_empleados():
   
   while True:
        print('1. Agregar empleado')
        print('2. Eliminar empleado')
        print('3. Modificar empleado')
        print('4. Buscar empleado')
        print('5. Mostrar empleados')
        print('6. Volver al menú principal')

        seleccion = int(input('Seleccione una opción: '))

        if seleccion == 1:
            print('Agregar empleado')
            agregar_empleados()

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
            break

        else:
            print('Opción inválida')

def agregar_empleados():
    print('1. Agregar empleados (csv)')
    print('2. Generar empleado')
    seleccion = int(input('Seleccione una opción: '))

    if seleccion == 1:
        print('Agregar empleados (csv)')
        agregar_empleados_csv()
        print('Empleados agregados exitosamente')

    elif seleccion == 2:
        print('Generar empleado')
        generar_empleado()