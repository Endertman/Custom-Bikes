# Proyecto de Bases de Datos
### Modelo de Base de Datos Relacional
#### Diseño General del Modelo
Puedes ver el diseño general del modelo de base de datos https://dbdesigner.page.link/7JCT5yN8vZBhcQJr5

## Esquema de la Base de Datos

```mermaid
erDiagram
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
    TECNICO_PEDIDO {
        TEXT id_pedido PK
        TEXT id_tecnico PK
    }
    PEDIDO {
        TEXT id_pedido PK
        TEXT fecha_inicio_pedido
        TEXT cliente
        TEXT fecha_entrega_pedido
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
    COMPONENTES {
        TEXT id_pedido PK
        TEXT marco_sku
        TEXT transmision_sku
        TEXT frenos_sku
        TEXT ruedas_sku
        TEXT neumaticos_sku
        TEXT tija_sku
        TEXT manillar_sku
        TEXT pedales_sku
        TEXT sillin_sku
    }
    COTIZACION {
        TEXT id_pedido PK
        INTEGER calculo_precio
    }
    CODIGOS_DESCUENTOS {
        TEXT codigo PK
        REAL porcentaje
    }
    COTIZACION_CODIGO {
        TEXT id_pedido PK
        TEXT codigo_seleccionado PK
    }
    BICICLETA {
        TEXT id_pedido PK
        INTEGER precio
    }
    TRANSACCIONES {
        TEXT id_pago PK
        INTEGER monto_pagado
    }
    BOLETA {
        TEXT id_pedido PK
        INTEGER precio_final
        INTEGER id_pago
    }
    HISTORICO_PEDIDOS {
        TEXT id_pedido PK
        TEXT fecha_entrega_pedido
    }
    GARANTIA {
        TEXT id_pedido PK
        TEXT fecha_inicio
        TEXT fecha_fin
        TEXT cobertura
        TEXT condiciones
        BLOB estado
    }

    PERSONAS ||--o{ CLIENTES : "relación"
    PERSONAS ||--o{ TECNICOS : "relación"
    CLIENTES ||--o{ PEDIDO : "realiza"
    TECNICOS ||--o{ TECNICO_PEDIDO : "asigna"
    PEDIDO ||--o{ TECNICO_PEDIDO : "tiene"
    PEDIDO ||--o{ COMPONENTES : "relación"
    COMPONENTES ||--o{ COTIZACION : "genera"
    COTIZACION ||--o{ COTIZACION_CODIGO : "aplica"
    COTIZACION ||--o{ BICICLETA : "relación"
    BICICLETA ||--o{ BOLETA : "genera"
    BOLETA ||--o{ TRANSACCIONES : "relación"
    PEDIDO ||--o{ HISTORICO_PEDIDOS : "archiva"
    HISTORICO_PEDIDOS ||--o{ GARANTIA : "relación"
    ALMACEN ||--o{ COMPONENTES : "proporciona"

