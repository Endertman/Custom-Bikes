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

    cursor.execute('''INSERT INTO personas (rut_id, nombre, apellido, telefono, correo, direccion) VALUES (?, ?, ?, ?, ?, ?)''', (rut_id, nombre, apellido, telefono, correo, direccion))
    cursor.execute('''INSERT INTO clientes (rut_id, altura) VALUES (?, ?)''', (rut_id, altura))

    conn.commit()
    conn.close()

    print(f'Cliente {nombre} {apellido} agregado exitosamente.')