import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def generar_grafico_contornos(imagen, nombre):
    if imagen is None:
        print(f"No se puede procesar '{nombre}', imagen no cargada.")
        return
    
    # Asegurar que la imagen sea binaria
    _, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

    # Encontrar contornos con vecindad-8
    contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear imagen en blanco para dibujar los contornos
    imagen_contornos = np.zeros_like(imagen_binaria)

    # Dibujar los contornos en la imagen en blanco
    cv2.drawContours(imagen_contornos, contornos, -1, (255), 1)

    # Crear gráfico
    plt.figure(figsize=(10, 10))
    plt.imshow(imagen_contornos, cmap='binary', interpolation='nearest')
    plt.title(f"Contorno de Celdas Binarias: {nombre}")

    # Configurar cuadrícula
    plt.grid(True, color='red', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(-0.5, imagen_contornos.shape[1], 1), [])
    plt.yticks(np.arange(-0.5, imagen_contornos.shape[0], 1), [])

    # Guardar gráfico
    os.makedirs('mapas_contornos', exist_ok=True)
    plt.savefig(f'mapas_contornos/{nombre}_contorno.png')
    plt.close()

def procesar_imagenes_contornos(directorio):
    archivos = [f for f in os.listdir(directorio) if f.endswith('.png')]
    print(f"Procesando imágenes en '{directorio}': {archivos}")

    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        generar_grafico_contornos(imagen, archivo)

# Directorio de imágenes binarias
carpeta_binarias = "Imagenes_binarias"

# Procesar imágenes y generar gráficos de contornos
procesar_imagenes_contornos(carpeta_binarias)
