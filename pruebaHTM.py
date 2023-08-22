import requests
from tqdm import tqdm
from IPython.display import clear_output


def descargar_imagen(url, nombre_archivo):
    try:
        respuesta = requests.get(url, stream=True)
        respuesta.raise_for_status()

        total_size = int(respuesta.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=nombre_archivo, dynamic_ncols=True,
                            leave=False)

        with open(nombre_archivo, 'wb') as archivo:
            for chunk in respuesta.iter_content(chunk_size=1024):
                archivo.write(chunk)
                progress_bar.update(len(chunk))

        progress_bar.close()
        print("Imagen descargada exitosamente como", nombre_archivo)
        return True
    except requests.exceptions.RequestException as e:
        print("Error al descargar la imagen:", e)
    except Exception as e:
        print("Ocurrió un error:", e)

    return False


# Lista de URLs de libros
urls_libros = [
    "https://www.conaliteg.sep.gob.mx/2023/c/P1LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1TPA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P0CMA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P0SHA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6SDA/"
]

extension = ".jpg"
noLibro = 0

total_images = sum([len(range(0, 1000)) for _ in urls_libros])  # Total de imágenes (asumiendo que son 1000 por URL)
progress_bar = tqdm(total=total_images, unit='imagen', unit_scale=True, dynamic_ncols=True)

for noLibro, base_url in enumerate(urls_libros, start=1):
    contador = 0
    while True:
        numero_imagen = str(contador).zfill(3)
        url_imagen = f"{base_url}{numero_imagen}{extension}"
        print("Intentando descargar:", url_imagen)

        if not descargar_imagen(url_imagen, f"imagen_descargada_{noLibro}_Libro_{contador}.jpg"):
            break

        contador += 1

    clear_output(wait=True)  # Limpia la salida de la consola
    progress_bar.update(1000)  # Actualiza la barra de progreso con el progreso de 1000 imágenes
    progress_bar.refresh()  # Refresca la barra de progreso

progress_bar.close()  # Cierra la barra de progreso final