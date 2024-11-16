import sqlite3

def agregar_empleados_csv():
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
                print(f'Persona {nombre} {apellido} agregado exitosamente.')

            except sqlite3.Error as e:
                print("Error al insertar la persona", e)

    with open('custom_bikes/datos/tecnico_respaldo.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            rut_id = row[0]
            especialidad = row[1]

            try:
                cursor.execute('''INSERT INTO rte (rut_id, especialidad)
                                  VALUES (?, ?)''', (rut_id, especialidad))

                conn.commit()
                print(f'Cliente {rut_id} agregado exitosamente.')

            except sqlite3.Error as e:
                print("Error al insertar el cliente:", e)

    conn.close()