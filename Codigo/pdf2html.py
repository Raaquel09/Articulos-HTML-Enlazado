# Importamos las librerias necesarias 
import os
import subprocess
import sys

# La funcion tiene dos argumentos:
# carpeta_raiz --> Ruta de la carpeta principal (SalidaRSEF)
# carpeta_salida --> Ruta de la carpeta de salida para los html (PaginaWeb/html)


# Tendremos dos carpetas mas a tener en cuenta:
# subcarpeta1 --> Carpetas que se crean con el nombre del paper, salida de RSEF
# subcarpeta2 --> Carpeta en la que se guardan los html

# Estructura:
# carpeta_raiz (SalidaRSEF)
#   subcarpeta1 (carpetaBIB1)
#       subcarpeta2 (PDFs)
#           nombrepdf1.pdf
#   subcarpeta1 (carpetaBIB2)
#       subcarpeta2 (PDFs)
#           nombrepdf2.pdf
#   subcarpeta1 (carpetaBIB3)
#       subcarpeta2 (PDFs)
#           nombrepdf3.pdf

def convertir_pdfs(carpeta_raiz, carpeta_salida):
    # Recorremos las subcarpetas que hay en la carpeta_raiz (son las creadas por RSEF)
    for subcarpeta1 in os.listdir(carpeta_raiz):
        ruta_subcarpeta1 = os.path.join(carpeta_raiz, subcarpeta1)
        if not os.path.isdir(ruta_subcarpeta1):
            continue
        # Recorremos las subcarpetas que hay en las carpetas creadas por RSEF
        # Tiene que haber una carpeta llamada PDFs que contiene el pdf descargado por RSEF con el comando download
        for subcarpeta2 in os.listdir(ruta_subcarpeta1):
            ruta_subcarpeta2 = os.path.join(ruta_subcarpeta1, subcarpeta2)
            if not os.path.isdir(ruta_subcarpeta2):
                continue

            # Busca el pdf dentro de la carpeta PDFs
            for archivo in os.listdir(ruta_subcarpeta2):
                if archivo.lower().endswith(".pdf"):
                    # Generamos la ruta del pdf
                    ruta_pdf = os.path.join(ruta_subcarpeta2, archivo)

                    # Usamos el nombre del PDF para el archivo HTML (quitamos la extension)
                    nombre_base = os.path.splitext(archivo)[0]
                    nombre_html = f"{nombre_base}.html"
                    # La ruta del HTML es el segundo argumento de la funcion
                    ruta_html = os.path.join(carpeta_salida, nombre_html)

                    # Ejecutamos el comando que convierte el pdf en un html
                    comando = ["pdf2htmlEX", "--zoom", "1.3", ruta_pdf, ruta_html]
                    print(f"Ejecutamos el comando que pasa de PDF a HTML: {' '.join(comando)}")
                    subprocess.run(comando)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("La carpeta del primer argumento tiene que existir, la del segundo si no existe se crea")
        print("Comando: python script.py <carpeta_raiz> <carpeta_salida>")
        print("Ejemplo: python pdf2htmlTodos.py SalidaRSEF PaginaWeb/html")
        sys.exit(1)

    # Dos argumentos, si la carpeta del segundo argumento no existe la crea
    carpeta_raiz = sys.argv[1]
    carpeta_salida = sys.argv[2]
    os.makedirs(carpeta_salida, exist_ok=True)
    convertir_pdfs(carpeta_raiz, carpeta_salida)
