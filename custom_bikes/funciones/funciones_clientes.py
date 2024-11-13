import sqlite3

def insert_cliente():
    conn = sqlite3.connect('custom_bikes\custom_bikes.db')
    cursor = conn.cursor()

    print('Ingrese los datos del cliente:')
    
    rut_id = input('RUT: ')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    telefono = input('Teléfono: ')
    correo = input('Correo: ')
    direccion = input('Dirección: ')

    cursor.execute('''INSERT INTO cliente (rut_id, nombre, apellido, telefono, correo, direccion) VALUES (?, ?, ?, ?, ?, ?)''', (rut_id, nombre, apellido, telefono, correo, direccion))

    conn.commit()
    conn.close()

    print(f'Cliente {nombre} {apellido} agregado exitosamente.')