import sqlite3

def seleccionar_componentes(id_pedido, cliente=None):
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

    try:
        cursor.execute('''
            INSERT INTO lista_componentes (
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

seleccionar_componentes(id_pedido=1)