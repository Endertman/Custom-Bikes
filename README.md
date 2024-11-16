# Sistema de Base de Datos para CustomBikes S.A.

## Contexto
CustomBikes S.A. es una empresa dedicada a la comercialización de bicicletas altamente personalizadas. Ofrecemos a nuestros clientes la posibilidad de elegir cada componente de su bicicleta, adaptándonos a sus preferencias y presupuesto. Desde el tipo de marco, ruedas y frenos, hasta detalles como materiales y colores, cada bicicleta es única y fabricada a la medida.

Para gestionar este nivel de personalización, es esencial contar con un sistema de base de datos eficiente que registre y administre pedidos, componentes, descuentos y el ensamblaje de bicicletas bajo las reglas de negocio de la empresa.

Este proyecto propone un sistema de base de datos para:
- Registrar los pedidos.
- Asignar técnicos especializados para el ensamblaje.
- Generar documentos de pago.
- Registrar las garantías de las bicicletas vendidas.
- Proveer herramientas de consulta y análisis para la toma de decisiones estratégicas.

## Objetivo
El sistema busca gestionar eficazmente la personalización de bicicletas, permitiendo a los clientes elegir componentes específicos y aplicar descuentos, cumpliendo con un plazo de entrega máximo de 60 días. Además, el sistema generará documentos de pago detallados y llevará un registro histórico de pedidos, técnicos y garantías.

---

## Funcionalidades
### Reglas Generales
1. **Personalización de componentes:**
   - Cada bicicleta es única, ensamblada con componentes específicos seleccionados por el cliente.
   - Los componentes deben estar registrados como productos independientes en la base de datos.

2. **Gestión de descuentos:**
   - Posibilidad de aplicar descuentos individuales a componentes o globales a través de códigos promocionales.

3. **Plazo de entrega:**
   - Todas las bicicletas deben entregarse en un máximo de **60 días**.

4. **Asignación de técnicos:**
   - Los pedidos se asignan a técnicos especialistas y, en caso necesario, a múltiples técnicos.

5. **Documentos de pago:**
   - Generación automática de facturas y comprobantes que detallen el monto, fechas y estado del pago.

6. **Garantías:**
   - Registro detallado de las garantías de las bicicletas vendidas, incluyendo cobertura y condiciones específicas.

7. **Historial de pedidos:**
   - Seguimiento de pedidos anteriores para análisis de tendencias y consultas futuras.

### Requerimientos Específicos
1. **Consulta de pedidos por cliente y fechas:**
   - Posibilidad de buscar pedidos realizados por un cliente en un rango de fechas.

2. **Componentes más solicitados:**
   - Informes que identifiquen los componentes más demandados.

3. **Bicicletas vendidas y sus garantías:**
   - Listar bicicletas junto con los detalles de sus garantías.

4. **Técnicos y bicicletas ensambladas:**
   - Relación entre técnicos y los pedidos que han ensamblado.

---

## Conceptos Técnicos
1. **Base de datos:**
   - Sistema organizado para almacenar y acceder eficientemente a la información.

2. **Tablas:**
   - Las tablas almacenan la información en filas (registros) y columnas (atributos).

3. **Claves Primarias (PK):**
   - Identificadores únicos que garantizan que cada registro sea único en una tabla.

4. **Claves Foráneas (FK):**
   - Relaciones entre tablas, vinculando datos como pedidos con clientes.

---

## Modelo de Datos
El sistema utiliza un modelo relacional, con las siguientes tablas principales:

- **Personas, Clientes, Técnicos:** Manejan los datos personales y roles de cada individuo.
- **Pedido y Componentes:** Gestionan las solicitudes de los clientes y los elementos seleccionados.
- **Almacén:** Contiene los detalles de los componentes disponibles.
- **Cotización y Descuentos:** Calculan los precios y aplican descuentos a nivel individual o global.
- **Histórico y Garantías:** Registran el estado de las bicicletas ensambladas y su seguimiento postventa.

Un diagrama detallado del esquema de la base de datos se incluye a continuación:

