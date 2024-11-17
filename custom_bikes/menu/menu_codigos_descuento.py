from custom_bikes.funciones.funciones_codigos_descuento import insert_codigo, insert_codigos_csv, eliminar_codigo, ver_codigos

def menu_codigos_descuento():
    while True:
        print('1. Insertar código')
        print('2. Insertar códigos desde CSV')
        print('3. Eliminar código')
        print('4. Ver códigos')
        print('5. Volver al menú principal')

        seleccion = int(input('Seleccione una opción: '))

        if seleccion == 1:
            print('Insertar código')
            insert_codigo()

        elif seleccion == 2:
            print('Insertar códigos desde CSV')
            insert_codigos_csv()

        elif seleccion == 3:
            print('Eliminar código')
            eliminar_codigo()

        elif seleccion == 4:
            print('Ver códigos')
            ver_codigos()

        elif seleccion == 5:
            print('Volver al menú principal')
            break

        else:
            print('Opción inválida')