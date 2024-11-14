def menu_garantias():
    seleccion = 0

    print('1. Agregar garantía')
    print('2. Eliminar garantía')
    print('3. Modificar garantía')
    print('4. Buscar garantía')
    print('5. Mostrar garantías')
    print('6. Volver al menú principal')

    seleccion = int(input('Seleccione una opción: '))

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