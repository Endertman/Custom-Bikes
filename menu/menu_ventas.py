def menu_ventas():
    seleccion = 0

    print('1. Agregar venta')
    print('2. Eliminar venta')
    print('3. Modificar venta')
    print('4. Buscar venta')
    print('5. Mostrar ventas')
    print('6. Volver al menú principal')

    seleccion = int(input('Seleccione una opción: '))

    if seleccion == 1:
        print('Agregar venta')
        agregar_venta()

    elif seleccion == 2:
        print('Eliminar venta')
        eliminar_venta()

    elif seleccion == 3:
        print('Modificar venta')
        modificar_venta()    

    elif seleccion == 4:
        print('Buscar venta')
        buscar_venta()

    elif seleccion == 5:
        print('Mostrar ventas')
        mostrar_ventas()

    elif seleccion == 6:
        menu_principal()

    else:
        print('Opción inválida')

def agregar_venta():

    print('1. Agregar venta (csv)')
    print('2. Generar venta')
    seleccion_ingreso_data = int(input('Seleccione una opción: '))

    if seleccion_ingreso_data == 1:
        print('Agregar venta (csv)')
        agregar_venta_csv()
    
    elif seleccion_ingreso_data == 2:
        print('Generar venta')
        agregar_venta_manual()

def agregar_venta_csv():
    import csv
    import os

    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    ruta_archivo = os.path.join(directorio_actual, 'ventas.csv')

    # Verificar si el archivo CSV existe
    if not os.path.exists(ruta_archivo):
        # Si no existe, crearlo con los encabezados
        with open(ruta_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['ID', 'Producto', 'Cantidad', 'Precio Unitario', 'Precio Total', 'Fecha'])

    # Solicitar datos de la venta
    id_venta = input('Ingrese el ID de la venta: ')
    producto = input('Ingrese el nombre del producto: ')
    cantidad = int(input('Ingrese la cantidad vendida: '))
    precio_unitario = float(input('Ingrese el precio unitario: '))
    precio_total = cantidad * precio_unitario
    fecha = input('Ingrese la fecha de la venta (YYYY-MM-DD): ')

    # Agregar la venta al archivo CSV
    with open(ruta_archivo, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([id_venta, producto, cantidad, precio_unitario, precio_total, fecha])

    print('Venta agregada exitosamente.')