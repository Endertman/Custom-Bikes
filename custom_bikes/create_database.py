import sqlite3

def crear_db():
    conn = sqlite3.connect('custom_bikes.db')
    cursor = conn.cursor()

    def crear_tabla_personas():
        cursor.execute('''CREATE TABLE IF NOT EXISTS personas (
            rut_id TEXT NOT NULL,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            telefono INTEGER NOT NULL,
            correo TEXT NOT NULL,
            direccion TEXT NOT NULL,
            PRIMARY KEY(rut_id)
        )''')

    def crear_tabla_clientes():
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
            rut_id TEXT NOT NULL,
            altura INTEGER NOT NULL,
            PRIMARY KEY(rut_id),
            FOREIGN KEY(rut_id) REFERENCES personas(rut_id) ON DELETE CASCADE
        )''')

    def crear_tabla_tecnicos():
        cursor.execute('''CREATE TABLE IF NOT EXISTS tecnicos (
            rut_id TEXT NOT NULL,
            especialidad TEXT NOT NULL,
            PRIMARY KEY(rut_id),
            FOREIGN KEY(rut_id) REFERENCES personas(rut_id) ON DELETE CASCADE
        )''')

    def crear_tabla_tecnico_pedido():
        cursor.execute('''CREATE TABLE IF NOT EXISTS tecnico_pedido (
            id_pedido TEXT NOT NULL,
            id_tecnico TEXT NOT NULL,
            PRIMARY KEY("id_pedido","id_tecnico"),
            FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
            FOREIGN KEY(id_tecnico) REFERENCES tecnico(rut_id)
        )''')

    def crear_tabla_pedido():
        cursor.execute('''CREATE TABLE IF NOT EXISTS pedido (
            id_pedido TEXT NOT NULL,
            fecha_inicio_pedido TEXT NOT NULL,
            cliente TEXT NOT NULL,
            fecha_entrega_pedido TEXT NOT NULL,
            PRIMARY KEY("id_pedido"),
            FOREIGN KEY(cliente) REFERENCES cliente(rut_id)
        )''')

    def crear_tabla_almacen():
        cursor.execute('''CREATE TABLE IF NOT EXISTS almacen (
            sku TEXT NOT NULL,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descuento_individual INTEGER NOT NULL DEFAULT '0',
            stock INTEGER NOT NULL  DEFAULT '0',
            precio INTEGER NOT NULL,
            PRIMARY KEY("sku")
        )''')

    def crear_tabla_componentes():
        cursor.execute('''CREATE TABLE IF NOT EXISTS componentes (
            "id_pedido" INTEGER NOT NULL,
            "marco_sku" TEXT NOT NULL,
            "transmision_sku" TEXT NOT NULL,
            "frenos_sku" TEXT NOT NULL,
            "ruedas_sku" TEXT NOT NULL,
            "neumaticos_sku" TEXT NOT NULL,
            "tija_sku" TEXT NOT NULL,
            "manillar_sku" TEXT NOT NULL,
            "pedales_sku" TEXT NOT NULL,
            "sillin_sku" TEXT NOT NULL,
            PRIMARY KEY("id_pedido"),
            FOREIGN KEY("id_pedido") REFERENCES "pedido"("id_pedido"),
            FOREIGN KEY("marco_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("transmision_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("frenos_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("ruedas_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("neumaticos_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("tija_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("manillar_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("pedales_sku") REFERENCES "almacen"("sku"),
            FOREIGN KEY("sillin_sku") REFERENCES "almacen"("sku")
        )''')
   
    def crear_tabla_cotizacion():
       cursor.execute('''CREATE TABLE IF NOT EXISTS cotizacion (
           id_pedido TEXT NOT NULL,
           calculo_precio INTEGER NOT NULL,
           PRIMARY KEY(id_pedido),
           FOREIGN KEY(id_pedido) REFERENCES componentes(id_pedido) ON DELETE CASCADE
       )''')

    def crear_tabla_codigos_descuentos():
       cursor.execute('''CREATE TABLE IF NOT EXISTS codigos_descuentos (
           codigo TEXT NOT NULL,
           porcentaje REAL NOT NULL,
           PRIMARY KEY(codigo)
       )''')

    def crear_tabla_cotizacion_codigo():
       cursor.execute('''CREATE TABLE IF NOT EXISTS cotizacion_codigo (
           id_pedido TEXT NOT NULL,
           codigo_seleccionado TEXT NOT NULL,
           PRIMARY KEY(id_pedido, codigo_seleccionado),       
           FOREIGN KEY(id_pedido) REFERENCES cotizacion(id_pedido) ON DELETE CASCADE,
           FOREIGN KEY(codigo_seleccionado) REFERENCES codigos_descuentos(codigo)  -- Aquí se cambió "codigo_selecionado" por "codigo"
       )''')
      
    def crear_tabla_bicicleta():
        cursor.execute('''CREATE TABLE IF NOT EXISTS bicicleta (
            id_pedido TEXT NOT NULL,
            precio INTEGER NOT NULL,
            PRIMARY KEY(id_pedido),
            FOREIGN KEY(id_pedido) REFERENCES cotizacion(id_pedido) ON DELETE CASCADE
        )''')
        
    def crear_tabla_transacciones():
        cursor.execute('''CREATE TABLE IF NOT EXISTS transacciones (
            id_pago TEXT NOT NULL,
            monto_pagado INTEGER NOT NULL,
            PRIMARY KEY(id_pago)
        )''')
    
    def crear_tabla_boleta():
        cursor.execute('''CREATE TABLE IF NOT EXISTS boleta (
            id_pedido TEXT NOT NULL,
            precio_final INTEGER NOT NULL,
            id_pago INTEGER NOT NULL,
            PRIMARY KEY(id_pedido),
            FOREIGN KEY(id_pedido) REFERENCES bicicleta(id_pedido) ON DELETE CASCADE,
            FOREIGN KEY(precio_final) REFERENCES bicicleta(precio),
            FOREIGN KEY(id_pago) REFERENCES transacciones(id_pago)
        )''')
    
    def crear_tabla_historico_pedidos():
        cursor.execute('''CREATE TABLE IF NOT EXISTS historico_pedidos (
            id_pedido TEXT NOT NULL,
            fecha_entrega_pedido TEXT NOT NULL,
            PRIMARY KEY(id_pedido),
            FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido)
        )''')
    
    def crear_tabla_garantia():
        cursor.execute('''CREATE TABLE IF NOT EXISTS garantia (
            id_pedido TEXT NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_fin TEXT NOT NULL,
            cobertura TEXT NOT NULL,
            condiciones TEXT NOT NULL,
            estado BLOB NOT NULL,
            PRIMARY KEY(id_pedido),
            FOREIGN KEY(id_pedido) REFERENCES historico_pedidos(id_pedido) ON DELETE CASCADE
        )''')
    

    crear_tabla_personas()
    crear_tabla_clientes()
    crear_tabla_tecnicos()

    crear_tabla_tecnico_pedido()

    crear_tabla_pedido()

    crear_tabla_almacen()
    crear_tabla_componentes()

    crear_tabla_codigos_descuentos()
    crear_tabla_cotizacion_codigo()

    crear_tabla_cotizacion()

    crear_tabla_bicicleta()

    crear_tabla_transacciones()
    crear_tabla_boleta()

    crear_tabla_historico_pedidos()
    crear_tabla_garantia()
    
    conn.commit()
    conn.close()

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
            ('01234567-8', 'Valeria', 'Torres', 01234567, 'valeria.torres@example.com', 'Calle 753'),
            ('12345678-0', 'Javier', 'Ramirez', 12345678, 'javier.ramirez@example.com', 'Avenida 951'),
            ('23456789-1', 'Elena', 'Fernandez', 23456789, 'elena.fernandez@example.com', 'Plaza 147'),
            ('34567890-2', 'Miguel', 'Gutierrez', 34567890, 'miguel.gutierrez@example.com', 'Calle 258'),
            ('45678901-3', 'Carmen', 'Jimenez', 45678901, 'carmen.jimenez@example.com', 'Avenida 369'),
            ('56789012-4', 'Ricardo', 'Perez', 56789012, 'ricardo.perez@example.com', 'Plaza 753'),
            ('67890123-5', 'Isabel', 'Lopez', 67890123, 'isabel.lopez@example.com', 'Calle 147'),
            ('78901234-6', 'Alejandro', 'Gonzalez', 78901234, 'alejandro.gonzalez@example.com', 'Avenida 258'),
            ('89012345-7', 'Camila', 'Martinez', 89012345, 'camila.martinez@example.com', 'Plaza 369'),
            ('90123456-8', 'Andres', 'Sanchez', 90123456, 'andres.sanchez@example.com', 'Calle 753'),
            ('01234567-9', 'Lucia', 'Hernandez', 01234567, 'lucia.hernandez@example.com', 'Avenida 951')
        ''')

    def insert_tecnicos():
        cursor.execute('''INSERT INTO tecnicos (rut_id, especialidad)
            VALUES
            ('12345678-9', 'Mecánica'),
            ('23456789-0', 'Electrónica'),
            ('34567890-1', 'Diseño'),
            ('45678901-2', 'Mecánica'),
            ('56789012-3', 'Electrónica'),
            ('67890123-4', 'Diseño'),
            ('78901234-5', 'Mecánica'),
            ('89012345-6', 'Electrónica'),
            ('90123456-7', 'Diseño'),
            ('01234567-8', 'Mecánica')
        ''')

    def insert_clientes():
        cursor.execute('''INSERT INTO clientes (rut_id, altura)
            VALUES
            ('12345678-0', 170),
            ('23456789-1', 165),
            ('34567890-2', 180),
            ('45678901-3', 175),
            ('56789012-4', 160),
            ('67890123-5', 185),
            ('78901234-6', 175),
            ('89012345-7', 165),
            ('90123456-8', 170),
            ('01234567-9', 180)
        ''')

    def insert_almacen():
        cursor.execute('''INSERT INTO almacen (sku, nombre, categoria, tipo, descuento_individual, stock, precio)
        VALUES
            ('SKU_R001', 'Marco Ruta Carbono', 'Ruta', 'Marco', 10, 20, 1500),
            ('SKU_R002', 'Marco Ruta Aluminio', 'Ruta', 'Marco', 5, 15, 1200),
            ('SKU_R003', 'Marco Ruta Titanio', 'Ruta', 'Marco', 0, 5, 2000),
            ('SKU_R004', 'Transmisión Ruta Shimano', 'Ruta', 'Transmisión', 1, 10, 1800),
            ('SKU_R005', 'Transmisión Ruta SRAM', 'Ruta', 'Transmisión', 0, 25, 1600),
            ('SKU_R006', 'Transmisión Ruta Campagnolo', 'Ruta', 'Transmisión', 0, 20, 2200),
            ('SKU_R007', 'Frenos Ruta Hidráulicos', 'Ruta', 'Frenos', 5, 20, 250),
            ('SKU_R008', 'Frenos Ruta Mecánicos', 'Ruta', 'Frenos', 0, 30, 180),
            ('SKU_R009', 'Frenos Ruta Disco', 'Ruta', 'Frenos', 10, 15, 300),
            ('SKU_R010', 'Ruedas Ruta Aero', 'Ruta', 'Ruedas', 0, 25, 1200),
            ('SKU_R011', 'Ruedas Ruta Ligeras', 'Ruta', 'Ruedas', 5, 20, 1300),
            ('SKU_R012', 'Ruedas Ruta Montaña', 'Ruta', 'Ruedas', 0, 10, 1000),
            ('SKU_R013', 'Neumáticos Ruta Competición', 'Ruta', 'Neumáticos', 0, 15, 800),
            ('SKU_R014', 'Neumáticos Ruta Resistencia', 'Ruta', 'Neumáticos', 5, 20, 700),
            ('SKU_R015', 'Neumáticos Ruta All-Terrain', 'Ruta', 'Neumáticos', 10, 30, 850),
            ('SKU_R016', 'Tija Ruta Carbono', 'Ruta', 'Tija', 0, 10, 400),
            ('SKU_R017', 'Tija Ruta Aluminio', 'Ruta', 'Tija', 5, 25, 300),
            ('SKU_R018', 'Tija Ruta Aero', 'Ruta', 'Tija', 0, 15, 500),
            ('SKU_R019', 'Manillar Ruta Drop', 'Ruta', 'Manillar', 5, 20, 150),
            ('SKU_R020', 'Manillar Ruta Compact', 'Ruta', 'Manillar', 0, 15, 100),
            ('SKU_R021', 'Manillar Ruta Aero', 'Ruta', 'Manillar', 10, 10, 180),
            ('SKU_R022', 'Pedales Ruta Clip', 'Ruta', 'Pedales', 0, 40, 120),
            ('SKU_R023', 'Pedales Ruta Plataforma', 'Ruta', 'Pedales', 5, 35, 110),
            ('SKU_R024', 'Pedales Ruta Mixtos', 'Ruta', 'Pedales', 0, 20, 130),
            ('SKU_R025', 'Sillín Ruta Ligero', 'Ruta', 'Sillín', 0, 20, 200),
            ('SKU_R026', 'Sillín Ruta Aero', 'Ruta', 'Sillín', 10, 10, 250),
            ('SKU_R027', 'Sillín Ruta Gel', 'Ruta', 'Sillín', 5, 15, 220),
            ('SKU_M001', 'Marco MTB Aluminio', 'MTB', 'Marco', 0, 30, 1000),
            ('SKU_M002', 'Marco MTB Carbono', 'MTB', 'Marco', 10, 15, 1200),
            ('SKU_M003', 'Marco MTB Acero', 'MTB', 'Marco', 5, 25, 900),
            ('SKU_M004', 'Transmisión MTB Shimano', 'MTB', 'Transmisión', 0, 4, 1800),
            ('SKU_M005', 'Transmisión MTB SRAM', 'MTB', 'Transmisión', 10, 20, 1600),
            ('SKU_M006', 'Transmisión MTB MicroSHIFT', 'MTB', 'Transmisión', 5, 10, 1400),
            ('SKU_M007', 'Frenos MTB Disco Hidráulicos', 'MTB', 'Frenos', 10, 30, 400),
            ('SKU_M008', 'Frenos MTB Disco Mecánicos', 'MTB', 'Frenos', 5, 25, 350),
            ('SKU_M009', 'Frenos MTB V-Brake', 'MTB', 'Frenos', 0, 50, 250),
            ('SKU_M010', 'Ruedas MTB 29 pulgadas', 'MTB', 'Ruedas', 5, 25, 1200),
            ('SKU_M011', 'Ruedas MTB 27.5 pulgadas', 'MTB', 'Ruedas', 0, 20, 1300),
            ('SKU_M012', 'Ruedas MTB Tubeless', 'MTB', 'Ruedas', 10, 15, 1500),
            ('SKU_M013', 'Neumáticos MTB Competición', 'MTB', 'Neumáticos', 0, 20, 800),
            ('SKU_M014', 'Neumáticos MTB All-Mountain', 'MTB', 'Neumáticos', 10, 30, 750),
            ('SKU_M015', 'Neumáticos MTB Downhill', 'MTB', 'Neumáticos', 10, 25, 850),
            ('SKU_M016', 'Tija MTB Aluminio', 'MTB', 'Tija', 0, 20, 300),
            ('SKU_M017', 'Tija MTB Carbono', 'MTB', 'Tija', 10, 15, 500),
            ('SKU_M018', 'Tija MTB Dropper', 'MTB', 'Tija', 5, 10, 400),
            ('SKU_M019', 'Manillar MTB Riser', 'MTB', 'Manillar', 0, 20, 180),
            ('SKU_M020', 'Manillar MTB Flat', 'MTB', 'Manillar', 5, 25, 150),
            ('SKU_M021', 'Manillar MTB DH', 'MTB', 'Manillar', 10, 10, 200),
            ('SKU_M022', 'Pedales MTB Plataforma', 'MTB', 'Pedales', 0, 30, 120),
            ('SKU_M023', 'Pedales MTB Clipless', 'MTB', 'Pedales', 10, 15, 100),
            ('SKU_M024', 'Pedales MTB Mixtos', 'MTB', 'Pedales', 5, 20, 130),
            ('SKU_M025', 'Sillín MTB Enduro', 'MTB', 'Sillín', 0, 15, 220),
            ('SKU_M026', 'Sillín MTB Gel', 'MTB', 'Sillín', 5, 20, 250),
            ('SKU_M027', 'Sillín MTB Ligero', 'MTB', 'Sillín', 0, 25, 230),
            ('SKU_U001', 'Marco Urbano Aluminio', 'Urbano', 'Marco', 5, 30, 900),
            ('SKU_U002', 'Marco Urbano Acero', 'Urbano', 'Marco', 0, 20, 850),
            ('SKU_U003', 'Marco Urbano Carbono', 'Urbano', 'Marco', 10, 10, 1200),
            ('SKU_U004', 'Transmisión Urbano Shimano', 'Urbano', 'Transmisión', 0, 25, 1800),
            ('SKU_U005', 'Transmisión Urbano Nexus', 'Urbano', 'Transmisión', 5, 15, 1700),
            ('SKU_U006', 'Transmisión Urbano SRAM', 'Urbano', 'Transmisión', 10, 20, 1900),
            ('SKU_U007', 'Frenos Urbano Disco', 'Urbano', 'Frenos', 5, 20, 300),
            ('SKU_U008', 'Frenos Urbano V-Brake', 'Urbano', 'Frenos', 0, 40, 150),
            ('SKU_U009', 'Frenos Urbano Hidráulicos', 'Urbano', 'Frenos', 10, 30, 350),
            ('SKU_U010', 'Ruedas Urbano Ligeras', 'Urbano', 'Ruedas', 5, 25, 1200),
            ('SKU_U011', 'Ruedas Urbano Aero', 'Urbano', 'Ruedas', 0, 20, 1300),
            ('SKU_U012', 'Ruedas Urbano Resistencia', 'Urbano', 'Ruedas', 10, 15, 1100),
            ('SKU_U013', 'Neumáticos Urbano Antipinchazos', 'Urbano', 'Neumáticos', 0, 25, 700),
            ('SKU_U014', 'Neumáticos Urbano All-Terrain', 'Urbano', 'Neumáticos', 5, 20, 650),
            ('SKU_U015', 'Neumáticos Urbano Plegables', 'Urbano', 'Neumáticos', 10, 20, 600),
            ('SKU_U016', 'Tija Urbano Aluminio', 'Urbano', 'Tija', 0, 20, 250),
            ('SKU_U017', 'Tija Urbano Carbono', 'Urbano', 'Tija', 5, 15, 400),
            ('SKU_U018', 'Tija Urbano Ajustable', 'Urbano', 'Tija', 10, 10, 450),
            ('SKU_U019', 'Manillar Urbano Recto', 'Urbano', 'Manillar', 0, 20, 180),
            ('SKU_U020', 'Manillar Urbano Drop', 'Urbano', 'Manillar', 5, 25, 200),
            ('SKU_U021', 'Manillar Urbano Ajustable', 'Urbano', 'Manillar', 10, 10, 150),
            ('SKU_U022', 'Pedales Urbano Plataforma', 'Urbano', 'Pedales', 0, 30, 120),
            ('SKU_U023', 'Pedales Urbano Clipless', 'Urbano', 'Pedales', 5, 20, 100),
            ('SKU_U024', 'Pedales Urbano Mixtos', 'Urbano', 'Pedales', 0, 25, 130),
            ('SKU_U025', 'Sillín Urbano Cómodo', 'Urbano', 'Sillín', 5, 20, 180),
            ('SKU_U026', 'Sillín Urbano Plegable', 'Urbano', 'Sillín', 0, 30, 200),
            ('SKU_U027', 'Sillín Urbano Deportivo', 'Urbano', 'Sillín', 10, 10, 250)
    ''')

    def insert_codigos_descuentos():
        cursor.execute('''INSERT INTO codigos_descuentos (codigo, porcentaje)
            VALUES
            ('DESCUENTO10',0.10),
            ('DESCUENTO20',0.20),
            ('BLACKFRIDAY',0.25),
            ('NAVIDAD',0.20),
            ('CYBERDAY',0.15),
            ('CYBERMONDAY',0.10)
        ''')

    insert_personas()
    insert_tecnicos()
    insert_clientes()
    insert_almacen()
    insert_codigos_descuentos()

    conn.commit()
    conn.close()

crear_db()
inserts()