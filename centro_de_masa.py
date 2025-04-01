import cv2
import numpy as np
import os
import pandas as pd

def calcular_momentos_centrales(imagen, nombre):
    if imagen is None:
        print(f"No se puede procesar '{nombre}', imagen no cargada.")
        return None

    # Asegurar que la imagen sea binaria
    _, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

    # Calcular los momentos espaciales
    momentos = cv2.moments(imagen_binaria)

    # Centro de masa
    if momentos["m00"] == 0:  
        print(f"No se encontró objeto binario en '{nombre}'")
        return None  

    x_cm = momentos["m10"] / momentos["m00"]
    y_cm = momentos["m01"] / momentos["m00"]

    # Crear coordenadas de píxeles
    X, Y = np.meshgrid(np.arange(imagen.shape[1]), np.arange(imagen.shape[0]))

    # Calcular momentos centrales
    momentos_centrales = {}
    for p in range(3):
        for q in range(3):
            if p == 0 and q == 0:
                continue  # μ_00 no tiene sentido en momentos centrales
            momentos_centrales[(p, q)] = np.sum(
                ((X - x_cm) ** p) * ((Y - y_cm) ** q) * (imagen_binaria / 255)
            )

    return nombre, x_cm, y_cm, momentos_centrales

def procesar_imagenes(directorio):
    resultados = []
    
    archivos = [f for f in os.listdir(directorio) if f.endswith('.png')]
    
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        resultado = calcular_momentos_centrales(imagen, archivo)
        if resultado:
            resultados.append(resultado)
    
    # Crear tabla de resultados
    tabla = pd.DataFrame([
        {
            "Imagen": nombre,
            "x_cm": x_cm,
            "y_cm": y_cm,
            "mu_01": momentos[(0, 1)],
            "mu_10": momentos[(1, 0)],
            "mu_11": momentos[(1, 1)],
            "mu_20": momentos[(2, 0)],
            "mu_02": momentos[(0, 2)],
        }
        for nombre, x_cm, y_cm, momentos in resultados
    ])
    
    print(tabla)
    tabla.to_csv("momentos_centrales.csv", index=False)

# Directorio de imágenes binarias
carpeta_binarias = "Imagenes_binarias"

# Procesar imágenes y generar tabla
procesar_imagenes(carpeta_binarias)