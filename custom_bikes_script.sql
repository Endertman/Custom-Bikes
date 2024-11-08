-- CREATE TABLE IF NOT EXISTS `garantia` (
-- 	`id_pedido` TEXT NOT NULL UNIQUE,
-- 	`fecha_inicio` REAL NOT NULL,
-- 	`fecha_fin` REAL NOT NULL,
-- 	`cobertura` TEXT NOT NULL,
-- 	`condiciones` TEXT NOT NULL,
-- 	`estado` REAL NOT NULL,
-- 	FOREIGN KEY(`id_pedido`) REFERENCES `historico_pedidos`(`id_pedido`)
-- );

-- CREATE TABLE IF NOT EXISTS `tecnico` (
-- 	`rut_id` TEXT NOT NULL,
-- 	`especialidad` TEXT NOT NULL,
-- 	FOREIGN KEY(`rut_id`) REFERENCES `personas`(`rut_id`)
-- );

-- CREATE TABLE IF NOT EXISTS `cliente` (
-- 	`rut_id` TEXT NOT NULL UNIQUE,
-- 	`altura` INTEGER NOT NULL,
-- 	FOREIGN KEY(`rut_id`) REFERENCES `personas`(`rut_id`)
-- );

-- CREATE TABLE IF NOT EXISTS `pedido` (
-- 	`id_pedido` INTEGER PRIMARY KEY NOT NULL UNIQUE,
-- 	`fecha_inicio_pedido` REAL NOT NULL,
-- 	`tecnicos` TEXT NOT NULL,
-- 	`cliente` TEXT NOT NULL,
-- 	`fecha_entrega_pedido` REAL NOT NULL,
-- 	FOREIGN KEY(`tecnicos`) REFERENCES `tecnico_pedido`(`id_tecnico`),
-- 	FOREIGN KEY(`cliente`) REFERENCES `cliente`(`rut_id`)
-- );

-- CREATE TABLE IF NOT EXISTS `bicicleta` (
-- 	`id_pedido` INTEGER NOT NULL,
-- 	`precio` INTEGER NOT NULL,
-- 	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`),
-- 	FOREIGN KEY(`precio`) REFERENCES `cotizacion`(`calculo_precio`)
-- );

-- CREATE TABLE IF NOT EXISTS `cotizacion` (
-- 	`id_pedido` INTEGER NOT NULL,
-- 	`calculo_precio` INTEGER NOT NULL,
-- 	`id_lista_componentes` INTEGER NOT NULL,
-- 	`codigo_descuento` INTEGER NOT NULL,
-- 	FOREIGN KEY(`id_pedido`) REFERENCES `bicicleta`(`id_pedido`),
-- 	FOREIGN KEY(`id_lista_componentes`) REFERENCES `componentes`(`id_lista_componentes`),
-- 	FOREIGN KEY(`codigo_descuento`) REFERENCES `cotizacion_codigo`(`codigo_seleccionado`)
-- );

-- CREATE TABLE IF NOT EXISTS `codigos_descuento` (
-- 	`codigo_descuento` TEXT NOT NULL UNIQUE,
-- 	`porcentaje` REAL NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS `componentes` (
-- 	`id_lista_componentes` INTEGER PRIMARY KEY NOT NULL UNIQUE,
-- 	`marco_sku` TEXT NOT NULL,
-- 	`transmision_sku` TEXT NOT NULL,
-- 	`frenos_sku` TEXT NOT NULL,
-- 	`ruedas_sku` TEXT NOT NULL,
-- 	`neumaticos_sku` TEXT NOT NULL,
-- 	`tija_sku` TEXT NOT NULL,
-- 	`manillar_sku` TEXT NOT NULL,
-- 	`pedales_sku` TEXT NOT NULL,
-- 	`sillin_sku` TEXT NOT NULL,
-- 	FOREIGN KEY(`marco_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`transmision_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`frenos_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`ruedas_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`neumaticos_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`tija_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`manillar_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`pedales_sku`) REFERENCES `almacen`(`sku`),
-- 	FOREIGN KEY(`sillin_sku`) REFERENCES `almacen`(`sku`)
-- );

-- CREATE TABLE IF NOT EXISTS `almacen` (
-- 	`sku` INTEGER PRIMARY KEY NOT NULL UNIQUE,
-- 	`nombre` TEXT NOT NULL,
-- 	`categoria` TEXT NOT NULL,
-- 	`tipo` TEXT NOT NULL,
-- 	`descuento_individual` INTEGER NOT NULL DEFAULT '0',
-- 	`stock` INTEGER NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS `boleta` (
-- 	`id_pedido` INTEGER NOT NULL UNIQUE,
-- 	`precio_final` INTEGER NOT NULL,
-- 	`id_pago` INTEGER NOT NULL,
-- 	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`),
-- 	FOREIGN KEY(`precio_final`) REFERENCES `bicicleta`(`precio`),
-- 	FOREIGN KEY(`id_pago`) REFERENCES `transacciones`(`id_pago`)
-- );

-- CREATE TABLE IF NOT EXISTS `transacciones` (
-- 	`id_pago` INTEGER PRIMARY KEY NOT NULL UNIQUE,
-- 	`monto_pagado` INTEGER NOT NULL DEFAULT '0'
-- );

-- CREATE TABLE IF NOT EXISTS `historico_pedidos` (
-- 	`id_pedido` INTEGER NOT NULL,
-- 	`fecha_entrega_pedido` REAL NOT NULL,
-- 	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`)
-- );

-- CREATE TABLE IF NOT EXISTS `tecnico_pedido` (
-- 	`id_pedido` INTEGER NOT NULL,
-- 	`id_tecnico` INTEGER NOT NULL,
-- 	FOREIGN KEY(`id_pedido`) REFERENCES `pedido`(`id_pedido`),
-- 	FOREIGN KEY(`id_tecnico`) REFERENCES `tecnico`(`rut_id`)
-- );

-- CREATE TABLE IF NOT EXISTS `cotizacion_codigo` (
-- 	`codigo_seleccionado` TEXT NOT NULL UNIQUE,
-- 	FOREIGN KEY(`codigo_seleccionado`) REFERENCES `codigos_descuento`(`codigo_descuento`)
-- );

-- CREATE TABLE IF NOT EXISTS `personas` (
-- 	`rut_id` TEXT NOT NULL UNIQUE,
-- 	`numero_de_telefono` TEXT NOT NULL,
-- 	`direccion` TEXT NOT NULL
-- );
