from menu_ventas import menu_ventas
from menu_garantias import menu_garantias
from menu_stock import menu_stock
from menu_empleados import menu_empleados

def menu_principal():
    seleccion = 0

    print('1. Ventas')
    print('2. Garantías')
    print('3. Empleados')
    print('4. Stock')

    seleccion = int(input('Seleccione una opción: '))
    
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

menu_principal()