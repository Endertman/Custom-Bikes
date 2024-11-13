import sqlite3

def agregar_producto():
    conn = sqlite3.connect('custom_bikes\custom_bikes.db')
    cursor = conn.cursor()

    print('Ingrese los datos del producto: ')
    sku_producto = input('Codigo del producto (sku): ')
    nombre_producto = input('Ingrese el nombre del producto: ')
    print('Seleccione a que categoria pertenece: ')
    print(f'  1. Ruta \n  2. MTB \n  3. Urbano')
    eleccion = int(input('Ingrese un numero: '))

    while eleccion < 1 or eleccion > 3:
        print('Opcion invalida. Intente nuevamente.')
        eleccion = int(input('Ingrese un numero: '))

    if eleccion == 1:
        categoria_producto = ('Ruta')
        print('El tipo de producto se ha selecciona como Ruta.')
    
    elif eleccion == 2:
        categoria_producto = ('MTB')
        print('El tipo de producto se ha selecciona como MTB.')

    elif eleccion == 3:
        categoria_producto = ('Urbano')
        print('El tipo de producto se ha selecciona como MTB.')

    print('Seleccione a que tipo pertenece: ')
    print(f'  1. Marco \n  2. Transmisión \n  3. Frenos \n  4. Ruedas \n  5. Neumaticos \n  6. Tija \n  7. Manillar \n  8. Pedales \n  9. Sillin  ')
    eleccion = int(input('Ingrese un numero: '))
    
    while eleccion < 1 or eleccion > 9:
         print('Opcion invalida. Intente nuevamente.')
         eleccion = int(input('Ingrese un numero: '))

    if eleccion == 1:
        tipo_producto = ('Marco')
        print('El tipo de producto se ha selecciona como Marco.')

    elif eleccion == 2:
        tipo_producto = ('Transmision')
        print('El tipo de producto se ha selecciona como Transmision.')

    elif eleccion == 3:
        tipo_producto = ('Frenos')
        print('El tipo de producto se ha selecciona como Frenos.')

    elif eleccion == 4:
        tipo_producto = ('Ruedas')
        print('El tipo de producto se ha selecciona como Ruedas.')

    elif eleccion == 5:
        tipo_producto = ('Neumaticos')
        print('El tipo de producto se ha selecciona como Neumaticos.')

    elif eleccion == 6:
        tipo_producto = ('Tija')
        print('El tipo de producto se ha selecciona como Tija.')

    elif eleccion == 7:
        tipo_producto = ('Manillar')
        print('El tipo de producto se ha selecciona como Manillar.')

    elif eleccion == 8:
        tipo_producto = ('Pedales')
        print('El tipo de producto se ha selecciona como Pedales.')

    elif eleccion == 9:
        tipo_producto = ('Sillin')
        print('El tipo de producto se ha selecciona como Sillin.')

    descuento_individual = int(input('Ingrese el descuento individual (Si no aplica coloque 0): '))
    stock = int(input('Ingrese el stock (si no hay stock coloque 0): '))
    precio = int(input('Ingrese el precio: '))
    print('Producto agregado exitosamente.')
    
    # Si van a agregar el precio tienen que modificar la tabla almacen ya que no existe esa columna en el momento que escribo este mensaje, solo modifican el codigo de aqui abajo
    cursor.execute('''INSERT INTO almacen (sku, nombre, categoria, tipo, descuento_individual, stock) VALUES (?, ?, ?, ?, ?, ?)''', (sku_producto, nombre_producto, categoria_producto, tipo_producto, descuento_individual, stock))
    conn.commit()
    conn.close()
    

def eliminar_producto():
    conn = sqlite3.connect('custom_bikes\custom_bikes.db')
    cursor = conn.cursor()

    sku_producto = input('Ingrese el codigo del producto que desea eliminar: ')
    cursor.execute('''DELETE FROM almacen WHERE sku = ?''', (sku_producto,))
    conn.commit()
    conn.close()
    print('Producto eliminado exitosamente.')

#def modificar_producto():




#def buscar_producto():


def mostrar_productos():
    conn = sqlite3.connect('custom_bikes\custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM almacen')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
