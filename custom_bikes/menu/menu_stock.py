from custom_bikes.funciones.funciones_stock import agregar_producto
from custom_bikes.funciones.funciones_stock import eliminar_producto
from custom_bikes.funciones.funciones_stock import modificar_producto
from custom_bikes.funciones.funciones_stock import buscar_producto
from custom_bikes.funciones.funciones_stock import mostrar_productos
from custom_bikes import menu_principal


def menu_stock():
    while True:
        print('1. Agregar producto')
        print('2. Eliminar producto')
        print('3. Modificar producto')
        print('4. Buscar producto')
        print('5. Mostrar stock')
        print('6. Volver al menú principal')

        seleccion = int(input('Seleccione una opción: '))
        
        if seleccion == 1:
            print('Agregar producto')
            agregar_producto() 
        
        elif seleccion == 2:
            print('Eliminar producto')
            eliminar_producto()
        
        elif seleccion == 3:
            print('Modificar producto')
            modificar_producto()
            
        elif seleccion == 4:
            print('Buscar producto')
            buscar_producto()
        
        elif seleccion == 5:
            print('Mostrar stock')
            mostrar_productos()
        
        elif seleccion == 6:
            print('Volver al menú principal')
            break
        
        else:
            print('Opción inválida') 

def agregar_producto():

    print('Agregar Producto')
    
    while True:
       print("\nIngrese los datos del nuevo producto: ")
       try:
           sku = input('SKU del producto: ')
           nombre = input('Nombre del producto: ')
           stock = int(input('Cantidad en stock: '))
           precio = float(input('Precio del producot: '))
           
           #confirmar la accion
           confirmacion = input(f"\n¿Desea agregar este producto (SKU: {sku}, Nombre: {nombre}, Stock: {stock}, Precio: {precio})? (s/n)").lower
           if confirmacion == 's':
               agregar_producto(sku, nombre, stock, precio)
               print("\nProducto agregago exitosamente.\n")
           else:
               print("\Operación cancelada. No se agregó el producto.\n")
       except ValueError:
           print("\nError: Verifique que el stock sea un número entero y el precio un valor númerico válido.\n")
           
           #Preguntar si desea agregar otro producto
           continuar = input("¿Desea agregar otro producto? (s/n): ").lower
           if continuar != 's':
               print("\nSaliendo de la funcion de agregar producto.\n")
               break

        
def eliminar_producto():
    print('Eliminar Prodcuto')
    
    while True:
        # Solicitar al usuario el SKU del producto a eliminar
        sku = input("\nIngrese el SKU del producto a eliminar: ").strip()
        
        #  Verificar si el producto existe en la base de datos
        producto_encontrado = buscar_producto(sku)
        
        if producto_encontrado:
            #Mostrar detalles del producto o eliminar
            print(f"\nProducto encontrado: SKU: {producto_encontrado[sku]}, Nombre: {producto_encontrado['nombre']}, Stock: {producto_encontrado['stock']}, Precio: {producto_encontrado['precio']}")
            
            #confirmar la eliminacion
            confirmacion = input(f"\n¿Está seguro de que desea eliminar el producto(SKU: {sku}, Nombre: {producto_encontrado['nombre']})? (s/n): ").lower()
            if confirmacion == 's':
                #Eliminar el producto de la base de datos
                eliminar_producto(sku) # Funcion que elimina el producto de la base de datos
                print("\nProducto eliminado exitosamente.\n")
            else:
                print("\nOperación cancelada. No se eliminó el producto.\n")
                
        else:
            print("\nError: No se encontró un producto con ese SKU.\n")
            
        
        continuar = input("¿Desea eliminar otro producto? (s/n): ")
        if continuar != 's':
            print("\nSaliendo de la función eliminar producto.\n")
            break
            
