import sqlite3
import matplotlib.pyplot as plt
from collections import Counter

def seleccion_tipo():
    tipos_seleccionados = []
    categorias_disponibles = {
        '1': 'Ruta',
        '2': 'MTB',
        '3': 'Urbano'
    }

    print("Categorías disponibles:")
    for key, value in categorias_disponibles.items():
        print(f"{key}. {value}")

    try:
        cantidad_seleccionada = int(input("Ingrese la cantidad de categorías a seleccionar (1-3): "))
        
        if cantidad_seleccionada > 3:
            print("No puede seleccionar más de 3 categorías.")
            return []
        elif cantidad_seleccionada < 1:
            print("Debe seleccionar al menos 1 categoría.")
            return []
        
        for i in range(cantidad_seleccionada):
            categoria = input(f"Ingrese el número de la categoría {i+1}: ")
            
            if categoria in categorias_disponibles:
                tipos_seleccionados.append(categorias_disponibles[categoria])
            else:
                print("Opción no válida. Inténtelo de nuevo.")
                return []

    except ValueError:
        print("Debe ingresar un número válido.")
        return []

    print(f"Categorías seleccionadas: {tipos_seleccionados}")
    return tipos_seleccionados

def seleccion_categoria():
    productos_seleccionados = []
    categorias_disponibles = {
        '1': 'marco_sku',      
        '2': 'transmision_sku', 
        '3': 'frenos_sku',     
        '4': 'ruedas_sku',     
        '5': 'neumaticos_sku',  
        '6': 'tija_sku',       
        '7': 'manillar_sku',    
        '8': 'pedales_sku',     
        '9': 'sillin_sku'      
    }

    print("Categorías disponibles:")
    for key, value in categorias_disponibles.items():
        print(f"{key}. {value}")

    try:
        cantidad_seleccionada = int(input("Ingrese la cantidad de categorías a seleccionar (1-9): "))

        if cantidad_seleccionada > 9:
            print("No puede seleccionar más de 9 categorías.")
            return []
        elif cantidad_seleccionada < 1:
            print("Debe seleccionar al menos 1 categoría.")
            return []

        for i in range(cantidad_seleccionada):
            categoria = input(f"Ingrese el número de la categoría {i+1}: ")

            if categoria in categorias_disponibles:
                productos_seleccionados.append(categorias_disponibles[categoria])
            else:
                print("Opción no válida. Inténtelo de nuevo.")
                return []

    except ValueError:
        print("Debe ingresar un número válido.")
        return []

    print(f"Productos seleccionados: {productos_seleccionados}")
    return productos_seleccionados

def analisis_tipo_bicicleta(tipos_seleccionados):
    if not tipos_seleccionados:
        print("No se seleccionaron categorías válidas. Análisis cancelado.")
        return

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        placeholders = ','.join(['?'] * len(tipos_seleccionados))
        query = f"""
            SELECT a.categoria, COUNT(*) as cantidad
            FROM pedido p
            JOIN bicicleta b ON p.id_pedido = b.id_pedido
            JOIN componentes c ON b.id_pedido = c.id_pedido
            JOIN almacen a ON c.marco_sku = a.sku
            WHERE a.categoria IN ({placeholders})
            GROUP BY a.categoria
            ORDER BY cantidad DESC;
        """

        cursor.execute(query, tipos_seleccionados)
        resultados = cursor.fetchall()

        if resultados:
            print("\nResultados del Análisis de Tipo de Bicicleta:")
            print(f"{'Tipo de Bicicleta':<20}{'Cantidad':<10}")
            print("-" * 30)
            for tipo, cantidad in resultados:
                print(f"{tipo:<20}{cantidad:<10}")
            
            tipos = [row[0] for row in resultados]
            cantidades = [row[1] for row in resultados]

            plt.figure(figsize=(8, 6))
            plt.bar(tipos, cantidades, color='skyblue', edgecolor='black')
            plt.title('Clientes Bike')
            plt.xlabel('Tipo de Bicicleta')
            plt.ylabel('Cantidad')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        else:
            print("No se encontraron resultados para las categorías seleccionadas.")
    
    except sqlite3.Error as e:
        print(f"Error al realizar el análisis: {e}")
    
    finally:
        conn.close()

