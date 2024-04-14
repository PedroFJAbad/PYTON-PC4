import requests
import zipfile
import os

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print("Imagen descargada correctamente.")
    else:
        print("Error al descargar la imagen.")

def zip_files(files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            zipf.write(file)
    print("Archivos comprimidos correctamente.")

def unzip_file(zip_filename, extract_folder):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print("Archivo descomprimido correctamente.")

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    filename = "image.jpg"
    zip_filename = "images.zip"
    extract_folder = "unzipped_images"

    download_image(url, filename)
    zip_files([filename], zip_filename)
    unzip_file(zip_filename, extract_folder)

    # Limpiar los archivos temporales
    os.remove(filename)
    os.remove(zip_filename)

if __name__ == "__main__":
    main()