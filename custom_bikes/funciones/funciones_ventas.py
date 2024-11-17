import sqlite3, csv, random, string, datetime, os
from custom_bikes.funciones.funciones_pedido import id_pedido
from custom_bikes.funciones.funciones_clientes import insert_cliente, seleccionar_cliente

import sqlite3
import csv
import os

import sqlite3
import csv
import os

def agregar_venta_csv():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_csv_pedidos = os.path.join(ruta_base, '../../datos/pedido_respaldo.csv')
    ruta_csv_tecnico_pedido = os.path.join(ruta_base, '../../datos/tecnico_pedido_respaldo.csv')
    ruta_csv_lista_componentes = os.path.join(ruta_base, '../../datos/lista_componentes_respaldo.csv')
    ruta_csv_cotizacion_codigo = os.path.join(ruta_base, '../../datos/cotizacion_codigo_respaldo.csv')
    ruta_csv_historico_pedidos = os.path.join(ruta_base, '../../datos/historico_pedidos_respaldo.csv')
    ruta_csv_garantia_respaldo = os.path.join(ruta_base, '../../datos/garantia_respaldo.csv')

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        with open(ruta_csv_pedidos, 'r') as pedidos_file:
            pedidos_reader = csv.reader(pedidos_file)
            next(pedidos_reader)

            for pedidos_row in pedidos_reader:
                rut_id = pedidos_row[0]
                fecha_inicio_pedido = pedidos_row[1]
                cliente = pedidos_row[2]
                fecha_entrega_pedido = pedidos_row[3]

                pedido_id = id_pedido(rut_id)
                if not pedido_id:
                    print("Error al obtener el ID del pedido.")
                    continue

                cursor.execute('''SELECT id_pedido FROM pedido WHERE id_pedido = ?''', (pedido_id,))
                if cursor.fetchone():
                    print(f"El pedido {pedido_id} ya existe. Omitiendo.")
                    continue

                try:
                    cursor.execute('''INSERT INTO pedido (id_pedido, fecha_inicio_pedido, cliente, fecha_entrega_pedido) VALUES (?, ?, ?, ?)''',
                                   (pedido_id, fecha_inicio_pedido, cliente, fecha_entrega_pedido))
                    conn.commit()
                    print(f"Pedido {pedido_id} agregado correctamente.")

                    with open(ruta_csv_tecnico_pedido, 'r') as tecnico_pedido_file:
                        tecnico_pedido_reader = csv.reader(tecnico_pedido_file)
                        next(tecnico_pedido_reader)

                        for tecnico_pedido_row in tecnico_pedido_reader:
                            if tecnico_pedido_row[0] == rut_id:
                                tecnico_id = tecnico_pedido_row[1]

                                cursor.execute('''INSERT INTO tecnico_pedido (id_pedido, id_tecnico) VALUES (?, ?)''', (pedido_id, tecnico_id))
                                conn.commit()
                                print(f"Técnico {tecnico_id} asignado al pedido {pedido_id}.")
                                break 

                    total_precio = 0
                    with open(ruta_csv_lista_componentes, 'r') as componentes_file:
                        componentes_reader = csv.reader(componentes_file)
                        next(componentes_reader)

                        for componentes_row in componentes_reader:
                            if componentes_row[0] == rut_id:
                                marco_sku, transmision_sku, frenos_sku, ruedas_sku, neumaticos_sku, tija_sku, manillar_sku, pedales_sku, sillin_sku = componentes_row[1:]
                                ids_componentes = [marco_sku, transmision_sku, frenos_sku, ruedas_sku, neumaticos_sku, tija_sku, manillar_sku, pedales_sku, sillin_sku]
                                total_precio = generar_precio(ids_componentes)

                                cursor.execute('''INSERT INTO componentes (id_pedido, marco_sku, transmision_sku, frenos_sku, ruedas_sku, neumaticos_sku, tija_sku, manillar_sku, pedales_sku, sillin_sku) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                               (pedido_id, marco_sku, transmision_sku, frenos_sku, ruedas_sku, neumaticos_sku, tija_sku, manillar_sku, pedales_sku, sillin_sku))
                                conn.commit()
                                break 

                    with open(ruta_csv_cotizacion_codigo, 'r') as cotizacion_codigo_file:
                        cotizacion_codigo_reader = csv.reader(cotizacion_codigo_file)
                        next(cotizacion_codigo_reader)

                        for cotizacion_codigo_row in cotizacion_codigo_reader:
                            if cotizacion_codigo_row[0] == rut_id: 
                                codigo = cotizacion_codigo_row[1]
                                id_pago = generar_codigo_transaccion(longitud=8)

                                cursor.execute('''SELECT porcentaje FROM codigos_descuentos WHERE codigo = ?''', (codigo,))
                                descuento = cursor.fetchone()

                                if descuento:
                                    descuento_porcentaje = descuento[0]
                                    precio_final = total_precio - (total_precio * descuento_porcentaje)
                                else:
                                    print(f"No se encontró un descuento para el código {codigo}.")
                                    precio_final = total_precio

                                cursor.execute('''INSERT INTO bicicleta (id_pedido, precio) VALUES (?, ?)''', (pedido_id, precio_final))
                                cursor.execute('''INSERT INTO cotizacion_codigo (id_pedido, codigo_seleccionado) VALUES (?, ?)''', (pedido_id, codigo))
                                cursor.execute('''INSERT INTO boleta (id_pedido, precio_final, id_pago) VALUES (?, ?, ?)''', (pedido_id, precio_final, id_pago))
                                cursor.execute('''INSERT INTO transacciones (id_pago, monto_pagado) VALUES (?, ?)''', (id_pago, precio_final))
                                conn.commit()
                                break  

                    with open(ruta_csv_historico_pedidos, 'r') as historico_pedido_file:
                        historico_pedido_reader = csv.reader(historico_pedido_file)
                        next(historico_pedido_reader)

                        for historico_pedido_row in historico_pedido_reader:
                            if historico_pedido_row[0] == rut_id:  
                                fecha_entrega = historico_pedido_row[1]

                                cursor.execute('''INSERT INTO historico_pedidos (id_pedido, fecha_entrega_pedido) VALUES (?, ?)''', (pedido_id, fecha_entrega))
                                conn.commit()
                                break 

                    with open(ruta_csv_garantia_respaldo, 'r') as garantia_file:
                        garantia_reader = csv.reader(garantia_file)
                        next(garantia_reader)

                        for garantia_row in garantia_reader:
                            if garantia_row[0] == rut_id:
                                fecha_inicio = garantia_row[1]
                                fecha_fin = garantia_row[2]
                                cobertura = garantia_row[3]
                                condiciones = garantia_row[4]
                                estado = garantia_row[5]

                                cursor.execute('''INSERT INTO garantia (id_pedido, fecha_inicio, fecha_fin, cobertura, condiciones, estado) VALUES (?, ?, ?, ?, ?, ?)''',
                                               (pedido_id, fecha_inicio, fecha_fin, cobertura, condiciones, estado))
                                conn.commit()
                                break

                except sqlite3.Error as e:
                    print(f"Error al agregar el pedido {pedido_id}: {e}")
                    continue

    except Exception as e:
        print(f"Error general al procesar los archivos: {e}")

    finally:
        conn.close()


def agregar_venta_cliente_nuevo():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    rut_id = insert_cliente()
    pedido_id = id_pedido(rut_id)
    ids_componentes = seleccionar_componentes(pedido_id)
    total_precio = generar_precio(ids_componentes)
    fecha_inicio_pedido = datetime.date.today()
    fecha_entrega_pedido = fecha_inicio_pedido + datetime.timedelta(days=30)
    id_pago = generar_codigo_transaccion(longitud=8)

    cursor.execute('''INSERT INTO pedido (id_pedido, fecha_inicio_pedido, cliente, fecha_entrega_pedido) VALUES (?, ?, ?, ?)''', (pedido_id, fecha_inicio_pedido, rut_id, fecha_entrega_pedido))
    cursor.execute('''INSERT INTO cotizacion (id_pedido, total_precio) VALUES (?, ?)''', (pedido_id, total_precio))
    cursor.execute('''INSERT INTO bicicleta (id_pedido, precio) VALUES (?, ?)''', (pedido_id, precio_final))

    codigo_descuento = input("Ingrese el código de descuento (si no tiene, presione Enter): ")
    if codigo_descuento:
        cursor.execute('''SELECT porcentaje FROM codigos_descuentos WHERE codigo = ?''', (codigo_descuento,))
        descuento = cursor.fetchone()
        if descuento:
            descuento_porcentaje = descuento[0]
            precio_final = total_precio - (total_precio * descuento_porcentaje)
            cursor.execute('''INSERT INTO cotizacion_codigo (id_pedido, codigo_seleccionado) VALUES (?, ?)''', (pedido_id, codigo_descuento))
        else:
            print("Código de descuento no válido.")
            precio_final = total_precio

    cursor.execute('''INSERT INTO boleta (id_pedido, precio_final, id_pago) VALUES (?, ?, ?)''', (pedido_id, precio_final, id_pago))
    cursor.execute('''INSERT INTO transaciones (id_pago, monto_pagado) VALUES (?, ?)''', (id_pago, precio_final))

    cursor.execute('''INSERT INTO historico_pedido (id_pedido, fecha_entrega_pedido) VALUES (?, ?)''', (pedido_id, fecha_entrega_pedido))
    cursor.execute('''INSERT INTO garantia (id_pedido, fecha_inicio, fecha_fin, cobertura, condiciones, estado) VALUES (?, ?, ?, ?, ?, ?)''', (pedido_id, fecha_inicio_pedido, fecha_entrega_pedido, 'Cobertura por defecto', 'Condiciones por defecto', 'En proceso'))

    conn.commit()
    conn.close()

    generar_factura(rut_id, pedido_id, fecha_inicio_pedido, fecha_entrega_pedido, total_precio, descuento_porcentaje, precio_final, id_pago, ids_componentes, codigo_descuento)

def agregar_venta_cliente_existente():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    rut_id = seleccionar_cliente()
    pedido_id = id_pedido(rut_id)
    ids_componentes = seleccionar_componentes(pedido_id)
    total_precio = generar_precio(ids_componentes)
    fecha_inicio_pedido = datetime.date.today()
    fecha_entrega_pedido = fecha_inicio_pedido + datetime.timedelta(days=30)
    id_pago = generar_codigo_transaccion(longitud=8)

    cursor.execute('''INSERT INTO pedido (id_pedido, fecha_inicio_pedido, cliente, fecha_entrega_pedido) VALUES (?, ?, ?, ?)''', (pedido_id, fecha_inicio_pedido, rut_id, fecha_entrega_pedido))
    cursor.execute('''INSERT INTO cotizacion (id_pedido, total_precio) VALUES (?, ?)''', (pedido_id, total_precio))
    cursor.execute('''INSERT INTO bicicleta (id_pedido, precio) VALUES (?, ?)''', (pedido_id, precio_final))

    codigo_descuento = input("Ingrese el código de descuento (si no tiene, presione Enter): ")
    if codigo_descuento:
        cursor.execute('''SELECT porcentaje FROM codigos_descuentos WHERE codigo = ?''', (codigo_descuento,))
        descuento = cursor.fetchone()
        if descuento:
            descuento_porcentaje = descuento[0]
            precio_final = total_precio - (total_precio * descuento_porcentaje)
            cursor.execute('''INSERT INTO cotizacion_codigo (id_pedido, codigo_seleccionado) VALUES (?, ?)''', (pedido_id, codigo_descuento))
        else:
            print("Código de descuento no válido.")
            precio_final = total_precio

    cursor.execute('''INSERT INTO boleta (id_pedido, precio_final, id_pago) VALUES (?, ?, ?)''', (pedido_id, precio_final, id_pago))
    cursor.execute('''INSERT INTO transaciones (id_pago, monto_pagado) VALUES (?, ?)''', (id_pago, precio_final))

    cursor.execute('''INSERT INTO historico_pedido (id_pedido, fecha_entrega_pedido) VALUES (?, ?)''', (pedido_id, fecha_entrega_pedido))
    cursor.execute('''INSERT INTO garantia (id_pedido, fecha_inicio, fecha_fin, cobertura, condiciones, estado) VALUES (?, ?, ?, ?, ?, ?)''', (pedido_id, fecha_inicio_pedido, fecha_entrega_pedido, 'Cobertura por defecto', 'Condiciones por defecto', 'En proceso'))

    conn.commit()
    conn.close()

    generar_factura(rut_id, pedido_id, fecha_inicio_pedido, fecha_entrega_pedido, total_precio, descuento_porcentaje, precio_final, id_pago, ids_componentes, codigo_descuento)

def seleccionar_componentes(id_pedido):
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    componentes_necesarios = {
        "marco_sku": "Marco",
        "transmision_sku": "Transmisión",
        "frenos_sku": "Frenos",
        "ruedas_sku": "Ruedas",
        "neumaticos_sku": "Neumáticos",
        "tija_sku": "Tija",
        "manillar_sku": "Manillar",
        "pedales_sku": "Pedales",
        "sillin_sku": "Sillín"
    }

    componentes_seleccionados = {}

    print('Seleccione el tipo de bicicleta a comprar')
    print('1. Bicicleta de montaña')
    print('2. Bicicleta de ruta')
    print('3. Bicicleta de ciudad')
    
    seleccion_tipo = int(input('Seleccione una opción: '))

    if seleccion_tipo == 1:
        categoria = 'MTB'
    elif seleccion_tipo == 2:
        categoria = 'Ruta'
    elif seleccion_tipo == 3:
        categoria = 'Ciudad'
    else:
        print("Opción no válida.")
        conn.close()
        return

    for sku, tipo in componentes_necesarios.items():
        while True:
            print(f"\nSeleccione el componente para {tipo}:")

            cursor.execute('''SELECT * FROM almacen WHERE categoria = ? AND tipo = ? AND stock > 0''', (categoria, tipo))
            resultados = cursor.fetchall()

            if resultados:
                print("\nComponentes disponibles:")
                for index, row in enumerate(resultados, start=1):
                    print(f'{index}. {row}')
                
                seleccion_componente = int(input('\nSeleccione el número del componente: '))

                if 1 <= seleccion_componente <= len(resultados):
                    componente_seleccionado = resultados[seleccion_componente - 1]
                    componentes_seleccionados[sku] = componente_seleccionado[0]  # Almacena el SKU del componente
                    print(f'\nComponente seleccionado para {tipo}: {componente_seleccionado[1]}')
                    break
                else:
                    print("Opción de componente no válida.")
            else:
                print(f"\nNo se encontraron componentes disponibles para {tipo}.")
                break

    ids_componentes = list(componentes_seleccionados.values())  

    try:
        cursor.execute('''
            INSERT INTO componentes (
                id_pedido, marco_sku, transmision_sku, frenos_sku, ruedas_sku, 
                neumaticos_sku, tija_sku, manillar_sku, pedales_sku, sillin_sku
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            id_pedido,
            componentes_seleccionados.get("marco_sku"),
            componentes_seleccionados.get("transmision_sku"),
            componentes_seleccionados.get("frenos_sku"),
            componentes_seleccionados.get("ruedas_sku"),
            componentes_seleccionados.get("neumaticos_sku"),
            componentes_seleccionados.get("tija_sku"),
            componentes_seleccionados.get("manillar_sku"),
            componentes_seleccionados.get("pedales_sku"),
            componentes_seleccionados.get("sillin_sku")
        ))
        conn.commit()
        print("\nComponentes seleccionados guardados exitosamente en la base de datos.")
    except sqlite3.Error as e:
        print(f"Error al guardar los componentes: {e}")
        conn.rollback()

    conn.close()

    return ids_componentes

