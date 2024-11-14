import sqlite3
def extension_garantia(rut_id):
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clientes WHERE id_cliente = ?', (rut_id[0],))
    

