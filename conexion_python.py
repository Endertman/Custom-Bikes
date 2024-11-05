import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('custom_bikes.db')
cursor = conexion.cursor()

cursor.execute('SELECT * FROM cliente')
clientes = cursor.fetchall()  # Obtiene todos los registros

for cliente in clientes:
    print(cliente)

cursor.execute('SELECT * FROM almacen')
almacen = cursor.fetchall()  # Obtiene todos los registros

for componente in almacen:
    print(componente)