def generar_precio(ids_componentes):
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    placeholders = ', '.join('?' for _ in ids_componentes)
    query = f"SELECT precio FROM almacen WHERE sku IN ({placeholders})"

    cursor.execute(query, ids_componentes)
    precios = cursor.fetchall()
    total_precio = sum(precio[0] for precio in precios)
    
    conn.close()

    return total_precio

def generar_codigo_transaccion(longitud=8):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return codigo

def generar_factura(rut_id, pedido_id, fecha_inicio_pedido, fecha_entrega_pedido, total_precio, descuento_porcentaje, precio_final, id_pago, ids_componentes, codigo_descuento):
    print("="*50)
    print(" " * 15 + "FACTURA DE VENTA")
    print("="*50)
    
    print(f"ID del Cliente: {rut_id}")
    print(f"ID del Pedido: {pedido_id}")
    print(f"Fecha de Inicio del Pedido: {fecha_inicio_pedido}")
    print(f"Fecha de Entrega: {fecha_entrega_pedido}")
    
    print("-" * 50)
    
    print("Componentes Seleccionados:")
    for componente in ids_componentes:
        print(f"- {componente}")
    
    print("-" * 50)

    print(f"Precio Total de los Componentes: ${total_precio}")
    print(f"Descuento Aplicado: {descuento_porcentaje}%")
    print(f"Precio Final (con descuento): ${precio_final}")
    
    print("-" * 50)

    print(f"Código de Transacción: {id_pago}")
    print(f"Código de Descuento Aplicado: {codigo_descuento}")
    
    print("="*50)
    print("Gracias por su compra.")
    print("="*50)

