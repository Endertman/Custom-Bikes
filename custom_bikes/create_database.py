import sqlite3

def crear_db():
    conn = sqlite3.connect('custom_bikes/custom_bikes.db')
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
            "id_pedido" TEXT NOT NULL,
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

crear_db()
