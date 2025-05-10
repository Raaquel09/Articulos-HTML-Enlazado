# Importamos las librerias necesarias 
import os
import re
import subprocess
import sys
import shutil

# Abrimos el fichero.bib que contiene la bibliografia de todos los pdfs
# En este caso se llama conjuntoBIB.bib

def extract_urls_from_bib(bib_file):
    # Del campo url de cada uno de los papers sacarmos la url
    # Funciona con cualquier tipo de url pero si no es directa a un pdf RSEF no se ejecuta correctamente
    url_pattern = r'url\s*=\s*\{(https?://[^\}]+)\}'
    
    with open(bib_file, 'r') as file:
        content = file.read()
    
    urls = re.findall(url_pattern, content)
    return urls

# Cogemos la ultima parte de la url y le quitamos la extension para hacer las carpetas de salida con el nombre del pdf
def get_pdf_name_from_url(url):
    return os.path.splitext(os.path.basename(url))[0]

# Procesamos el fichero bib
def process_bib_file(bib_file_path, output_folder):
    print(f"\nLeemos el fichero: {bib_file_path}")

    # Extraemos las urls del fichero bib
    urls = extract_urls_from_bib(bib_file_path)

    if not urls:
        print("No se encontraron URLs en el fichero .bib")
        return

    # Por cada url realizamos lo siguiente:
    # Saca el nombre del pdf y lo usa para crear una carpeta con este mismo nombre
    # Ejecuta el comando: rsef download -i <url> -o <output_dir>
    # rsef download -i urlPDF -o carpetaNombrePDF
    # Si se ha ejecutado correctamente ejecuta el sigueiente comando: rsef assess -i <metadata> -o <output_dir> -U -B
    # rsef assess -i downloaded_metadata.json -o carpetaNombrePDF -U -B

    for url in urls:
        pdf_name = get_pdf_name_from_url(url)
        output_dir = os.path.join(output_folder, pdf_name)
        os.makedirs(output_dir, exist_ok=True)

        print(f"Ejecutamos el comando download de RSEF: rsef download -i {url} -o {output_dir}")
        subprocess.run(['rsef', 'download', '-i', url, '-o', output_dir])

        metadata_path = os.path.join(output_dir, 'downloaded_metadata.json')
        if os.path.isfile(metadata_path):
            print(f"Ejecutamos el comando assess de RSEF: rsef assess -i {metadata_path} -o {output_dir} -U -B")
            subprocess.run(['rsef', 'assess', '-i', metadata_path, '-o', output_dir, '-U', '-B'])
        else:
            print(f"No se encuentra {metadata_path}, no se omite puede ejecutar rsef assess")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("El primer argumento tiene que ser un fichero.bib, la carpeta del segundo argumento si no existe se crea")
        print("Uso: python script.py <archivo.bib> <carpeta_de_salida>")
        print("Ejemplo: python RSEFTodos.py conjuntoBIB.bib SalidaRSEF")
        sys.exit(1)
    
    # Dos argumentos, ruta a un fichero .bib y una carpeta de salida
    bib_file_path = sys.argv[1]
    output_folder = sys.argv[2]
    
    if not os.path.isfile(bib_file_path) or not bib_file_path.endswith('.bib'):
        print(f"Error: {bib_file_path} no es un archivo .bib valido")
        sys.exit(1)
    # Si la carpeta de salida no existe se crea
    os.makedirs(output_folder, exist_ok=True)
    
    process_bib_file(bib_file_path, output_folder)
