import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('custom_bikes.db')
cursor = conexion.cursor()

def borrar_db():
    cursor.execute('''DROP DATABASE custom_bikes''')
    
def crear_db():
    cursor.execute('''CREATE DATABASE custom_bikes''')

def crear_tabla_personas():
    cursor.execute('''CREATE TABLE IF NOT EXISTS personas (
    	`rut_id` TEXT NOT NULL UNIQUE,
	    `nombre` TEXT NOT NULL,
	    `apellido` TEXT NOT NULL,
	    `telefono` INTEGER NOT NULL,
	    `correo` TEXT NOT NULL,
	    `direccion` TEXT NOT NULL,
	    PRIMARY KEY(`rut_id`)
    )''')

def crear_tabla_cliente():
    cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
    	`rut_id` TEXT NOT NULL UNIQUE,
	    `altura` INTEGER NOT NULL,
	    FOREIGN KEY(`rut_id`) REFERENCES `personas`(`rut_id`)
    )''')

def crear_tabla_tecnico():
    cursor.execute('''CREATE TABLE IF NOT EXISTS tecnico (
    	`rut_id` TEXT NOT NULL UNIQUE,
	    `especialidad` TEXT NOT NULL,
	    FOREIGN KEY(`rut_id`) REFERENCES `personas`(`rut_id`)
    )''')
 
crear_db()


# funciones para agregar personas
def personas(rut_id, nombre, apellido, telefono, correo, direccion):
    cursor.execute('''INSERT INTO personas (rut_id, nombre, apellido, telefono, correo, direccion) VALUES (?, ?, ?, ?, ?, ?)''', (rut_id, nombre, apellido, telefono, correo, direccion))
    conexion.commit()
    print("Persona agregada exitosamente.")















































































def transacciones():
    cursor.execute('''CREATE TABLE IF NOT EXIST transacciones
                   `id_pago` INTEGER PRIMARY KEY NOT NULL UNIQUE,
					`monto_pagado` INTEGER NOT NULL DEFAULT '0'))''')
    
def tecnico_pedido():
    cursor.execute('''CREATE TABLE IF NOT EXIST tecnico_pedido (
                  `id_pedido` INTEGER NOT NULL,
				  `id_tecnico` INTEGER NOT NULL,
				  FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`),
				  FOREIGN KEY(`id_tecnico`) REFERENCES `tecnico`(`rut_id`))
                   ''')
    
def historico_pedidos():
    cursor.execute('''CREATE TABLE IF NOT EXIST historico_pedidos (
                	`id_pedido` INTEGER NOT NULL,
					`fecha_entrega_pedido` REAL NOT NULL,
					FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`))
                   ''')

def pedido():
    cursor.execute('''CREATE TABLE IF NOT EXIST pedido(
                	`id_pedido` INTEGER PRIMARY KEY NOT NULL UNIQUE,
					`fecha_inicio_pedido` REAL NOT NULL,
					`tecnicos` TEXT NOT NULL,
					`cliente` TEXT NOT NULL,
					`fecha_entrega_pedido` REAL NOT NULL,
					FOREIGN KEY(`tecnicos`) REFERENCES `tecnico_pedido`(`id_tecnico`),
					FOREIGN KEY(`cliente`) REFERENCES `cliente`(`rut_id`)
                   )''')
    
def lista_componentes():
    cursor.execute('''CREATE TABLE IF NOT EXIST componentes (
                   `id_lista_componentes` INTEGER PRIMARY KEY NOT NULL UNIQUE,
					`marco_sku` TEXT NOT NULL,
					`transmision_sku` TEXT NOT NULL,
					`frenos_sku` TEXT NOT NULL,
					`ruedas_sku` TEXT NOT NULL,
					`neumaticos_sku` TEXT NOT NULL,
					`tija_sku` TEXT NOT NULL,
					`manillar_sku` TEXT NOT NULL,
					`pedales_sku` TEXT NOT NULL,
					`sillin_sku` TEXT NOT NULL,
					FOREIGN KEY(`marco_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`transmision_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`frenos_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`ruedas_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`neumaticos_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`tija_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`manillar_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`pedales_sku`) REFERENCES `almacen`(`sku`),
					FOREIGN KEY(`sillin_sku`) REFERENCES `almacen`(`sku`)
				)''')