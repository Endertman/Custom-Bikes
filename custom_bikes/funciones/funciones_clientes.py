import sqlite3
import os

def insert_cliente():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
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
        cursor.execute('''INSERT INTO clientes (rut_id, altura) 
                          VALUES (?, ?)''', (rut_id, altura))

        conn.commit()
        print(f'Cliente {nombre} {apellido} agregado exitosamente.')
    
    except sqlite3.Error as e:
        print("Error al insertar el cliente:", e)
    
    finally:
        conn.commit()
    
    return rut_id

def agregar_cliente_csv():
    import csv
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_csv_personas = os.path.join(ruta_base, '../../datos/personas_clientes_respaldo.csv')
    ruta_csv_cliente = os.path.join(ruta_base, '../../datos/cliente_respaldo.csv')

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    with open(ruta_csv_personas, 'r') as file:
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
                print(f'Persona {nombre} {apellido} agregado exitosamente.')

            except sqlite3.Error as e:
                print("Error al insertar a la persona:", e)

    with open(ruta_csv_cliente, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            rut_id = row[0]
            altura = row[1]

            try:
                cursor.execute('''INSERT INTO clientes (rut_id, altura)
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
    rut_id = cliente[0]

    conn.close()

    if cliente:
        print(f"Cliente encontrado: {cliente[1]} {cliente[2]}")  
        return rut_id
    else:
        print("Cliente no encontrado.")
        return 