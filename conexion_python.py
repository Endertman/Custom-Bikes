import sqlite3

def crear_db():
    conn = sqlite3.connect('custom_bikes.db')
    cursor = conn.cursor()

    def crear_tabla_personas():
        cursor.execute('''CREATE TABLE IF NOT EXISTS personas (
            rut_id TEXT NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            telefono INTEGER NOT NULL,
            correo TEXT NOT NULL,
            direccion TEXT NOT NULL,
            PRIMARY KEY(rut_id)
        )''')

    def crear_tabla_cliente():
        cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
            rut_id TEXT NOT NULL UNIQUE,
            altura INTEGER NOT NULL,
            FOREIGN KEY(rut_id) REFERENCES personas(rut_id)
        )''')

    def crear_tabla_tecnico():
        cursor.execute('''CREATE TABLE IF NOT EXISTS tecnico (
            rut_id TEXT NOT NULL UNIQUE,
            especialidad TEXT NOT NULL,
            FOREIGN KEY(rut_id) REFERENCES personas(rut_id)
        )''')

    def crear_tabla_transacciones():
        cursor.execute('''CREATE TABLE IF NOT EXISTS transacciones (
            id_pago INTEGER PRIMARY KEY NOT NULL UNIQUE,
            monto_pagado INTEGER NOT NULL DEFAULT '0'
        )''')

    def crear_tabla_tecnico_pedido():
        cursor.execute('''CREATE TABLE IF NOT EXISTS tecnico_pedido (
            id_pedido INTEGER NOT NULL,
            id_tecnico TEXT NOT NULL,
            FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido),
            FOREIGN KEY(id_tecnico) REFERENCES tecnico(rut_id)
        )''')

    def crear_tabla_historico_pedidos():
        cursor.execute('''CREATE TABLE IF NOT EXISTS historico_pedidos (
            id_pedido INTEGER NOT NULL,
            fecha_entrega_pedido REAL NOT NULL,
            FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido)
        )''')
    
    def crear_tabla_pedido():
        cursor.execute('''CREATE TABLE IF NOT EXISTS pedido (
            id_pedido INTEGER PRIMARY KEY NOT NULL UNIQUE,
            fecha_inicio_pedido REAL NOT NULL,
            tecnicos TEXT NOT NULL,
            cliente TEXT NOT NULL,
            fecha_entrega_pedido REAL NOT NULL,
            FOREIGN KEY(tecnicos) REFERENCES tecnico_pedido(id_tecnico),
            FOREIGN KEY(cliente) REFERENCES cliente(rut_id)
        )''')

    def crear_tabla_almacen():
        cursor.execute('''CREATE TABLE IF NOT EXISTS almacen (
            sku INTEGER PRIMARY KEY NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descuento_individual INTEGER NOT NULL DEFAULT '0',
            stock INTEGER NOT NULL
        )''')
    
    def crear_tabla_componentes():
        cursor.execute('''CREATE TABLE IF NOT EXISTS componentes (
            id_lista_componentes INTEGER PRIMARY KEY NOT NULL UNIQUE,
            marco_sku TEXT NOT NULL,
            transmision_sku TEXT NOT NULL,
            frenos_sku TEXT NOT NULL,
            ruedas_sku TEXT NOT NULL,
            neumaticos_sku TEXT NOT NULL,
            tija_sku TEXT NOT NULL,
            manillar_sku TEXT NOT NULL,
            pedales_sku TEXT NOT NULL,
            sillin_sku TEXT NOT NULL,
            FOREIGN KEY(marco_sku) REFERENCES almacen(sku),
            FOREIGN KEY(transmision_sku) REFERENCES almacen(sku),
            FOREIGN KEY(frenos_sku) REFERENCES almacen(sku),
            FOREIGN KEY(ruedas_sku) REFERENCES almacen(sku),
            FOREIGN KEY(neumaticos_sku) REFERENCES almacen(sku),
            FOREIGN KEY(tija_sku) REFERENCES almacen(sku),
            FOREIGN KEY(manillar_sku) REFERENCES almacen(sku),
            FOREIGN KEY(pedales_sku) REFERENCES almacen(sku),
            FOREIGN KEY(sillin_sku) REFERENCES almacen(sku)
        )''')
        
    def crear_tabla_garantia():
        cursor.execute('''CREATE TABLE IF NOT EXISTS garantia (
            id_pedido TEXT NOT NULL UNIQUE,
            fecha_inicio REAL NOT NULL,
            fecha_fin REAL NOT NULL,
            cobertura TEXT NOT NULL,
            condiciones TEXT NOT NULL,
            estado REAL NOT NULL,
            FOREIGN KEY(id_pedido) REFERENCES historico_pedidos(id_pedido)
        )''')
    
    def crear_tabla_bicicleta():
        cursor.execute('''CREATE TABLE IF NOT EXISTS bicicleta (
            id_pedido INTEGER NOT NULL,
            precio INTEGER NOT NULL,
            FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido),
            FOREIGN KEY(precio) REFERENCES cotizacion(calculo_precio)
        )''')
    
    def crear_tabla_cotizacion():
        cursor.execute('''CREATE TABLE IF NOT EXISTS cotizacion (
            id_pedido INTEGER NOT NULL,
            calculo_precio INTEGER NOT NULL,
            id_lista_componentes INTEGER NOT NULL,
            codigo_descuento INTEGER NOT NULL,
            FOREIGN KEY(id_pedido) REFERENCES bicicleta(id_pedido),
            FOREIGN KEY(id_lista_componentes) REFERENCES componentes(id_lista_componentes),
            FOREIGN KEY(codigo_descuento) REFERENCES cotizacion_codigo(codigo_seleccionado)
        )''')
        
    def crear_tabla_codigos_descuentos():
        cursor.execute('''CREATE TABLE IF NOT EXISTS codigos_descuento (
            codigo_descuento TEXT NOT NULL UNIQUE,
            porcentaje REAL NOT NULL
        )''')
    
    def crear_tabla_boleta():
        cursor.execute('''CREATE TABLE IF NOT EXISTS boleta (
            id_pedido INTEGER NOT NULL UNIQUE,
            precio_final INTEGER NOT NULL,
            id_pago INTEGER NOT NULL,
            FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido),
            FOREIGN KEY(precio_final) REFERENCES bicicleta(precio),
            FOREIGN KEY(id_pago) REFERENCES transacciones(id_pago)
        )''')
    
    def crear_tabla_cotizacion_codigo():
        cursor.execute('''CREATE TABLE IF NOT EXISTS cotizacion_codigo (
            codigo_seleccionado TEXT NOT NULL UNIQUE,
            FOREIGN KEY(codigo_seleccionado) REFERENCES codigos_descuento(codigo_descuento)
        )''')

    crear_tabla_personas()
    crear_tabla_cliente()
    crear_tabla_tecnico()
    crear_tabla_transacciones()
    crear_tabla_tecnico_pedido()
    crear_tabla_historico_pedidos()
    crear_tabla_pedido()
    crear_tabla_almacen()
    crear_tabla_componentes()
    crear_tabla_garantia()
    crear_tabla_bicicleta()
    crear_tabla_cotizacion()
    crear_tabla_codigos_descuentos()
    crear_tabla_boleta()
    crear_tabla_cotizacion_codigo()
    
    conn.commit()
    conn.close()

crear_db()

def inserts():
    conn = sqlite3.connect('custom_bikes.db')
    cursor = conn.cursor()

    def insert_personas():
        cursor.execute('''INSERT INTO personas (rut_id, nombre, apellido, telefono, correo, direccion)
            VALUES
            ('12345678-9', 'Juan', 'Perez', 12345678, 'juan.perez@example.com', 'Calle 123'),
            ('23456789-0', 'Maria', 'Gonzalez', 23456789, 'maria.gonzalez@example.com', 'Avenida 456'),
            ('34567890-1', 'Pedro', 'Rodriguez', 34567890, 'pedro.rodriguez@example.com', 'Plaza 789'),
            ('45678901-2', 'Ana', 'Lopez', 45678901, 'ana.lopez@example.com', 'Calle 321'),
            ('56789012-3', 'Luis', 'Martinez', 56789012, 'luis.martinez@example.com', 'Avenida 654'),
            ('67890123-4', 'Sofia', 'Garcia', 67890123, 'sofia.garcia@example.com', 'Plaza 987'),
            ('78901234-5', 'Carlos', 'Sanchez', 78901234, 'carlos.sanchez@example.com', 'Calle 147'),
            ('89012345-6', 'Laura', 'Hernandez', 89012345, 'laura.hernandez@example.com', 'Avenida 258'),
            ('90123456-7', 'Diego', 'Diaz', 90123456, 'diego.diaz@example.com', 'Plaza 369'),
            ('01234567-8', 'Valeria', 'Torres', 01234567, 'valeria.torres@example.com', 'Calle 753')
        ''')