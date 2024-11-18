import sqlite3, os, csv

def insert_codigo():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    codigo = input('Ingrese el nombre del código: ')
    descuento = float(input('Ingrese el descuento (ej: 0.10): '))

    try:
        cursor.execute('''INSERT INTO codigos_descuentos (codigo, porcentaje) VALUES (?, ?)''', (codigo, descuento))

        conn.commit()
        print(f'Codigo {codigo} agregado exitosamente.')
    
    except sqlite3.Error as e:
        print("Error al insertar el codigo:", e)
    
    finally:
        conn.commit()
        conn.close()
    
def insert_codigos_csv():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_csv_codigos= os.path.join(ruta_base, '../../datos/codigos_descuentos_respaldo.csv')

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    with open(ruta_csv_codigos, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            codigo = row[0]
            descuento = row[1]

            try:
                cursor.execute('''INSERT INTO codigos_descuentos (codigo, porcentaje)
                                  VALUES (?, ?)''', (codigo, descuento))

                conn.commit()
                print(f'Codigo {codigo} agregado exitosamente.')

            except sqlite3.Error as e:
                print("Error al insertar el codigo:", e)

def seleccionar_codigo():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM codigos_descuentos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    codigo = input("Ingrese el código: ")

    cursor.execute("SELECT * FROM codigos_descuentos WHERE codigo = ?", (codigo,))
    codigo = cursor.fetchone()
    codigo = codigo[0]
    return codigo

def eliminar_codigo():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM codigos_descuentos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    codigo = input("Ingrese el código a eliminar: ")

    cursor.execute("DELETE FROM codigos_descuentos WHERE codigo = ?", (codigo, ))

    conn.commit()
    conn.close()

def ver_codigos():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM codigos_descuentos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
