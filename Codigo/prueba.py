import os
import re
import subprocess
import sys

def extract_entries_from_bib(bib_file):
    with open(bib_file, 'r') as file:
        content = file.read()

    # Divide el contenido en bloques @article{...}
    entries = re.findall(r'@[\w]+\s*\{[^@]*?\}', content, re.DOTALL)
    return entries

def extract_field(entry, field_name):
    # Extrae el valor del campo deseado (url, eprint, etc.)
    pattern = rf'{field_name}\s*=\s*\{{(https?://[^\}}]+)\}}'
    match = re.search(pattern, entry, re.IGNORECASE)
    return match.group(1) if match else None

def get_pdf_name_from_url(url):
    return os.path.splitext(os.path.basename(url))[0]

def process_bib_file(bib_file_path, output_folder):
    print(f"\nLeemos el fichero: {bib_file_path}")

    entries = extract_entries_from_bib(bib_file_path)

    if not entries:
        print("No se encontraron entradas en el fichero .bib")
        return

    for entry in entries:
        url = extract_field(entry, 'url')
        eprint = extract_field(entry, 'eprint')

        selected_url = None
        source = None

        # Prioridad: usar 'url' si es un PDF, si no probar con 'eprint'
        if url and url.endswith(".pdf"):
            selected_url = url
            source = "url"
        elif eprint and eprint.endswith(".pdf"):
            selected_url = eprint
            source = "eprint"
        else:
            print("Entrada omitida: no hay URL ni eprint válido (PDF)")
            continue

        pdf_name = get_pdf_name_from_url(selected_url)
        output_dir = os.path.join(output_folder, pdf_name)
        os.makedirs(output_dir, exist_ok=True)

        print(f"\nUsando {source} para descargar: {selected_url}")
        print(f"Ejecutamos: rsef download -i {selected_url} -o {output_dir}")
        subprocess.run(['rsef', 'download', '-i', selected_url, '-o', output_dir])

        metadata_path = os.path.join(output_dir, 'downloaded_metadata.json')
        if os.path.isfile(metadata_path):
            print(f"Ejecutamos: rsef assess -i {metadata_path} -o {output_dir} -U -B")
            subprocess.run(['rsef', 'assess', '-i', metadata_path, '-o', output_dir, '-U', '-B'])
        else:
            print(f"No se encuentra {metadata_path}, no se puede ejecutar rsef assess")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python script.py <archivo.bib> <carpeta_de_salida>")
        print("Ejemplo: python RSEFTodos.py conjuntoBIB.bib SalidaRSEF")
        sys.exit(1)

    bib_file_path = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.isfile(bib_file_path) or not bib_file_path.endswith('.bib'):
        print(f"Error: {bib_file_path} no es un archivo .bib válido")
        sys.exit(1)

    os.makedirs(output_folder, exist_ok=True)
    process_bib_file(bib_file_path, output_folder)
