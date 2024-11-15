import sqlite3

def insert_cliente():
    conn = sqlite3.connect('custom_bikes\custom_bikes.db')
    cursor = conn.cursor()

    print('Ingrese los datos del cliente:')
    
    rut_id = input('RUT: ')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    telefono = int(input('Teléfono: '))
    correo = input('Correo: ')
    direccion = input('Dirección: ')
    altura = int(input('Altura: '))

    try:
        cursor.execute('''INSERT INTO personas (rut_id, nombre, apellido, telefono, correo, direccion) 
                          VALUES (?, ?, ?, ?, ?, ?)''', (rut_id, nombre, apellido, telefono, correo, direccion))
        cursor.execute('''INSERT INTO cliente (rut_id, altura) 
                          VALUES (?, ?)''', (rut_id, altura))

        conn.commit()
        print(f'Cliente {nombre} {apellido} agregado exitosamente.')

        return rut_id
    
    except sqlite3.Error as e:
        print("Error al insertar el cliente:", e)
    
    finally:
        conn.close()

def agregar_cliente_csv():
    import csv

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    with open('custom_bikes\datos\personas_respaldo.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            rut_id = row[0]
            nombre = row[1]
            apellido = row[2]
            telefono = row[3]
            correo = row[4]
            direccion = row[5]

            try:
                cursor.execute('''INSERT INTO personas (rut_id, nombre, apellido, telefono, correo, direccion)
                                  VALUES (?, ?, ?, ?, ?, ?)''', (rut_id, nombre, apellido, telefono, correo, direccion))

                conn.commit()
                print(f'Cliente {nombre} {apellido} agregado exitosamente.')

            except sqlite3.Error as e:
                print("Error al insertar el cliente:", e)

    with open('custom_bikes\datos\cliente_respaldo.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            rut_id = row[0]
            altura = row[1]

            try:
                cursor.execute('''INSERT INTO cliente (rut_id, altura)
                                  VALUES (?, ?)''', (rut_id, altura))

                conn.commit()
                print(f'Cliente {rut_id} agregado exitosamente.')

            except sqlite3.Error as e:
                print("Error al insertar el cliente:", e)
    
        conn.close()

def seleccionar_cliente():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT personas.rut_id, personas.nombre, personas.apellido FROM clientes INNER JOIN personas ON clientes.rut_id = personas.rut_id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    rut_id = input("Ingrese el RUT del cliente: ")

    cursor.execute("SELECT * FROM personas WHERE rut_id = ?", (rut_id,))
    cliente = cursor.fetchone()

    conn.close()

    if cliente:
        print(f"Cliente encontrado: {cliente[1]} {cliente[2]}")  
        return cliente
    else:
        print("Cliente no encontrado.")
        return None  