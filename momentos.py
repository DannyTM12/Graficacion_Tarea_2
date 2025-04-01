import cv2
import numpy as np
import os
import pandas as pd

def calcular_momentos_invariantes(imagen):
    # Calcular momentos centrales de la imagen
    momentos = cv2.moments(imagen)
    
    # Extraer los valores necesarios
    mu_00 = momentos['m00']
    
    if mu_00 == 0:
        return None  # Evitar divisiones por cero
    
    # Calcular momentos centrales
    mu_10 = momentos['m10']
    mu_01 = momentos['m01']
    mu_11 = momentos['m11']
    mu_20 = momentos['m20']
    mu_02 = momentos['m02']
    
    # Calcular momentos centrales normalizados
    mu_10_normalizado = mu_10 / mu_00
    mu_01_normalizado = mu_01 / mu_00
    
    # Calcular momentos centrales de segundo orden
    mu_20_normalizado = mu_20 / (mu_00 ** 2)
    mu_02_normalizado = mu_02 / (mu_00 ** 2)
    mu_11_normalizado = mu_11 / (mu_00 ** 2)
    
    # Retornar invariantes de escala
    return (mu_10_normalizado, mu_01_normalizado, mu_11_normalizado, 
            mu_20_normalizado, mu_02_normalizado)

# Rutas de las carpetas
carpeta_original = r"C:\Users\X415EA-EB757T\OneDrive\Documentos\GrafT2\Imagenes_binarias"
carpeta_escalada = r"C:\Users\X415EA-EB757T\OneDrive\Documentos\GrafT2\Imagenes_escaladas"

# Verificar si las carpetas existen
if not os.path.exists(carpeta_original):
    print(f"La carpeta '{carpeta_original}' no existe.")
    exit()
if not os.path.exists(carpeta_escalada):
    print(f"La carpeta '{carpeta_escalada}' no existe.")
    exit()

# Obtener lista de imágenes originales
archivos = [f for f in os.listdir(carpeta_original) if f.endswith(".png")]

# Verificar si hay imágenes en la carpeta original
if not archivos:
    print("No se encontraron imágenes en la carpeta original.")
    exit()

# Tabla para almacenar resultados
resultados = []

for archivo in archivos:
    ruta_original = os.path.join(carpeta_original, archivo)
    ruta_escalada = os.path.join(carpeta_escalada, archivo)

    # Verificar si la imagen escalada existe antes de procesarla
    if not os.path.exists(ruta_escalada):
        print(f"No se encontró la imagen escalada: {archivo}")
        continue

    # Cargar imágenes en escala de grises
    imagen_original = cv2.imread(ruta_original, cv2.IMREAD_GRAYSCALE)
    imagen_escalada = cv2.imread(ruta_escalada, cv2.IMREAD_GRAYSCALE)

    # Verificar si las imágenes se cargaron correctamente
    if imagen_original is None:
        print(f"No se pudo cargar la imagen original: {archivo}")
        continue
    if imagen_escalada is None:
        print(f"No se pudo cargar la imagen escalada: {archivo}")
        continue 

    # Binarizar las imágenes
    _, imagen_original = cv2.threshold(imagen_original, 127, 255, cv2.THRESH_BINARY)
    _, imagen_escalada = cv2.threshold(imagen_escalada, 127, 255, cv2.THRESH_BINARY)

    # Calcular invariantes de escala
    momentos_original = calcular_momentos_invariantes(imagen_original)
    momentos_escalada = calcular_momentos_invariantes(imagen_escalada)

    if momentos_original and momentos_escalada:
        resultados.append([archivo] + list(momentos_original) + list(momentos_escalada))

# Verificar si se obtuvieron resultados
if not resultados:
    print("No se pudieron calcular los momentos invariantes para ninguna imagen.")
    exit()

# Crear un DataFrame de Pandas
columnas = ["Imagen", 
            "mu_10 (Antes)", "mu_01 (Antes)", "mu_11 (Antes)", "mu_20 (Antes)", "mu_02 (Antes)",
            "mu_10 (Después)", "mu_01 (Después)", "mu_11 (Después)", "mu_20 (Después)", "mu_02 (Después)"]

df = pd.DataFrame(resultados, columns=columnas)

# Guardar en CSV con codificación utf-8-sig (para evitar errores en Excel)
df.to_csv("momentos_invariantes.csv", index=False, encoding="utf-8-sig")

# Mostrar el DataFrame sin problemas de codificación en Windows
print(df.to_string(index=False))