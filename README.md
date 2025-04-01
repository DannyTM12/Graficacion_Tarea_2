# Proyecto: Análisis de Objetos Binarios con Momentos Invariantes y Transformaciones Morfológicas

Este repositorio contiene el código y los resultados del análisis de objetos binarios mediante técnicas de procesamiento de imágenes. El proyecto incluye el cálculo de momentos invariantes de Hu, centro de masa, momentos centrales, transformaciones geométricas y operaciones morfológicas, así como la generación de reportes en formato CSV y PDF.

## Contenido del repositorio

- **Carpeta `imagenes_binarias/`**: Contiene las imágenes en formato binario utilizadas en el análisis.
- **Carpeta `resultados/`**: Contiene las carpetas generadas con los resultados de cada procesamiento, incluyendo las transformaciones y los gráficos.
- **Archivos `.py`**: Programas en Python desarrollados para el procesamiento de las imágenes:
  - `centro_de_masa.py`: Cálculo del centro de masa y momentos centrales.
  - `momentos_hu.py`: Cálculo de los tres primeros momentos invariantes de Hu.
  - `transformaciones.py`: Aplicación de rotaciones y transformaciones morfológicas.
  - `generar_csv.py`: Generación de archivos CSV con los resultados obtenidos.
  - `graficos.py`: Generación de gráficos para visualizar los resultados.
- **Archivos `.csv`**: Archivos con los resultados numéricos obtenidos en cada etapa del análisis.
- **Reporte en PDF**: Documento con la explicación del procedimiento, resultados y conclusiones.

## Requisitos
Para ejecutar los programas en Python, se requieren las siguientes bibliotecas:
```sh
pip install numpy pandas opencv-python matplotlib
```

## Uso
Ejecutar cada archivo de la siguiente manera:
```sh
python centro_de_masa.py
python momentos_hu.py
python transformaciones.py
python generar_csv.py
python graficos.py
```
Los resultados se guardarán en la carpeta `resultados/` y los datos en los archivos CSV correspondientes.

## Contacto
Para cualquier consulta sobre este proyecto, contactar al desarrollador a través de este repositorio.

---
**Repositorio creado para documentar y almacenar los resultados del análisis de objetos binarios mediante técnicas de procesamiento de imágenes.**

