# Importamos las librerias necesarias 
import os
import sys
import json
import shutil
from pathlib import Path
import bibtexparser

# Lee el archivo .bib 
def process_bib(bib_file):
    with open(bib_file, 'r', encoding='utf-8') as f:
        bib_content = f.read()
    bib_database = bibtexparser.loads(bib_content)
    return bib_database.entries

# Comprobamos que tenga el numero de argumentos correctos:
# bib_file --> Fichero .bib con la informacion de cada paper
# carpeta_raiz --> Ruta de la carpeta principal (SalidaRSEF)
# carpeta_salida --> Ruta de la carpeta de salida para guardar el codigo de la pagina web y el fichero conjuntoJSON (PaginaWeb)
if len(sys.argv) != 4:
    print("El fichero .bib y carpeta del segundo argumento tienen que existir, la del tercero si no existe se crea")
    print("Uso: python unirTodos.py <bib_file> <carpeta_raiz> <carpeta_salida>")
    print("Ejemplo: python unirTodos.py conjuntoBIB.bib SalidaRSEF PaginaWeb")
    sys.exit(1)

# Tres argumentos, ruta a un fichero .bib, carpeta_raiz y carpeta de salida
bib_file = sys.argv[1]
carpeta_raiz = sys.argv[2]
carpeta_salida = sys.argv[3]

# La carpeta de salida si no existe la creamos
os.makedirs(carpeta_salida, exist_ok=True)

entradas_bib = process_bib(bib_file)

# Inicializa la lista, en la que cada elemento sera el contenido de un paper
datos_combinados = []

# Itera sobre subcarpeta1, en la que cada una corresponde a un paper
# Se comprueba que subcarpeta1 es una carpeta y que contiene el fichero url_search_output.json 
for subcarpeta1 in os.listdir(carpeta_raiz):
    ruta_subcarpeta1 = os.path.join(carpeta_raiz, subcarpeta1)
    if not os.path.isdir(ruta_subcarpeta1):
        continue

    ruta_json = os.path.join(ruta_subcarpeta1, "url_search_output.json")
    if not os.path.isfile(ruta_json):
        print(f"No se ha encontrado el fichero {ruta_json}")
        continue

    # Buscar la entrada .bib que coincida con el nombre de la carpeta
    # Se busca que la entrada .bib tenga el final del campo url igual que el nombre de subcarpeta1
    bib_entry = None
    for entry in entradas_bib:
        url = entry.get("url", "")
        carpeta_url = os.path.splitext(os.path.basename(url))[0]
        if carpeta_url == subcarpeta1:
            bib_entry = entry
            break

    if bib_entry is None:
        print(f"No se ha encontrado una entrada .bib que coincida con la carpeta '{subcarpeta1}'")
        continue

    # Buscar subcarpeta2 (PDFs) dentro de subcarpeta1 
    for subcarpeta2 in os.listdir(ruta_subcarpeta1):
        ruta_subcarpeta2 = os.path.join(ruta_subcarpeta1, subcarpeta2)
        if not os.path.isdir(ruta_subcarpeta2):
            continue

        # Coge el pdf
        for file in os.listdir(ruta_subcarpeta2):
            if file.lower().endswith(".pdf"):
                 # Usamos el nombre del PDF para el archivo HTML (quitamos la extension)
                nombre_pdf = os.path.splitext(file)[0]
                archivo_html = f"{nombre_pdf}.html"
                # Forma una ruta relativa
                url_html = f"html/{archivo_html}"

                # Lee el json que hay en la carpeta url_search_output.json
                with open(ruta_json, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Si el json es una lista de objetos (debería de serlo ya que es el formato de RSEF)
                # Agrega el campo file_html con la ruta relativa al html generado
                # Mete tambien la informacion de la entrada del bib correspondiente
                if isinstance(data, list):
                    for item in data:
                        item["file_html"] = url_html
                        item.update(bib_entry)

                # Si el json no es una lista de objetos lo convierte en una de un solo objeto
                # Agrega el campo file_html con la ruta relativa al html generado
                # Mete tambien la informacion de la entrada del bib correspondiente
                elif isinstance(data, dict):
                    data["file_html"] = url_html
                    data.update(bib_entry)
                    data = [data]
                else:
                    print(f"Formato inesperado en {ruta_json}")
                    continue

                # Combinamos toda la informacion para crear un unico archivo
                datos_combinados.extend(data)

# Guardamos el resultado en conjuntoJSON.json
ruta_salida_json = os.path.join(carpeta_salida, "conjuntoJSON.json")
with open(ruta_salida_json, "w", encoding="utf-8") as f:
    json.dump(datos_combinados, f, indent=4, ensure_ascii=False)


# Copiar paginaWeb.html a carpeta_salida, asi no dependemos de que la carpeta ya este hecha y con el fichero dentro
ruta_html_origen = os.path.join(os.path.dirname(__file__), "paginaWeb.html")
ruta_html_destino = os.path.join(carpeta_salida, "paginaWeb.html")

try:
    shutil.copy(ruta_html_origen, ruta_html_destino)
    print(f"Copiado paginaWeb.html en {ruta_html_destino}")
except FileNotFoundError:
    print(f"No se ha encontrado paginaWeb.html en el directorio del codigo")
