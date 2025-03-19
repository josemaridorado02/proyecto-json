def listar_titulos(datos):
    for articulo in datos["articulos"]:
        print(f"Título: {articulo['titulo']}")
        print(f"Fecha de publicación: {articulo['publicadoEn']}")
        print(f"Etiquetas: {', '.join(articulo['etiquetas'])}\n")

def listar_titulos_simples(datos):
    """Muestra solo los títulos de los artículos disponibles."""
    for articulo in datos["articulos"]:
        print(f"- {articulo['titulo']}")

def listar_autores(datos):
    """Muestra la lista de autores únicos en orden alfabético."""
    autores = set()
    for articulo in datos["articulos"]:
        autores.add(articulo["autor"]["nombre"])
    
    for autor in sorted(autores):
        print(f"- {autor}")

def total_articulos_por_categoria(datos):
    categorias = {}
    for articulo in datos["articulos"]:
        for categoria in articulo["fuente"]["categorias"]:
            categorias[categoria] = categorias.get(categoria, 0) + 1
    
    for categoria, total in categorias.items():
        print(f"Categoría: {categoria}, Total de artículos: {total}")

def mostrar_companias(datos, titulo):
    for articulo in datos["articulos"]:
        if articulo["titulo"].lower() == titulo.lower():
            if "empresas" in articulo:
                print("\nCompañías relacionadas:")
                for empresa in articulo["empresas"]:
                    print(f"- {empresa['nombre']} ({empresa['industria']})")
            else:
                print("\nNo hay compañías relacionadas con este artículo.")
            return
    print("\nArtículo no encontrado.")

def buscar_por_autor(datos, autor):
    encontrado = False
    for articulo in datos["articulos"]:
        if articulo["autor"]["nombre"].lower() == autor.lower():
            print(f"\nTítulo: {articulo['titulo']}")
            print(f"Fecha de publicación: {articulo['publicadoEn']}")
            encontrado = True
    if not encontrado:
        print("\nNo se encontró ningún artículo de este autor.")

def resumen_por_fuente(datos):
    fuentes = {}
    for articulo in datos["articulos"]:
        fuente = articulo["fuente"]["nombre"]
        if fuente not in fuentes:
            fuentes[fuente] = []
        fuentes[fuente].append(articulo["titulo"])
    
    for fuente, titulos in fuentes.items():
        print(f"\nFuente: {fuente}, Total de artículos: {len(titulos)}")
        for titulo in titulos:
            print(f"- {titulo}")
        print()