def analisis_categoria_producto(productos_seleccionados):
    if not productos_seleccionados:
        print("No se seleccionaron productos válidos. Análisis cancelado.")
        return

    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        columnas = ', '.join([f'c.{producto}' for producto in productos_seleccionados])
        query = f"""
        SELECT {columnas}
        FROM componentes c
        """
        
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            conteos = {producto: 0 for producto in productos_seleccionados}

            for fila in resultados:
                for i, producto in enumerate(productos_seleccionados):
                    if fila[i]:
                        conteos[producto] += 1

            print("\nConteo de productos seleccionados:")
            for producto, cantidad in conteos.items():
                print(f"{producto:<20}{cantidad:<10}")
            
            # Preparar los datos para el gráfico
            productos = list(conteos.keys())
            cantidades = list(conteos.values())

            # Crear el gráfico
            plt.figure(figsize=(10, 6))
            plt.bar(productos, cantidades, color='skyblue', edgecolor='black')
            plt.title('Clientes Bike')
            plt.xlabel('Producto')
            plt.ylabel('Cantidad')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

        else:
            print("No se encontraron datos en las columnas seleccionadas.")
    
    except sqlite3.Error as e:
        print(f"Error al realizar el análisis: {e}")
    
    finally:
        conn.close()

def contar_repeticiones_sku():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
    cursor = conn.cursor()

    try:
        columnas_componentes = [
            'marco_sku', 'transmision_sku', 'frenos_sku', 'ruedas_sku',
            'neumaticos_sku', 'tija_sku', 'manillar_sku', 'pedales_sku', 'sillin_sku'
        ]
        
        all_skus = []

        for columna in columnas_componentes:
            query = f"""
            SELECT {columna}
            FROM componentes c
            WHERE c.{columna} IS NOT NULL
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            all_skus.extend([fila[0] for fila in resultados])

        conteos_skus = Counter(all_skus)

        skus = list(conteos_skus.keys())
        cantidades = list(conteos_skus.values())

        sku_to_nombre = {
                'SKU_R001': 'Marco Ruta Carbono',
                'SKU_R002': 'Marco Ruta Aluminio',
                'SKU_R003': 'Marco Ruta Titanio',
                'SKU_R004': 'Transmisión Ruta Shimano',
                'SKU_R005': 'Transmisión Ruta SRAM',
                'SKU_R006': 'Transmisión Ruta Campagnolo',
                'SKU_R007': 'Frenos Ruta Hidráulicos',
                'SKU_R008': 'Frenos Ruta Mecánicos',
                'SKU_R009': 'Frenos Ruta Disco',
                'SKU_R010': 'Ruedas Ruta Aero',
                'SKU_R011': 'Ruedas Ruta Ligeras',
                'SKU_R012': 'Ruedas Ruta Montaña',
                'SKU_R013': 'Neumáticos Ruta Competición',
                'SKU_R014': 'Neumáticos Ruta Resistencia',
                'SKU_R015': 'Neumáticos Ruta All-Terrain',
                'SKU_R016': 'Tija Ruta Carbono',
                'SKU_R017': 'Tija Ruta Aluminio',
                'SKU_R018': 'Tija Ruta Aero',
                'SKU_R019': 'Manillar Ruta Drop',
                'SKU_R020': 'Manillar Ruta Compact',
                'SKU_R021': 'Manillar Ruta Aero',
                'SKU_R022': 'Pedales Ruta Clip',
                'SKU_R023': 'Pedales Ruta Plataforma',
                'SKU_R024': 'Pedales Ruta Mixtos',
                'SKU_R025': 'Sillín Ruta Ligero',
                'SKU_R026': 'Sillín Ruta Aero',
                'SKU_R027': 'Sillín Ruta Gel',
                'SKU_M001': 'Marco MTB Aluminio',
                'SKU_M002': 'Marco MTB Carbono',
                'SKU_M003': 'Marco MTB Acero',
                'SKU_M004': 'Transmisión MTB Shimano',
                'SKU_M005': 'Transmisión MTB SRAM',
                'SKU_M006': 'Transmisión MTB MicroSHIFT',
                'SKU_M007': 'Frenos MTB Disco Hidráulicos',
                'SKU_M008': 'Frenos MTB Disco Mecánicos',
                'SKU_M009': 'Frenos MTB V-Brake',
                'SKU_M010': 'Ruedas MTB 29 pulgadas',
                'SKU_M011': 'Ruedas MTB 27.5 pulgadas',
                'SKU_M012': 'Ruedas MTB Tubeless',
                'SKU_M013': 'Neumáticos MTB Competición',
                'SKU_M014': 'Neumáticos MTB All-Mountain',
                'SKU_M015': 'Neumáticos MTB Downhill',
                'SKU_M016': 'Tija MTB Aluminio',
                'SKU_M017': 'Tija MTB Carbono',
                'SKU_M018': 'Tija MTB Dropper',
                'SKU_M019': 'Manillar MTB Riser',
                'SKU_M020': 'Manillar MTB Flat',
                'SKU_M021': 'Manillar MTB DH',
                'SKU_M022': 'Pedales MTB Plataforma',
                'SKU_M023': 'Pedales MTB Clipless',
                'SKU_M024': 'Pedales MTB Mixtos',
                'SKU_M025': 'Sillín MTB Enduro',
                'SKU_M026': 'Sillín MTB Gel',
                'SKU_M027': 'Sillín MTB Ligero',
                'SKU_U001': 'Marco Urbano Aluminio',
                'SKU_U002': 'Marco Urbano Acero',
                'SKU_U003': 'Marco Urbano Carbono',
                'SKU_U004': 'Transmisión Urbano Shimano',
                'SKU_U005': 'Transmisión Urbano Nexus',
                'SKU_U006': 'Transmisión Urbano SRAM',
                'SKU_U007': 'Frenos Urbano Disco',
                'SKU_U008': 'Frenos Urbano V-Brake',
                'SKU_U009': 'Frenos Urbano Hidráulicos',
                'SKU_U010': 'Ruedas Urbano Ligeras',
                'SKU_U011': 'Ruedas Urbano Aero',
                'SKU_U012': 'Ruedas Urbano Resistencia',
                'SKU_U013': 'Neumáticos Urbano Antipinchazos',
                'SKU_U014': 'Neumáticos Urbano All-Terrain',
                'SKU_U015': 'Neumáticos Urbano Plegables',
                'SKU_U016': 'Tija Urbano Aluminio',
                'SKU_U017': 'Tija Urbano Carbono',
                'SKU_U018': 'Tija Urbano Ajustable',
                'SKU_U019': 'Manillar Urbano Recto',
                'SKU_U020': 'Manillar Urbano Curvo',
                'SKU_U021': 'Manillar Urbano Plegable',
                'SKU_U022': 'Pedales Urbano Plataforma',
                'SKU_U023': 'Pedales Urbano Clip',
                'SKU_U024': 'Pedales Urbano Plegables',
                'SKU_U025': 'Sillín Urbano Confort',
                'SKU_U026': 'Sillín Urbano Gel',
                'SKU_U027': 'Sillín Urbano Plegable'
        }

        nombres_productos = [sku_to_nombre.get(sku, sku) for sku in skus]

        print("\nConteo de repeticiones de SKUs:")
        for sku, cantidad in zip(nombres_productos, cantidades):
            print(f"{sku:<30}{cantidad:<10}")

        if nombres_productos:
            plt.figure(figsize=(16, 14))
            plt.bar(nombres_productos, cantidades, color='skyblue', edgecolor='black', width=0.5)
            plt.title('Ventas de productos')
            plt.xlabel('Producto')
            plt.ylabel('Cantidad')
            plt.xticks(rotation=45, ha='right', fontsize=10)  
            plt.tight_layout()  
            plt.show()

        else:
            print("No se encontraron SKUs repetidos en la base de datos.")
    
    except sqlite3.Error as e:
        print(f"Error al realizar el análisis: {e}")
    
    finally:
        conn.close()