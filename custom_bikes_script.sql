CREATE TABLE IF NOT EXISTS `garantia` (
	`id_pedido` TEXT NOT NULL UNIQUE,
	`fecha_inicio` REAL NOT NULL,
	`fecha_fin` REAL NOT NULL,
	`cobertura` TEXT NOT NULL,
	`condiciones` TEXT NOT NULL,
	`estado` REAL NOT NULL,
	FOREIGN KEY(`id_pedido`) REFERENCES `historico_pedidos`(`id_pedido`)
);

CREATE TABLE IF NOT EXISTS `tecnico` (
	`rut_id` TEXT NOT NULL,
	`especialidad` TEXT NOT NULL,
	FOREIGN KEY(`rut_id`) REFERENCES `personas`(`rut_id`)
);

CREATE TABLE IF NOT EXISTS `cliente` (
	`rut_id` TEXT NOT NULL UNIQUE,
	`altura` INTEGER NOT NULL,
	FOREIGN KEY(`rut_id`) REFERENCES `personas`(`rut_id`)
);

CREATE TABLE IF NOT EXISTS `pedido` (
	`id_pedido` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`fecha_inicio_pedido` REAL NOT NULL,
	`tecnicos` TEXT NOT NULL,
	`cliente` TEXT NOT NULL,
	`fecha_entrega_pedido` REAL NOT NULL,
	FOREIGN KEY(`tecnicos`) REFERENCES `tecnico_pedido`(`id_tecnico`),
	FOREIGN KEY(`cliente`) REFERENCES `cliente`(`rut_id`)
);