def eliminar_venta(pedido_id_seleccionado):
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''DELETE FROM garantia WHERE id_pedido = ?''', (pedido_id,))
        cursor.execute('''DELETE FROM historico_pedido WHERE id_pedido = ?''', (pedido_id,))
        cursor.execute('''DELETE FROM transacciones WHERE id_pago = (SELECT id_pago FROM boleta WHERE id_pedido = ?)''', (pedido_id,))
        cursor.execute('''DELETE FROM boleta WHERE id_pedido = ?''', (pedido_id,))
        cursor.execute('''DELETE FROM cotizacion_codigo WHERE id_pedido = ?''', (pedido_id,))
        cursor.execute('''DELETE FROM cotizacion WHERE id_pedido = ?''', (pedido_id,))
        cursor.execute('''DELETE FROM bicicleta WHERE id_pedido = ?''', (pedido_id,))
        cursor.execute('''DELETE FROM pedido WHERE id_pedido = ?''', (pedido_id,))

        conn.commit()
        print(f"Venta con ID {pedido_id} eliminada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar la venta: {e}")
        conn.rollback()
    finally:
        conn.close()

def modificar_venta(pedido_id_seleccionado):
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM componentes WHERE id_pedido = ?''', (pedido_id_seleccionado,))
    componentes_existentes = cursor.fetchone()

    if not componentes_existentes:
        print(f"No se encontraron componentes para el pedido con ID {pedido_id_seleccionado}.")
        conn.close()
        return

    print(f"Componentes actuales para el pedido {pedido_id_seleccionado}:")
    print(componentes_existentes)

    marco_sku = input("Ingrese nuevo marco SKU (dejar vacío para mantener el actual): ")
    if not marco_sku:
        marco_sku = componentes_existentes[1]

    transmision_sku = input("Ingrese nueva transmisión SKU (dejar vacío para mantener el actual): ")
    if not transmision_sku:
        transmision_sku = componentes_existentes[2]

    frenos_sku = input("Ingrese nuevo frenos SKU (dejar vacío para mantener el actual): ")
    if not frenos_sku:
        frenos_sku = componentes_existentes[3]

    ruedas_sku = input("Ingrese nuevas ruedas SKU (dejar vacío para mantener el actual): ")
    if not ruedas_sku:
        ruedas_sku = componentes_existentes[4]

    neumaticos_sku = input("Ingrese nuevos neumáticos SKU (dejar vacío para mantener el actual): ")
    if not neumaticos_sku:
        neumaticos_sku = componentes_existentes[5]

    tija_sku = input("Ingrese nueva tija SKU (dejar vacío para mantener el actual): ")
    if not tija_sku:
        tija_sku = componentes_existentes[6]

    manillar_sku = input("Ingrese nuevo manillar SKU (dejar vacío para mantener el actual): ")
    if not manillar_sku:
        manillar_sku = componentes_existentes[7]

    pedales_sku = input("Ingrese nuevos pedales SKU (dejar vacío para mantener el actual): ")
    if not pedales_sku:
        pedales_sku = componentes_existentes[8]

    sillin_sku = input("Ingrese nuevo sillín SKU (dejar vacío para mantener el actual): ")
    if not sillin_sku:
        sillin_sku = componentes_existentes[9]

    try:
        cursor.execute('''UPDATE componentes
                          SET marco_sku = ?, transmision_sku = ?, frenos_sku = ?, ruedas_sku = ?, 
                              neumaticos_sku = ?, tija_sku = ?, manillar_sku = ?, pedales_sku = ?, sillin_sku = ?
                          WHERE id_pedido = ?''', 
                          (marco_sku, transmision_sku, frenos_sku, ruedas_sku, neumaticos_sku, tija_sku, manillar_sku, pedales_sku, sillin_sku, pedido_id_seleccionado))

        conn.commit()
        print(f"Componentes del pedido {pedido_id_seleccionado} modificados exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al modificar los componentes del pedido {pedido_id_seleccionado}: {e}")
        conn.rollback()

    finally:
        conn.close()

