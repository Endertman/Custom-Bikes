from custom_bikes.funciones.funciones_garantias import extender_garantia, eliminar_garantia, buscar_garantia, mostrar_garantias

def menu_garantias():
   
    while True:
        print('1. Extender garantía')
        print('2. Buscar garantía')
        print('3. Mostrar garantías')
        print('4. Volver al menú principal')
    
        seleccion = int(input('Seleccione una opción: '))
    
        if seleccion == 1:
            print('Extender garantía')
            extender_garantia()
    
        elif seleccion == 2:
            print('Buscar garantía')
            buscar_garantia()
    
        elif seleccion == 3:
            print('Mostrar garantías')
            mostrar_garantias()
        
        elif seleccion == 4:
            print('Volver al menú principal')
            break
        
        else:
            print('Opción inválida')


