from custom_bikes.menu.menu_ventas import menu_ventas
from custom_bikes.menu.menu_garantias import menu_garantias
from custom_bikes.menu.menu_stock import menu_stock
from custom_bikes.menu.menu_empleados import menu_empleados

def menu_principal():
    init = True
    while init == True:
        print('Custom Bikes')
        print('1. Ventas')
        print('2. Garantías')
        print('3. Empleados')
        print('4. Stock')

        seleccion = int(input('Seleccione una opción: '))
    
        if seleccion == 1:
            menu_ventas()
            init = False

        elif seleccion == 2:
            menu_garantias()
            init = False

        elif seleccion == 3:
            menu_empleados()
            init = False

        elif seleccion == 4:
            menu_stock()
            init = False

        else:
            print('Opción inválida')

