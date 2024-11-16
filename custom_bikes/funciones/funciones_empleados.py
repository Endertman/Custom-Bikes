import sqlite3
import os

def agregar_empleados_csv():
    import csv
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_csv_personas = os.path.join(ruta_base, '../../datos/personas_respaldo.csv')
    ruta_csv_tecnicos = os.path.join(ruta_base, '../../datos/tecnico_respaldo.csv')

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
                print("Error al insertar la persona", e)

    with open(ruta_csv_tecnicos, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            rut_id = row[0]
            especialidad = row[1]

            try:
                cursor.execute('''INSERT INTO tecnicos (rut_id, especialidad)
                                  VALUES (?, ?)''', (rut_id, especialidad))

                conn.commit()
                print(f'Empleado {rut_id} agregado exitosamente.')

            except sqlite3.Error as e:
                print("Error al insertar al empleado:", e)

    conn.close()

def generar_empleado():
    import sqlite3

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    rut_id = input('Ingrese el rut del empleado: ')
    nombre = input('Ingrese el nombre del empleado: ')
    apellido = input('Ingrese el apellido del empleado: ')
    telefono = input('Ingrese el telefono del empleado: ')
    correo = input('Ingrese el correo del empleado: ')
    direccion = input('Ingrese la direccion del empleado: ')
    especialidad = input('Ingrese la especialidad del empleado: ')

    try:
        cursor.execute('''INSERT INTO personas (rut_id, nombre, apellido, telefono, correo, direccion)
                          VALUES (?, ?, ?, ?, ?, ?)''', (rut_id, nombre, apellido, telefono, correo, direccion))

        cursor.execute('''INSERT INTO tecnicos (rut_id, especialidad)
                          VALUES (?, ?)''', (rut_id, especialidad))

        conn.commit()
        print(f'Empleado {nombre} {apellido} agregado exitosamente.')

    except sqlite3.Error as e:
        print("Error al insertar el empleado:", e)

    conn.close()

def eliminar_empleado():
    import sqlite3

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    rut_id = input('Ingrese el rut del empleado a eliminar: ')

    try:
        cursor.execute('''DELETE FROM personas WHERE rut_id = ?''', (rut_id,))
        cursor.execute('''DELETE FROM tecnicos WHERE rut_id = ?''', (rut_id,))

        conn.commit()
        print(f'Empleado {rut_id} eliminado exitosamente.')

    except sqlite3.Error as e:
        print("Error al eliminar el empleado:", e)

    conn.close()

def modificar_empleado():
    import sqlite3

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    rut_id = input('Ingrese el rut del empleado a modificar: ')
    nombre = input('Ingrese el nuevo nombre del empleado: ')
    apellido = input('Ingrese el nuevo apellido del empleado: ')
    telefono = input('Ingrese el nuevo telefono del empleado: ')
    correo = input('Ingrese el nuevo correo del empleado: ')
    direccion = input('Ingrese la nueva direccion del empleado: ')
    especialidad = input('Ingrese la nueva especialidad del empleado: ')

    try:
        cursor.execute('''UPDATE personas SET nombre = ?, apellido = ?, telefono = ?, correo = ?, direccion = ?
                          WHERE rut_id = ?''', (nombre, apellido, telefono, correo, direccion, rut_id))

        cursor.execute('''UPDATE tecnicos SET especialidad = ?
                          WHERE rut_id = ?''', (especialidad, rut_id))

        conn.commit()
        print(f'Empleado {rut_id} modificado exitosamente.')

    except sqlite3.Error as e:
        print("Error al modificar el empleado:", e)

    conn.close()

def buscar_empleado():
    import sqlite3

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    rut_id = input('Ingrese el rut del empleado a buscar: ')

    try:
        cursor.execute('''SELECT * FROM personas WHERE rut_id = ?''', (rut_id, ))
        empleado = cursor.fetchone()

        cursor.execute('''SELECT * FROM tecnicos WHERE rut_id = ?''', (rut_id, ))
        tecnicos = cursor.fetchone()

        if empleado:
            print(f'Empleado encontrado: {empleado}')
            print(f'Empleado encontrado: {tecnicos}')
        else:
            print(f'Empleado {rut_id} no encontrado.')

    except sqlite3.Error as e:
        print("Error al buscar el empleado:", e)

    conn.close()

def mostrar_tecnicos():
    import sqlite3

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT p.rut_id, p.nombre, p.apellido, p.telefono, p.correo, p.direccion, t.especialidad
            FROM personas p
            INNER JOIN tecnicos t ON p.rut_id = t.rut_id
        ''')
        tecnicos = cursor.fetchall()

        if tecnicos:
            print('--- Lista de Técnicos ---')
            for tecnico in tecnicos:
                rut_id = tecnico[0]
                nombre = f"{tecnico[1]} {tecnico[2]}"
                telefono = tecnico[3]
                correo = tecnico[4]
                direccion = tecnico[5] 
                especialidad = tecnico[6] 

                print(f"RUT: {rut_id}, Nombre: {nombre}, Teléfono: {telefono}, Correo: {correo}, Dirección: {direccion}")
                print(f"Especialidad: {especialidad}")
                print('---------------------------------')

        else:
            print('No hay técnicos registrados.')

    except sqlite3.Error as e:
        print("Error al mostrar los técnicos:", e)

    finally:
        conn.close()