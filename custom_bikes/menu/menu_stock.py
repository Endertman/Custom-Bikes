from custom_bikes.funciones.funciones_stock import agregar_producto, eliminar_producto, modificar_producto, buscar_producto, mostrar_productos

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

def agregar_productos():

    print('Agregar Producto')
    
    while True:
       print("Ingrese los datos del nuevo producto: ")
       try:
            agregar_producto()

       except ValueError:
           print("Error: Verifique que el stock sea un número entero y el precio un valor númerico válido.")

def eliminar_producto():
    print('Eliminar Prodcuto')
    
    while True:
        # Solicitar al usuario el SKU del producto a eliminar
        sku = input("Ingrese el SKU del producto a eliminar: ").strip()
        
        #  Verificar si el producto existe en la base de datos
        producto_encontrado = buscar_producto(sku)
        
        if producto_encontrado:
            #Mostrar detalles del producto o eliminar
            print(f"Producto encontrado: SKU: {producto_encontrado[sku]}, Nombre: {producto_encontrado['nombre']}, Stock: {producto_encontrado['stock']}, Precio: {producto_encontrado['precio']}")
            
            #confirmar la eliminacion
            confirmacion = input(f"¿Está seguro de que desea eliminar el producto(SKU: {sku}, Nombre: {producto_encontrado['nombre']})? (s/n): ").lower()
            if confirmacion == 's':
                #Eliminar el producto de la base de datos
                eliminar_producto(sku) # Funcion que elimina el producto de la base de datos
                print("Producto eliminado exitosamente.\n")
            else:
                print("Operación cancelada. No se eliminó el producto.\n")
                
        else:
            print("Error: No se encontró un producto con ese SKU.\n")
            
        
        continuar = input("¿Desea eliminar otro producto? (s/n): ")
        if continuar != 's':
            print("Saliendo de la función eliminar producto.")
            break
            
def modificar_producto():
    print('Modificar Producto')
    
    while True:
        # Solicitar al usuario el SKU del producto a modificar
        sku = input("Ingrese el SKU del producto a modificar: ").strip()
        
        # Verificar si el producto existe en la base de datos
        producto_encontrado = buscar_producto(sku)
        
        if producto_encontrado:
            # Mostrar detalles del producto
            print(f"Producto encontrado: SKU: {sku}, Nombre: {producto_encontrado['nombre']}, Stock: {producto_encontrado['stock']}, Precio: {producto_encontrado['precio']}")
            
            # Solicitar al usuario qué desea modificar
            print("¿Qué desea modificar?")
            print("1. Nombre")
            print("2. Stock")
            print("3. Precio")
            opcion = input("Ingrese el número de la opción deseada: ").strip()
            
            if opcion == '1':
                nuevo_nombre = input("Ingresa el nuevo nombre del producto: ").strip()
                producto_encontrado['nombre'] = nuevo_nombre
                print("\nEl nombre del producto ha sido actualizado.")
                
            elif opcion == '2':
                try:
                    nuevo_stock = int(input("Ingrese el nuevo stock del producto: ").strip())
                    producto_encontrado['stock'] = nuevo_stock
                    print("El stock del producto ha sido actualizado.")
                except ValueError:
                    print("Error: El stock debe ser un número entero.")
            
            elif opcion == '3':
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio del producto: ").strip())
                    producto_encontrado['precio'] = nuevo_precio
                    print("El precio del producto ha sido actualizado.")
                except ValueError:
                    print("Error: El precio debe ser un número váludo.")
            
            else:
                print("\nError: Opción no válida.\n")
            
            # Confirmar cambios
            guardar_cambios = input("\n¿Desea guardar los cambios realizados? (s/n): ").lower()
            if guardar_cambios == 's':
                modificar_producto(sku, producto_encontrado)
                print("Cambios guardados exitosamente.")
            else:
                print("Operación cancelada. No se guardaron los cambios.")
            
            # Preguntar si desea modificar otro producto
            continuar = input("¿Desea modificar otro producto? (s/n): ")
            if continuar != 's':
                print("Saliendo de la función modificar producto.")
                break

def buscar_producto():
    print('Buscar Producto')

    while True:
        #Solicitar al usuario el SKU del producto a buscar
        sku = input("Ingrese el SKU del producto que desea buscar: ").strip()

        #Verificar si el producto existe en la base de datos
        producto_encontrado = buscar_producto(sku)

        if producto_encontrado:
            # Mostrar los detalles del producto encontrado
            print("Producto Encontrado:")
            print(f"SKU: {sku}")
            print(f"Nombre: {producto_encontrado['nombre']}")
            print(f"Stock: {producto_encontrado['stock']}")
            print(f"Precio: {producto_encontrado['precion']}")
        
        else:
            # Mensaje en caso de no encontrar nada
            print("Error: No se encontró un producto con ese SKU.")
        
        # Preguntar para encontrar otro producto
        continuar = input("¿Desea buscar otro producto? (s/n): ")
        if continuar != 's':
            print("Saliendo de la función buscar producto.")
            break

def mostrar_productos():
    print('Mostrar Productos')

    while True:
        #Obtener la lista de productos desde la base de datos
        productos = mostrar_productos()

        if productos:
            # Detalles de los productos
             print("Productos disponibles:")
             print(f"{'SKU':<15}{'Nombre':<20}{'Stock':<10}{'Precio':<10}")
             print("-" * 55)
             for producto in productos:
                print(f"{producto['sku']:<15}{producto['nombre']:<20}{producto['stock']:<10}{producto['precio']:<10}")
                print("-" * 55)  
        else:
            # en caso de que no haya productos
            print("No hay productos registrados en la base de datos.")

        # Preguntar si desea volver a mostrar los productos
        continuar = input("¿Desea volver a mostrar la lista de productos? (s/n): ").lower()
        if continuar != 's':
            print("Saliendo de la función mostrar productos.")
            break   

            