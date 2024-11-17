from custom_bikes.menu.menu_ventas import menu_ventas
from custom_bikes.menu.menu_garantias import menu_garantias
from custom_bikes.menu.menu_stock import menu_stock
from custom_bikes.menu.menu_empleados import menu_empleados
from custom_bikes.menu.menu_codigos_descuento import menu_codigos_descuento
from custom_bikes.menu.menu_analisis import menu_analisis

def menu_principal():
    while True:
        print('Custom Bikes -- Menú Principal')
        print('1. Ventas')
        print('2. Garantías')
        print('3. Empleados')
        print('4. Stock')
        print('5. Códigos de descuento')
        print('6. Análisis')
        print('7. Salir')

        seleccion = int(input('Seleccione una opción: '))
    
        if seleccion == 1:
            menu_ventas()

        elif seleccion == 2:
            menu_garantias()

        elif seleccion == 3:
            menu_empleados()

        elif seleccion == 4:
            menu_stock()

        elif seleccion == 5:
            menu_codigos_descuento()

        elif seleccion == 6:
            menu_analisis()

        elif seleccion == 7:
            print('Saliendo...')
            break
        
        else:
            print('Opción inválida')

