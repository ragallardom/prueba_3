import globales, math

def valor_alto():
    archivo_valores = globales.leer_archivo_csv("valor_productos.csv")

    valores_ordenados = sorted(archivo_valores, key=lambda x: x["valor"], reverse=True)
    print("El producto con valor más alto es")
    print("   Producto   | valor | IVA")
    print(f"{valores_ordenados[:1][0]['producto']} | {valores_ordenados[:1][0]['valor']} | {valores_ordenados[:1][0]['iva']}\n")

def valor_iva_bajo():
    archivo_valores = globales.leer_archivo_csv("valor_productos.csv")

    valores_ordenados = sorted(archivo_valores, key=lambda x: x["valor"], reverse=False)
    print("El producto con IVA más bajo es")
    print("   Producto   | valor | IVA")
    print(f"{valores_ordenados[:1][0]['producto']} | {valores_ordenados[:1][0]['valor']} | {valores_ordenados[:1][0]['iva']}\n")

def promedio():
    archivo_valores = globales.leer_archivo_csv("valor_productos.csv")

    suma = 0
    cantidad = 0

    for valor in archivo_valores:
        suma += int(valor['valor'])
        cantidad += 1

    promedio = suma / cantidad

    print(f"El promedio de las ventas es: {promedio}\n")

def media_geo():
    archivo_valores = globales.leer_archivo_csv("valor_productos.csv")

    suma = 0
    cantidad = 0

    for valor in archivo_valores:
        suma += math.log(int(valor['valor']))
        cantidad += 1

    media_geo = math.exp(suma / cantidad)

    print(f"La media geométrica de las ventas es: {media_geo}\n")