def buscar_venta(pedido_id_seleccionado):
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        # Consultamos los detalles de un pedido específico
        cursor.execute('''
            SELECT p.id_pedido, p.fecha_inicio_pedido, p.cliente, p.fecha_entrega_pedido, 
                   c.total_precio, b.precio, t.monto_pagado, h.fecha_entrega_pedido, g.estado
            FROM pedido p
            JOIN cotizacion c ON p.id_pedido = c.id_pedido
            JOIN bicicleta b ON p.id_pedido = b.id_pedido
            JOIN transaciones t ON p.id_pedido = t.id_pago
            JOIN historico_pedido h ON p.id_pedido = h.id_pedido
            JOIN garantia g ON p.id_pedido = g.id_pedido
            WHERE p.id_pedido = ?
        ''', (pedido_id_seleccionado,))
        
        pedido = cursor.fetchone()

        if pedido:
            # Mostrar los resultados
            print(f"{'ID Pedido':<20}{'Fecha Inicio':<15}{'Cliente':<20}{'Fecha Entrega':<15}{'Total Precio':<15}{'Precio Final':<15}{'Monto Pagado':<15}{'Fecha Entrega Hist':<20}{'Estado Garantía':<15}")
            print("="*120)

            print(f"{pedido[0]:<20}{pedido[1]:<15}{pedido[2]:<20}{pedido[3]:<15}{pedido[4]:<15}{pedido[5]:<15}{pedido[6]:<15}{pedido[7]:<20}{pedido[8]:<15}")
        
        else:
            print(f"No se encontró el pedido con ID: {pedido_id_seleccionado}")

    except sqlite3.Error as e:
        print(f"Error al obtener el pedido: {e}")

    finally:
        conn.close()