```mermaid
erDiagram
    %% Entidades relacionadas con PERSONAS
    PERSONAS {
        TEXT rut_id PK
        TEXT nombre
        TEXT apellido
        INTEGER telefono
        TEXT correo
        TEXT direccion
    }

    CLIENTES {
        TEXT rut_id PK
        INTEGER altura
    }

    TECNICOS {
        TEXT rut_id PK
        TEXT especialidad
    }

    %% Entidad relacionada con PEDIDO
    PEDIDO {
        TEXT id_pedido PK
        TEXT fecha_inicio_pedido
        TEXT cliente FK
        TEXT fecha_entrega_pedido
    }

    TECNICO_PEDIDO {
        TEXT id_tecnico_pedido PK
        TEXT id_pedido FK
        TEXT id_tecnico FK
    }

    %% Relación de CLIENTES con PEDIDO
    CLIENTES ||--o| PEDIDO : "realiza"

    %% Relación de PERSONAS con CLIENTES y TECNICOS
    PERSONAS ||--o| CLIENTES : "es cliente de"
    PERSONAS ||--o| TECNICOS : "es técnico de"

    %% Entidad COMPONENTES relacionada con PEDIDO y ALMACEN
    COMPONENTES {
        TEXT id_componente PK
        TEXT marco_sku FK
        TEXT transmision_sku FK
        TEXT frenos_sku FK
        TEXT ruedas_sku FK
        TEXT neumaticos_sku FK
        TEXT tija_sku FK
        TEXT manillar_sku FK
        TEXT pedales_sku FK
        TEXT sillin_sku FK
    }

    ALMACEN {
        TEXT sku PK
        TEXT nombre
        TEXT categoria
        TEXT tipo
        INTEGER descuento_individual
        INTEGER stock
        INTEGER precio
    }

    %% Relación de COMPONENTES con ALMACEN
    COMPONENTES ||--o| ALMACEN : "almacenados en"
    PEDIDO ||--o| COMPONENTES : "contiene"

    %% Entidad COTIZACION relacionada con PEDIDO y COTIZACION_CODIGO
    COTIZACION {
        TEXT id_cotizacion PK
        INTEGER calculo_precio
        TEXT id_pedido FK
    }

    COTIZACION_CODIGO {
        TEXT id_cotizacion FK
        TEXT codigo_seleccionado FK
    }

    CODIGOS_DESCUENTOS {
        TEXT codigo PK
        REAL porcentaje
    }

    %% Relación de COTIZACION con PEDIDO y COTIZACION_CODIGO
    PEDIDO ||--o| COTIZACION : "genera"
    COTIZACION ||--o| COTIZACION_CODIGO : "aplica"
    COTIZACION_CODIGO ||--o| CODIGOS_DESCUENTOS : "usa"

    %% Entidad BICICLETA relacionada con COTIZACION
    BICICLETA {
        TEXT id_bicicleta PK
        INTEGER precio
        TEXT id_pedido FK
        TEXT id_componente FK
    }

    %% Relación de BICICLETA con BOLETA
    BICICLETA ||--|{ BOLETA : "detalla"
    COTIZACION ||--|{ BICICLETA : "produce"

    %% Entidad BOLETA relacionada con TRANSACCIONES
    TRANSACCIONES {
        TEXT id_pago PK
        INTEGER monto_pagado
        TEXT id_boleta FK
    }

    BOLETA {
        TEXT id_boleta PK
        INTEGER precio_final
        TEXT id_pedido FK
    }

    %% Relación de BOLETA con TRANSACCIONES
    BOLETA ||--o| TRANSACCIONES : "concreta"

    %% Entidad HISTORICO_PEDIDOS relacionada con PEDIDO y GARANTIA
    HISTORICO_PEDIDOS {
        TEXT id_historico PK
        TEXT id_pedido FK
        TEXT fecha_entrega_pedido
    }

    GARANTIA {
        TEXT id_garantia PK
        TEXT id_pedido FK
        TEXT fecha_inicio
        TEXT fecha_fin
        TEXT cobertura
        TEXT condiciones
        BLOB estado
    }

    %% Relación de HISTORICO_PEDIDOS con PEDIDO y GARANTIA
    PEDIDO ||--|{ HISTORICO_PEDIDOS : "es parte de"
    HISTORICO_PEDIDOS ||--|{ GARANTIA : "tiene"

    %% Relación de TECNICO_PEDIDO con PEDIDO y TECNICOS
    TECNICO_PEDIDO ||--o| PEDIDO : "apoya"
    TECNICO_PEDIDO ||--o| TECNICOS : "es asignado a"
