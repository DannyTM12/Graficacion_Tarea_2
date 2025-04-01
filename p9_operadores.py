import cv2
import numpy as np
import os

carpeta_imagenes = "imagenes_binarias/"

carpeta_resultados = "resultados/"


def esqueleto(index, ruta_imagen):
    """
    Obtiene el esqueleto de una imagen binaria.

    Args:
        img (numpy.ndarray): Imagen binaria (blanco y negro).

    Returns:
        numpy.ndarray: Esqueleto de la imagen.
    """

    # Cargar la imagen en escala de grises
    imagen = cv2.imread(ruta_imagen, 0)

    if imagen is None:
        print(f"Error: No se pudo cargar la imagen desde {ruta_imagen}")
        return None

    imagen = imagen.copy()  # Copia para no modificar la original
    skel = np.zeros(imagen.shape, np.uint8)
    size = np.size(imagen)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while not done:
        eroded = cv2.erode(imagen, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(imagen, temp)
        skel = cv2.bitwise_or(skel, temp)
        imagen = eroded.copy()

        zeros = size - cv2.countNonZero(imagen)
        if zeros == size:
            done = True

    # resultados bordes
    carpeta_esqueleto = os.path.join(carpeta_resultados, 'esqueleto')

    nombre_imagen = f'{index}_equeleto.png'

    ruta_resultado = os.path.join(carpeta_esqueleto, nombre_imagen)

    cv2.imwrite(ruta_resultado, skel)


def rellenar_huecos(index, ruta_imagen):

    # Cargar la imagen en escala de grises
    imagen = cv2.imread(ruta_imagen, 0)

    if imagen is None:
        print(f"Error: No se pudo cargar la imagen desde {ruta_imagen}")
        return None

    # 2. Define el elemento estructurante (kernel)
    kernel = np.ones((5, 5), np.uint8)  # Un kernel rectangular de 5x5

    # 3. Aplica el cierre
    cierre = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)

    # resultados bordes
    carpeta_rellenar = os.path.join(carpeta_resultados, 'rellenar_huecos')

    nombre_imagen = f'{index}_rellenar.png'

    ruta_resultado = os.path.join(carpeta_rellenar, nombre_imagen)

    cv2.imwrite(ruta_resultado, cierre)


def suavizar_bordes(index, ruta_imagen):

    # Cargar la imagen en escala de grises
    imagen = cv2.imread(ruta_imagen, 0)

    if imagen is None:
        print(f"Error: No se pudo cargar la imagen desde {ruta_imagen}")
        return None

    # 2. Define el elemento estructurante (kernel)
    kernel = np.ones((5, 5), np.uint8)  # Un kernel rectangular de 5x5

    # 3. Aplica la apertura
    apertura = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)

    # resultados bordes
    carpeta_bordes = os.path.join(carpeta_resultados, 'suavizar_bordes')

    nombre_imagen = f'{index}_bordes.png'

    ruta_resultado = os.path.join(carpeta_bordes, nombre_imagen)

    cv2.imwrite(ruta_resultado, apertura)


def reducir_ruido(index, ruta_imagen):

    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen, 0)  # Cargar en escala de grises

    # 2. Define el elemento estructurante (kernel)
    kernel = np.ones((5, 5), np.uint8)  # Un kernel rectangular de 5x5

    # 3. Aplica la erosión
    # Aplica la erosión una vez
    erosion = cv2.erode(imagen, kernel, iterations=1)

    # resultados ruido
    carpeta_ruido = os.path.join(carpeta_resultados, 'reducir_ruido')

    nombre_imagen = f'{index}_ruido.png'

    ruta_resultado = os.path.join(carpeta_ruido, nombre_imagen)

    cv2.imwrite(ruta_resultado, erosion)


for index, imagen in enumerate(os.listdir(carpeta_imagenes)):
    ruta_archivo = os.path.join(carpeta_imagenes, imagen)
    if os.path.isfile(ruta_archivo):
        esqueleto(index, ruta_archivo)
    else:
        print("Error:", ruta_archivo)