CREATE TABLE IF NOT EXISTS `bicicleta` (
	`id_pedido` INTEGER NOT NULL,
	`precio` INTEGER NOT NULL,
	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`),
	FOREIGN KEY(`precio`) REFERENCES `cotizacion`(`calculo_precio`)
);

CREATE TABLE IF NOT EXISTS `cotizacion` (
	`id_pedido` INTEGER NOT NULL,
	`calculo_precio` INTEGER NOT NULL,
	`id_lista_componentes` INTEGER NOT NULL,
	`codigo_descuento` INTEGER NOT NULL,
	FOREIGN KEY(`id_pedido`) REFERENCES `bicicleta`(`id_pedido`),
	FOREIGN KEY(`id_lista_componentes`) REFERENCES `componentes`(`id_lista_componentes`),
	FOREIGN KEY(`codigo_descuento`) REFERENCES `cotizacion_codigo`(`codigo_seleccionado`)
);

CREATE TABLE IF NOT EXISTS `codigos_descuento` (
	`codigo_descuento` TEXT NOT NULL UNIQUE,
	`porcentaje` REAL NOT NULL
);

INSERT INTO codigo_descuento VALUES (codigo_descuento,porcentaje)
('DESCUENTO10',10)
('DESCUENTO20',20)
('BLACKFRIDAY',30)
('NAVIDAD',20)
('CYBERDAY',15)
('CYBERMONY',10);

CREATE TABLE IF NOT EXISTS `componentes` (
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
);

CREATE TABLE IF NOT EXISTS `almacen` (
	`sku` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`categoria` TEXT NOT NULL,
	`tipo` TEXT NOT NULL,
	`descuento_individual` INTEGER NOT NULL DEFAULT '0',
	`stock` INTEGER NOT NULL
);

INSERT INTO almacen VALUES (sku,nombre,categoria,tipo,descuento_individual,stock,precio)
('SKU_R001','Marco Ruta Carbono','Ruta','Marco',10,20,100)
('SKU_R002','Marco Ruta Aluminio','Ruta','Marco',5,15,100)
('SKU_R003','Marco Ruta Titanio','Ruta','Marco',0,5,100)
('SKU_R004','Transmisión Ruta Shimano','Ruta','Transmisión',15,30,100)
('SKU_R005','Transmisión Ruta SRAM','Ruta','Transmisión',0,25,100)
('SKU_R006','Transmisión Ruta Campagnolo','Ruta','Transmisión',10,10,100)
('SKU_R007','Frenos Ruta Hidráulicos','Ruta','Frenos',5,20,100)
('SKU_R008','Frenos Ruta Mecánicos','Ruta','Frenos',0,30,100)
('SKU_R009','Frenos Ruta Disco','Ruta','Frenos',10,15,100)
('SKU_R010','Ruedas Ruta Aero','Ruta','Ruedas',0,25,100)
('SKU_R011','Ruedas Ruta Ligeras','Ruta','Ruedas',5,20,100)
('SKU_R012','Ruedas Ruta Montaña','Ruta','Ruedas',0,10,100)
('SKU_R013','Neumáticos Ruta Competición','Ruta','Neumáticos',0,50,100)
('SKU_R014','Neumáticos Ruta Resistencia','Ruta','Neumáticos',5,40,100)
('SKU_R015','Neumáticos Ruta All-Terrain','Ruta','Neumáticos',0,30,100)
('SKU_R016','Tija Ruta Carbono','Ruta','Tija',0,10,100)
('SKU_R017','Tija Ruta Aluminio','Ruta','Tija',5,25,100)
('SKU_R018','Tija Ruta Aero','Ruta','Tija',0,15,100)
('SKU_R019','Manillar Ruta Drop','Ruta','Manillar',5,20,100)
('SKU_R020','Manillar Ruta Compact','Ruta','Manillar',0,15,100)
('SKU_R021','Manillar Ruta Aero','Ruta','Manillar',10,10,100)
('SKU_R022','Pedales Ruta Clip','Ruta','Pedales',0,40,100)
('SKU_R023','Pedales Ruta Plataforma','Ruta','Pedales',5,35,100)
('SKU_R024','Pedales Ruta Mixtos','Ruta','Pedales',0,20,100)
('SKU_R025','Sillín Ruta Ligero','Ruta','Sillín',0,20,100)
('SKU_R026','Sillín Ruta Aero','Ruta','Sillín',10,10,100)
('SKU_R027','Sillín Ruta Gel','Ruta','Sillín',5,15,100)
('SKU_M001','Marco MTB Aluminio','MTB','Marco',0,30,100)
('SKU_M002','Marco MTB Carbono','MTB','Marco',10,15,100)
('SKU_M003','Marco MTB Acero','MTB','Marco',5,25,100)
('SKU_M004','Transmisión MTB Shimano','MTB','Transmisión',0,40,100)
('SKU_M005','Transmisión MTB SRAM','MTB','Transmisión',10,20,100)
('SKU_M006','Transmisión MTB MicroSHIFT','MTB','Transmisión',5,15,100)
('SKU_M007','Frenos MTB Disco Hidráulicos','MTB','Frenos',10,30,100)
('SKU_M008','Frenos MTB Disco Mecánicos','MTB','Frenos',5,25,100)
('SKU_M009','Frenos MTB V-Brake','MTB','Frenos',0,50,100)
('SKU_M010','Ruedas MTB 29 pulgadas','MTB','Ruedas',5,25,100)
('SKU_M011','Ruedas MTB 27.5 pulgadas','MTB','Ruedas',0,20,100)
('SKU_M012','Ruedas MTB Tubeless','MTB','Ruedas',10,15,100)
('SKU_M013','Neumáticos MTB Competición','MTB','Neumáticos',0,50,100)
('SKU_M014','Neumáticos MTB All-Mountain','MTB','Neumáticos',5,40,100)
('SKU_M015','Neumáticos MTB Downhill','MTB','Neumáticos',10,25,100)
('SKU_M016','Tija MTB Aluminio','MTB','Tija',0,20,100)
('SKU_M017','Tija MTB Carbono','MTB','Tija',10,15,100)
('SKU_M018','Tija MTB Dropper','MTB','Tija',5,10,100)
('SKU_M019','Manillar MTB Riser','MTB','Manillar',0,20,100)
('SKU_M020','Manillar MTB Flat','MTB','Manillar',5,25,100)
('SKU_M021','Manillar MTB DH','MTB','Manillar',10,10,100)
('SKU_M022','Pedales MTB Plataforma','MTB','Pedales',0,30,100)
('SKU_M023','Pedales MTB Clipless','MTB','Pedales',10,15,100)
('SKU_M024','Pedales MTB Mixtos','MTB','Pedales',5,20,100)
('SKU_M025','Sillín MTB Enduro','MTB','Sillín',0,15,100)
('SKU_M026','Sillín MTB Gel','MTB','Sillín',5,20,100)
('SKU_M027','Sillín MTB Ligero','MTB','Sillín',0,25,100)
('SKU_U001','Marco Urbano Aluminio','Urbano','Marco',5,30,100)
('SKU_U002','Marco Urbano Acero','Urbano','Marco',0,20,100)
('SKU_U003','Marco Urbano Carbono','Urbano','Marco',10,10,100)
('SKU_U004','Transmisión Urbano Shimano','Urbano','Transmisión',5,35,100)
('SKU_U005','Transmisión Urbano Nexus','Urbano','Transmisión',0,25,100)
('SKU_U006','Transmisión Urbano SRAM','Urbano','Transmisión',10,15,100)
('SKU_U007','Frenos Urbano Disco','Urbano','Frenos',5,20,100)
('SKU_U008','Frenos Urbano V-Brake','Urbano','Frenos',0,40,100)
('SKU_U009','Frenos Urbano Hidráulicos','Urbano','Frenos',10,15,100)
('SKU_U010','Ruedas Urbano Ligeras','Urbano','Ruedas',5,25,100)
('SKU_U011','Ruedas Urbano Aero','Urbano','Ruedas',0,20,100)
('SKU_U012','Ruedas Urbano Resistencia','Urbano','Ruedas',10,10,100)
('SKU_U013','Neumáticos Urbano Antipinchazos','Urbano','Neumáticos',0,50,100)
('SKU_U014','Neumáticos Urbano All-Terrain','Urbano','Neumáticos',5,35,100)
('SKU_U015','Neumáticos Urbano Plegables','Urbano','Neumáticos',10,25,100)
('SKU_U016','Tija Urbano Aluminio','Urbano','Tija',0,20,100)
('SKU_U017','Tija Urbano Carbono','Urbano','Tija',5,15,100)
('SKU_U018','Tija Urbano Ajustable','Urbano','Tija',10,10,100)
('SKU_U019','Manillar Urbano Recto','Urbano','Manillar',0,20,100)
('SKU_U020','Manillar Urbano Curvo','Urbano','Manillar',5,25,100)
('SKU_U021','Manillar Urbano Plegable,Urbano,Manillar',10,10,100)
('SKU_U022','Pedales Urbano Plataforma','Urbano','Pedales',5,30,100)
('SKU_U023','Pedales Urbano Clip','Urbano','Pedales',0,20,100)
('SKU_U024','Pedales Urbano Plegables','Urbano','Pedales',10,15,100)
('SKU_U025','Sillín Urbano Confort','Urbano','Sillín',5,20,100)
('SKU_U026','Sillín Urbano Gel','Urbano','Sillín',0,15,100)
('SKU_U027','Sillín Urbano Plegable','Urbano','Sillín',10,10,100);

CREATE TABLE IF NOT EXISTS `boleta` (
	`id_pedido` INTEGER NOT NULL UNIQUE,
	`precio_final` INTEGER NOT NULL,
	`id_pago` INTEGER NOT NULL,
	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`),
	FOREIGN KEY(`precio_final`) REFERENCES `bicicleta`(`precio`),
	FOREIGN KEY(`id_pago`) REFERENCES `transacciones`(`id_pago`)
);

CREATE TABLE IF NOT EXISTS `transacciones` (
	`id_pago` INTEGER PRIMARY KEY NOT NULL UNIQUE,
	`monto_pagado` INTEGER NOT NULL DEFAULT '0'
);

CREATE TABLE IF NOT EXISTS `historico_pedidos` (
	`id_pedido` INTEGER NOT NULL,
	`fecha_entrega_pedido` REAL NOT NULL,
	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`)
);

CREATE TABLE IF NOT EXISTS `tecnico_pedido` (
	`id_pedido` INTEGER NOT NULL,
	`id_tecnico` INTEGER NOT NULL,
	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`),
	FOREIGN KEY(`id_tecnico`) REFERENCES `tecnico`(`rut_id`)
);

CREATE TABLE IF NOT EXISTS `cotizacion_codigo` (
	`codigo_seleccionado` TEXT NOT NULL UNIQUE,
	FOREIGN KEY(`codigo_seleccionado`) REFERENCES `codigos_descuento`(`codigo_descuento`)
);

CREATE TABLE IF NOT EXISTS `personas` (
	`rut_id` TEXT NOT NULL UNIQUE,
	`numero_de_telefono` TEXT NOT NULL,
	`direccion` TEXT NOT NULL
);
