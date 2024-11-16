import sqlite3
import datetime
from custom_bikes.funciones.funciones_clientes import seleccionar_cliente

def extender_garantia():
    
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()
   
    try: 
        print('Seleccione el tipo de cliente')
        rut_id = seleccionar_cliente()

        cursor.execute(''' SELECT g.id_pedido, g.fecha_inicio, g.fecha_fin, g.estado FROM garantia g JOIN pedido p ON g.id_pedido = p.id_pedido WHERE p.cliente = ?''', (rut_id,))
        garantias = cursor.fetchall()
        
        if not garantias:
            print('El cliente no tiene garantías.')
            return
        
        print(f'Garantías del cliente {rut_id}:')
        print('ID Pedido | Fecha de Inicio | Fecha de Fin | Estado')
        
        for garantia in garantias:
            print(f'{garantia[0]} | {garantia[1]} | {garantia[2]} | {garantia[3]}')

        id_pedido = int(input('Ingrese el ID del pedido para extender la garantía: '))

        cursor.execute(''' SELECT id_pedido FROM garantia WHERE id_pedido = ?''', (id_pedido, ))
        garantia_seleccionada = cursor.fetchone()

        if not garantia_seleccionada:
            print('El pedido no tiene una garantía asociada.')
            return
        
        fecha_fin_actual = datetime.datetime.strptime(garantia_seleccionada[1], '%Y-%m-%d').date()
        dias_extension = int(input('Ingrese la cantidad de días a extender la garantía: '))
        nueva_fecha_fin = fecha_fin_actual + datetime.timedelta(days=dias_extension)

        cursor.execute(''' UPDATE garantia SET fecha_fin = ? WHERE id_pedido = ?''', (nueva_fecha_fin, id_pedido))
        conn.commit()

        print(f'Garantía del pedido {id_pedido} extendida exitosamente hasta {nueva_fecha_fin}')
    
    except sqlite3.Error as e:
        print("Error al extender la garantía:", e)
    
    finally:
        conn.close()

def buscar_garantia():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        print('Seleccione el tipo de cliente')
        rut_id = seleccionar_cliente()

        cursor.execute(''' SELECT g.id_pedido,g.fecha_inicio, g.fecha_fin, g.estado FROM garantia g JOIN pedido p ON g.id_pedido = p.id_pedido WHERE p.cliente = ?''', (rut_id,))
        garantias = cursor.fetchall()

        if not garantias:
            print('El cliente no tiene garantías.')
            return

        print(f'Garantías del cliente {rut_id}:')
        print('ID Pedido | Fecha de Inicio | Fecha de Fin | Estado')

        for garantia in garantias:
            print(f'{garantia[0]} | {garantia[1]} | {garantia[2]} | {garantia[3]}')

    except sqlite3.Error as e:
        print("Error al buscar las garantías:", e)

    finally:
        conn.close()

def mostrar_garantias():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        cursor.execute(''' SELECT g.id_pedido,g.fecha_inicio, g.fecha_fin, g.estado FROM garantia g''')
        garantias = cursor.fetchall()

        if not garantias:
            print('No hay garantías.')
            return

        print('Garantías:')
        print('ID Pedido | Fecha de Inicio | Fecha de Fin | Estado')

        for garantia in garantias:
            print(f'{garantia[0]} | {garantia[1]} | {garantia[2]} | {garantia[3]}')

    except sqlite3.Error as e:
        print("Error al mostrar las garantías:", e)

    finally:
        conn.close()
