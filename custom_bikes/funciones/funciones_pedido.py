import sqlite3
def id_pedido(rut_id):

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT 1 FROM clientes WHERE rut_id = ?''', (rut_id,))
    if not cursor.fetchone():
        print("Cliente no encontrado.")
        conn.close()
        return None

    cursor.execute('''SELECT COUNT(*) FROM pedido WHERE cliente LIKE ?''', (f'{rut_id}%',))
    numero_pedidos = cursor.fetchone()[0] + 1
    
    id_pedido = f"{rut_id}_{numero_pedidos}"

    conn.close()
    return id_pedido