def mostrar_ventas():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT p.id_pedido, p.fecha_inicio_pedido, p.cliente, p.fecha_entrega_pedido, 
                   c.total_precio, b.precio, t.monto_pagado, h.fecha_entrega_pedido, g.estado
            FROM pedido p
            JOIN cotizacion c ON p.id_pedido = c.id_pedido
            JOIN bicicleta b ON p.id_pedido = b.id_pedido
            JOIN transaciones t ON p.id_pedido = t.id_pago
            JOIN historico_pedido h ON p.id_pedido = h.id_pedido
            JOIN garantia g ON p.id_pedido = g.id_pedido
        ''')
        
        pedidos = cursor.fetchall()

        if pedidos:
            print(f"{'ID Pedido':<20}{'Fecha Inicio':<15}{'Cliente':<20}{'Fecha Entrega':<15}{'Total Precio':<15}{'Precio Final':<15}{'Monto Pagado':<15}{'Fecha Entrega Hist':<20}{'Estado Garantía':<15}")
            print("="*120)

            for pedido in pedidos:
                print(f"{pedido[0]:<20}{pedido[1]:<15}{pedido[2]:<20}{pedido[3]:<15}{pedido[4]:<15}{pedido[5]:<15}{pedido[6]:<15}{pedido[7]:<20}{pedido[8]:<15}")
        
        else:
            print("No hay pedidos registrados.")

    except sqlite3.Error as e:
        print(f"Error al obtener los pedidos: {e}")

    finally:
        conn.close()