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
 


# funciones para agregar personas
def personas(rut_id, nombre, apellido, telefono, correo, direccion):
    cursor.execute('''INSERT INTO personas (rut_id, nombre, apellido, telefono, correo, direccion) VALUES (?, ?, ?, ?, ?, ?)''', (rut_id, nombre, apellido, telefono, correo, direccion))
    conexion.commit()
    print("Persona agregada exitosamente.")
    
# Aqui vamos a ejecutar todo el programa
cursor.execute("DROP DATABASE")

# el angel es weko





#hola angel


























#Endert chupalo