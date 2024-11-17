from custom_bikes.funciones.funciones_analisis import analisis_tipo_bicicleta, analisis_categoria_producto, seleccion_tipo, seleccion_categoria, contar_repeticiones_sku

def menu_analisis():
    while True:
        print('1. Analisis de tipo de bicicleta mas vendidas')
        print('2. Analisis de categoria de componentes mas vendidas')
        print('3. Productos mas vendidos')
        print('4. Volver al menú principal')

        seleccion = int(input('Seleccione una opción: '))

        if seleccion == 1:
            tipos_seleccionados = seleccion_tipo()
            analisis_tipo_bicicleta(tipos_seleccionados)

        elif seleccion == 2:
            categorias_seleccionadas = seleccion_categoria()
            analisis_categoria_producto(categorias_seleccionadas)

        elif seleccion == 3:
            contar_repeticiones_sku()

        elif seleccion == 4:
            print('Volver al menú principal')
            break
        
        else:
            print('Opción inválida')