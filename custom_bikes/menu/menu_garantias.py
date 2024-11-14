from custom_bikes.funciones.funciones_clientes import seleccionar_cliente
from custom_bikes.funciones.funciones_garantias import extension_garantia

def menu_garantias():
   
    while True:
        print('1. Extender garantía')
        print('2. Eliminar garantía')
        print('3. Buscar garantía')
        print('4. Mostrar garantías')
        print('5. Volver al menú principal')
    
        seleccion = int(input('Seleccione una opción: '))
    
        if seleccion == 1:
            print('Extender garantía')
            agregar_garantia()
    
        elif seleccion == 2:
            print('Eliminar garantía')
            eliminar_garantia()
    
        elif seleccion == 3:
            print('Buscar garantía')
            buscar_garantia()
    
        elif seleccion == 4:
            print('Mostrar garantías')
            mostrar_garantias()
        
        elif seleccion == 5:
            print('Volver al menú principal')
            break
        
        else:
            print('Opción inválida')

def extender_garantia():
    
    print('Extender Garantía')
   
    while True:
        print('Seleccione el tipo de cliente')
        cliente = seleccionar_cliente()
        rut_id = cliente[0]
        
        extension_garantia(rut_id)

def eliminar_garantia():

    print('Eliminar Garantía')
    print('1. Eliminar una garantía')

    seleccion_eliminar = int(input('Seleccione una opción: '))

    if seleccion_eliminar == 1:
        print('Eliminar una garantía')

        while True:
            print('Seleccione el cliente')
            print('1. Cliente nuevo')
            print('2. Cliente existente')

            seleccionar_cliente = int(input('Seleccione una opción: '))

            if seleccionar_cliente == 1:
                print('Cliente nuevo')
                insert_cliente()
                
                eliminar_garantia_nueva() #Funcion para eliminar la garantia del cliente nuevo

            elif seleccionar_cliente == 2:
                cliente = seleccionar_cliente()
                if cliente is None:
                    print('Cliente no encontrado')
                else:
                    print('Cliente existente')
                
                seleccionar_cliente()
                seleccionar_productos(cliente)
            
            else:
                print('Opción inválida')

def buscar_garantia():

    print('Buscar Garantía')
    print('1. Buscar una garantía')

    seleccionar_buscar = int(input('Seleccione una opción: '))

    if seleccionar_buscar == 1:
        print('Buscar una garantía')

        while True:
            print('Seleccione el cliente')
            print('1. Cliente nuevo')
            print('2. Cliente existente')

            seleccionar_cliente = int(input('Seleccione una opción: '))

            if seleccionar_cliente == 1:
                print('Cliente nuevo')
                insert_cliente() #Función para registrar al cliente si es necesario

                buscar_garantia_nueva() # Función para buscar la garantía de un cliente nuevo

            elif seleccionar_cliente == 2:
                cliente = seleccionar_cliente()
                if cliente is None:
                    print('Cliente no encontrado')
                else:
                    print('Cliente existente')
                
                seleccionar_cliente()
                seleccionar_productos(cliente) # Función para seleccionar y mostrar productos
                
            else:
                print('Opción invádila.')