def modificar_producto():
    print('Modificar Producto')
    
    while True:
        # Solicitar al usuario el SKU del producto a modificar
        sku = input("\nIngrese el SKU del producto a modificar: ").strip()
        
        # Verificar si el producto existe en la base de datos
        producto_encontrado = buscar_producto(sku)
        
        if producto_encontrado:
            # Mostrar detalles del producto
            print(f"\nProducto encontrado: SKU: {sku}, Nombre: {producto_encontrado['nombre']}, Stock: {producto_encontrado['stock']}, Precio: {producto_encontrado['precio']}")
            
            # Solicitar al usuario qué desea modificar
            print("\n¿Qué desea modificar?")
            print("1. Nombre")
            print("2. Stock")
            print("3. Precio")
            opcion = input("Ingrese el número de la opción deseada: ").strip()
            
            if opcion == '1':
                nuevo_nombre = input("Ingresa el nuevo nombre del producto: ").strip()
                producto_encontrado['nombre'] = nuevo_nombre
                print("\nEl nombre del producto ha sido actualizado.\n")
                
            elif opcion == '2':
                try:
                    nuevo_stock = int(input("Ingrese el nuevo stock del producto: ").strip())
                    producto_encontrado['stock'] = nuevo_stock
                    print("\nEl stock del producto ha sido actualizado.\n")
                except ValueError:
                    print("\nError: El stock debe ser un número entero.\n")
            
            elif opcion == '3':
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio del producto: ").strip())
                    producto_encontrado['precio'] = nuevo_precio
                    print("\nEl precio del producto ha sido actualizado.\n")
                except ValueError:
                    print("\nError: El precio debe ser un número váludo.\n")
            
            else:
                print("\nError: Opción no válida.\n")
            
            # Confirmar cambios
            guardar_cambios = input("\n¿Desea guardar los cambios realizados? (s/n): ").lower()
            if guardar_cambios == 's':
                modificar_producto(sku, producto_encontrado)
                print("\nCambios guardados exitosamente.\n")
            else:
                print("\nOperación cancelada. No se guardaron los cambios.\n")
            
            # Preguntar si desea modificar otro producto
            continuar = input("¿Desea modificar otro producto? (s/n): ")
            if continuar != 's':
                print("\nSaliendo de la función modificar producto.\n")
                break

def buscar_producto():
    print('Buscar Producto')

    while True:
        #Solicitar al usuario el SKU del producto a buscar
        sku = input("\nIngrese el SKU del producto que desea buscar: ").strip()

        #Verificar si el producto existe en la base de datos
        producto_encontrado = buscar_producto(sku)

        if producto_encontrado:
            # Mostrar los detalles del producto encontrado
            print("\nProducto Encontrado:")
            print(f"SKU: {sku}")
            print(f"Nombre: {producto_encontrado['nombre']}")
            print(f"Stock: {producto_encontrado['stock']}")
            print(f"Precio: {producto_encontrado['precion']}\n")
        
        else:
            # Mensaje en caso de no encontrar nada
            print("\nError: No se encontró un producto con ese SKU.\n")
        
        # Preguntar para encontrar otro producto
        continuar = input("¿Desea buscar otro producto? (s/n): ")
        if continuar != 's':
            print("\nSaliendo de la función buscar producto.\n")
            break

def mostrar_productos():
    print('Mostrar Productos')

    while True:
        #Obtener la lista de productos desde la base de datos
        productos = mostrar_productos()

        if productos:
            # Detalles de los productos
             print("\nProductos disponibles:")
             print(f"{'SKU':<15}{'Nombre':<20}{'Stock':<10}{'Precio':<10}")
             print("-" * 55)
             for producto in productos:
                print(f"{producto['sku']:<15}{producto['nombre']:<20}{producto['stock']:<10}{producto['precio']:<10}")
                print("-" * 55)  
        else:
            # en caso de que no haya productos
            print("\nNo hay productos registrados en la base de datos.\n")

        # Preguntar si desea volver a mostrar los productos
        continuar = input("¿Desea volver a mostrar la lista de productos? (s/n): ").lower()
        if continuar != 's':
            print("\nSaliendo de la función mostrar productos.\n")
            break   

def volver_menu_principal():
    print('Volver al Menú Principal')

    while True:
        print("\nEstá a punto de regresar al menú principal.")

        confirmacion = input("¿Desea continuar? (s/n): ").lower()

        if confirmacion == 's':
            print("\nRegresando al menú principal...\n")
            menu_principal()
            break
        
        elif confirmacion == 'n':
            print("\nOperación cancelada. Permanecerá en la función actual.\n")
            break
        
        else: 
            print("\nError: Por favor, ingrese 's' para continuar o 'n' para cancelar.\n")
            