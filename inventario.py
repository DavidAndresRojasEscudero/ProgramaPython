CODIGO       = 0
NOMBRE       = 1
STOCK_ACTUAL = 2
STOCK_MINIMO = 3

def calcular_cantidad_pedido(stock_actual, stock_minimo):
   
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        # Si el stock actual es suficiente, no se pide nada
        cantidad_a_pedir = 0

    return cantidad_a_pedir

def generar_reporte_pedidos(matriz_inventario):
    print("\n========================================")
    print("       LISTA DE PEDIDOS A REALIZAR")
    print("========================================")

    hubo_pedidos = False

    for articulo in matriz_inventario:

        nombre_articulo = articulo[NOMBRE]
        actual = articulo[STOCK_ACTUAL]
        minimo = articulo[STOCK_MINIMO]
        cantidad = calcular_cantidad_pedido(actual, minimo)

        if cantidad > 0:
            print(f"Artículo: {nombre_articulo:15} -> Cantidad a pedir: {cantidad}")
            hubo_pedidos = True

    if not hubo_pedidos:
        print("Todos los artículos tienen stock suficiente. No hay pedidos.")

    print("========================================")

inventario = [
    ["A001", "Teclado USB",        8,  10],
    ["A002", "Mouse Óptico",      15,  10],
    ["A003", "Monitor 24 pulg",    3,   5],
    ["A004", "Cable HDMI",        20,  15],
    ["A005", "Disco Duro 1TB",     2,   6],
]

print("========================================")
print("        INVENTARIO ACTUAL")
print("========================================")

for articulo in inventario:
    print(f"Código: {articulo[CODIGO]} | Nombre: {articulo[NOMBRE]:15} "
          f"| Stock Actual: {articulo[STOCK_ACTUAL]} | Stock Mínimo: {articulo[STOCK_MINIMO]}")

generar_reporte_pedidos(inventario)
