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

def seleccionar_cliente():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    rut_id = input("Ingrese el RUT del cliente: ")
    cursor.execute("SELECT * FROM personas WHERE rut_id = ?", (rut_id,)) #agregar innerjoin
    cliente = cursor.fetchone()

    conn.close()

    if cliente:
        print(f"Cliente encontrado: {cliente[1]} {cliente[2]}")  
        return cliente
    else:
        print("Cliente no encontrado.")
        return None
    
