import cv2
import numpy as np
import os
import pandas as pd

def calcular_momentos_hu(imagen):
    momentos = cv2.moments(imagen)
    mu_20 = momentos["mu20"]
    mu_02 = momentos["mu02"]
    mu_11 = momentos["mu11"]
    mu_30 = momentos["mu30"]
    mu_12 = momentos["mu12"]
    mu_21 = momentos["mu21"]
    mu_03 = momentos["mu03"]

    phi1 = mu_20 + mu_02
    phi2 = (mu_20 - mu_02)**2 + 4 * mu_11**2
    phi3 = (mu_30 - 3 * mu_12)**2 + (3 * mu_21 - mu_03)**2

    return phi1, phi2, phi3

def rotar_imagen(imagen, angulo):
    (h, w) = imagen.shape[:2]
    centro = (w // 2, h // 2)
    matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo, 1.0)
    imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return imagen_rotada

def procesar_imagenes(directorio, angulo_rotacion, archivo_salida):
    archivos = [f for f in os.listdir(directorio) if f.endswith('.png')]
    print(f"Procesando {len(archivos)} imágenes...")

    datos = []

    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        _, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

        # Calcular momentos de Hu antes de la rotación
        hu_original = calcular_momentos_hu(imagen_binaria)

        # Rotar la imagen
        imagen_rotada = rotar_imagen(imagen_binaria, angulo_rotacion)

        # Calcular momentos de Hu después de la rotación
        hu_rotada = calcular_momentos_hu(imagen_rotada)

        # Guardar en la lista
        datos.append([archivo, hu_original[0], hu_original[1], hu_original[2], hu_rotada[0], hu_rotada[1], hu_rotada[2]])

    # Crear DataFrame y guardar en CSV
    columnas = ["Imagen", "Hu1_Original", "Hu2_Original", "Hu3_Original", "Hu1_Rotado", "Hu2_Rotado", "Hu3_Rotado"]
    df = pd.DataFrame(datos, columns=columnas)
    df.to_csv(archivo_salida, index=False)

    print(f"Resultados guardados en '{archivo_salida}'")

# Directorio con imágenes binarias
carpeta_binarias = "Imagenes_binarias"
archivo_csv = "resultados_momentos_hu.csv"

# Procesar imágenes y guardar los resultados en CSV
procesar_imagenes(carpeta_binarias, 45, archivo_csv)
