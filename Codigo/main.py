# Importamos las librerias necesarias 
import sys
import subprocess
import os

def main():

    with open("salida.txt", "w") as f:
        def log(msg):
            print(msg)
            f.write(msg + "\n")
            f.flush()

    if len(sys.argv) != 5:
        print("Uso: python main.py archivo.bib carpetaSalidaRSEF carpetaSalidaHTMLs carpetaSalidaConjuntoJSON+CodigoPaginaWeb")
        print("Se ejecuta desde la carpeta Codigo")
        print("Ejemplo: python main.py ../Pruebas/BibTex/conjuntoBIB.bib ../Pruebas/SalidaRSEF ../Pruebas/PaginaWeb/html ../Pruebas/PaginaWeb")
        sys.exit(1)

    archivo_bib = sys.argv[1]
    carpeta1 = sys.argv[2]  # carpetaSalidaRSEF --> SalidaRSEF
    carpeta2 = sys.argv[3]  # carpetaSalidaHTMLs --> PaginaWeb/html
    carpeta3 = sys.argv[4]  # carpetaSalidaConjuntoJSON+CodigoPaginaWeb --> PaginaWeb

    # Comando 1: python RSEF.py conjuntoBIB.bib SalidaRSEF
    print("Ejemplo: python RSEF.py conjuntoBIB.bib SalidaRSEF")
    print(f"Ejecutando: RSEF.py {archivo_bib} {carpeta1}")
    subprocess.run(["python", "RSEF.py", archivo_bib, carpeta1], check=True)

    # Comando 2: python pdf2htmlTodos.py SalidaRSEF PaginaWeb/html
    print("Ejemplo: python pdf2html.py SalidaRSEF PaginaWeb/html")
    print(f"Ejecutando: pdf2html.py {carpeta1} {carpeta2}")
    subprocess.run(["python", "pdf2html.py", carpeta1, carpeta2], check=True)

    # Comando 3: python unirTodos.py conjuntoBIB.bib SalidaRSEF PaginaWeb
    print("Ejemplo: python unir.py conjuntoBIB.bib SalidaRSEF PaginaWeb")
    print(f"Ejecutando: unir.py {archivo_bib} {carpeta1} {carpeta3}")
    subprocess.run(["python", "unir.py", archivo_bib, carpeta1, carpeta3], check=True)

if __name__ == "__main__":
    main()
