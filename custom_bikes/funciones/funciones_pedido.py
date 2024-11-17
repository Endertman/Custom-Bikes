import sqlite3

def id_pedido(rut_id):

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT 1 FROM clientes WHERE rut_id = ?''', (rut_id,))
    if not cursor.fetchone():
        numero_pedidos = 1

    cursor.execute('''SELECT COUNT(*) FROM pedido WHERE cliente LIKE ?''', (f'{rut_id}%',))
    numero_pedidos = cursor.fetchone()[0] + 1
    
    id_pedido = f"{rut_id}_{numero_pedidos}"

    conn.close()
    return id_pedido

def seleccionar_pedido():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedido")
    row = cursor.fetchall()
    for row in row:
        print(row)

    pedido_id = input("Ingrese el ID del pedido: ")

    cursor.execute("SELECT * FROM pedido WHERE id_pedido = ?", (pedido_id,))
    pedido = cursor.fetchone()

    if pedido:
        print(f"Pedido encontrado: {pedido[0]}")
        return pedido_id
    else:
        print("Pedido no encontrado.")
        return  