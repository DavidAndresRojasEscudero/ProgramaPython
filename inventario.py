CODIGO       = 0
NOMBRE       = 1
STOCK_ACTUAL = 2
STOCK_MINIMO = 3

def calcular_cantidad_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        cantidad_a_pedir = 0
 
    return cantidad_a_pedir
 
def capturar_inventario(cantidad_articulos):
    matriz_inventario = []
 
    for i in range(1, cantidad_articulos + 1):
        print(f"\n||1 Datos del artículo {i} ||")
 
        codigo = input("Codigo del articulo: ")
        nombre = input("Nombre del articulo: ")
        stock_actual = int(input("Stock actual: "))
        stock_minimo = int(input("Stock minimo requerido: "))

        articulo = [codigo, nombre, stock_actual, stock_minimo]
        matriz_inventario.append(articulo)
 
    return matriz_inventario
 
def generar_reporte_pedidos(matriz_inventario):
    print("\n=============================")
    print("LISTA DE PEDIDOS A REALIZAR")
    print("=============================")
 
    hubo_pedidos = False  

    for articulo in matriz_inventario:
 
        nombre_articulo = articulo[NOMBRE]
        actual = articulo[STOCK_ACTUAL]
        minimo = articulo[STOCK_MINIMO]
 
        cantidad = calcular_cantidad_pedido(actual, minimo)
 
        # Solo se muestra en el reporte si hace falta pedir algo
        if cantidad > 0:
            print(f"Artículo: {nombre_articulo}   ||   Cantidad a pedir: {cantidad}")
            hubo_pedidos = True
 
    if not hubo_pedidos:
        print("Todos los artículos tienen stock suficiente. No hay pedidos.")
 
 
CANTIDAD_ARTICULOS = 5
print("\n=======================")
print("REGISTRO DE INVENTARIO")
print("=======================")
 
inventario = capturar_inventario(CANTIDAD_ARTICULOS)
 
print("\n==================")
print("INVENTARIO ACTUAL")
print("==================")
 
for articulo in inventario:
    print(f"Código: {articulo[CODIGO]} | Nombre: {articulo[NOMBRE]} "
          f"| Stock Actual: {articulo[STOCK_ACTUAL]} | Stock Mínimo: {articulo[STOCK_MINIMO]}")
 
generar_reporte_pedidos(inventario)