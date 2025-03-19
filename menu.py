import json
import funciones

def cargar_datos():
    with open("proyecto.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

datos = cargar_datos()

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Listar títulos de artículos, fecha y etiquetas")
        print("2. Mostrar total de artículos por categoría")
        print("3. Buscar artículo y mostrar compañías relacionadas")
        print("4. Buscar artículo por autor y mostrar título y fecha")
        print("5. Resumen de noticias por fuente")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            funciones.listar_titulos(datos)
        elif opcion == "2":
            funciones.total_articulos_por_categoria(datos)
        elif opcion == "3":
            print("\nTítulos disponibles:")
            funciones.listar_titulos_simples(datos)  # Muestra solo los títulos
            titulo = input("\nIntroduce el título del artículo: ")
            funciones.mostrar_companias(datos, titulo)
        elif opcion == "4":
            print("\nAutores disponibles:")
            funciones.listar_autores(datos)  # Muestra la lista de autores únicos
            autor = input("\nIntroduce el nombre del autor: ")
            funciones.buscar_por_autor(datos, autor)
        elif opcion == "5":
            funciones.resumen_por_fuente(datos)
        elif opcion == "6":
            return
        else:
            print("Opción no válida, intenta de nuevo.")

menu()

