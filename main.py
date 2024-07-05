import globales, os, random, estadisticas

MENU_GENERAL = (
    "\t=== Menú General ==="
    "\n\t1. Asignar montos aleatorios"
    "\n\t2. Ver estadisticas."
    "\n\t3. Salir del programa."
)

def asignar_montos():
    archivo_productos = globales.leer_archivo_json("productos.json")

    valor_productos = []

    for producto in archivo_productos:
        valor = random.randint(2000, 10000)

        nuevo_valor = {
            
            "producto": producto["producto"],
            "valor": valor,
            "iva": int(valor * 0.19)
        }

        valor_productos.append(nuevo_valor)
    
    globales.guardar_archivo_csv("valor_productos.csv", valor_productos, ["producto", "valor", "iva"])

def menu_general():
    while True:
        opcion = globales.seleccionar_opcion(3, MENU_GENERAL)

        match opcion:
            case 1:
                os.system("cls")
                asignar_montos()
                input("Se ha cargado el valor de los productos, presione ENTER para continuar...")
            case 2:
                os.system("cls")
                print("Estadisticas\n")
                estadisticas.valor_alto()
                estadisticas.valor_iva_bajo()
                estadisticas.promedio()
                estadisticas.media_geo()
                input("\nPresione ENTER para continuar...")
            case 3:
                input("Saliendo del programa, presione ENTER para continuar...")
                return

if __name__ == "__main__":
    menu_general()