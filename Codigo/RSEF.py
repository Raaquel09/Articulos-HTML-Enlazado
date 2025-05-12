# Importamos las librerías necesarias  
import os
import re
import subprocess
import sys
import shutil
import requests  # Para comprobar si la URL es válida

# Abrimos el fichero .bib que contiene la bibliografía de todos los PDFs
# En este caso se llama conjuntoBIB.bib

def extract_urls_from_bib(bib_file):
    # Del campo URL de cada uno de los papers sacamos la URL
    # Funciona con cualquier tipo de URL, pero si no es directa a un PDF RSEF no se ejecuta correctamente
    url_pattern = r'url\s*=\s*\{(https?://[^\}]+)\}'
    
    with open(bib_file, 'r') as file:
        content = file.read()
    
    urls = re.findall(url_pattern, content)
    return urls

def is_valid_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        
        # Verificamos si el Content-Type es application/pdf
        if 'application/pdf' in response.headers.get('Content-Type', ''):
            return response.status_code == 200  # Solo si la URL responde con un 200 OK y es un PDF
        else:
            print(f"La URL no apunta a un PDF: {url}")
            return False
    except requests.RequestException:
        return False


# Cogemos la última parte de la URL y le quitamos la extensión para hacer las carpetas de salida con el nombre del PDF
def get_pdf_name_from_url(url):
    return os.path.splitext(os.path.basename(url))[0]

# Procesamos el fichero .bib
def process_bib_file(bib_file_path, output_folder):
    print(f"\nLeemos el fichero: {bib_file_path}")

    # Extraemos las URLs del fichero .bib
    urls = extract_urls_from_bib(bib_file_path)

    if not urls:
        print("No se encontraron URLs en el fichero .bib")
        return

    # Por cada URL realizamos lo siguiente:
    # Saca el nombre del pdf y lo usa para crear una carpeta con este mismo nombre
    # Ejecuta el comando: rsef download -i <url> -o <output_dir>
    # rsef download -i urlPDF -o carpetaNombrePDF
    # Si se ha ejecutado correctamente ejecuta el sigueiente comando: rsef assess -i <metadata> -o <output_dir> -U -B
    # rsef assess -i downloaded_metadata.json -o carpetaNombrePDF -U -B

    for url in urls:
        # Hay que comprobar si la URL es válida
        if is_valid_url(url):  
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
                print(f"No se encuentra {metadata_path}, no se puede ejecutar rsef assess")
        else:
            print(f"La URL no es válida: {url}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("El primer argumento tiene que ser un fichero .bib, la carpeta del segundo argumento si no existe se crea")
        print("Uso: python script.py <archivo.bib> <carpeta_de_salida>")
        print("Ejemplo: python RSEFTodos.py conjuntoBIB.bib SalidaRSEF")
        sys.exit(1)
    
    # Dos argumentos, ruta a un fichero .bib y una carpeta de salida
    bib_file_path = sys.argv[1]
    output_folder = sys.argv[2]
    
    if not os.path.isfile(bib_file_path) or not bib_file_path.endswith('.bib'):
        print(f"Error: {bib_file_path} no es un archivo .bib válido")
        sys.exit(1)
    
    # Si la carpeta de salida no existe se crea
    os.makedirs(output_folder, exist_ok=True)
    
    process_bib_file(bib_file_path, output_folder)
