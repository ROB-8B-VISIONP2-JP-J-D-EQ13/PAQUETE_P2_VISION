EQUIPO 13
JOAQUIN ROMO MARQUEZ
DIEGO CAMARILLO SANCHEZ
JUAN PABLO VAZQUEZ CUEVAS

PROYECTO 2: SEGMENTACIÓN Y CONTEO DE OBJETOS EN UNA BANDA O SUPERFICIE DE TRABAJO
Este proyecto consiste en una librería desarrollada en Python para segmentar, detectar y contar objetos presentes en una imagen.  
El sistema fue desarrollado utilizando técnicas básicas de visión y procesamiento digital de imágenes con OpenCV.

El programa permite:
- Cargar imágenes
- Convertir imágenes a escala de grises
- Aplicar filtrado Gaussiano
- Realizar umbralización automática con Otsu
- Detectar regiones conectadas
- Contar objetos automáticamente
- Mostrar propiedades básicas de cada objeto detectado

Librerías utilizadas

- OpenCV
- NumPy
- Matplotlib


Estructura del proyecto
PAQUETE_P2_VISION/
main.py
setup.py
requirements.txt

vision/
 __init__.py 
procesamiento.py
 conteo.py
 visualizacion.py
-----------------------------------------
Instalación
Abrir terminal en la carpeta del proyecto y ejecutar:
pip install -e .
O instalar dependencias manualmente:
pip install -r requirements.txt
------------------------------------------------------
EJECUCION
Ejecutar el archivo principal:
python main.py
Después el programa solicitará la ruta de la imagen.
Ejemplo:
C:\imagenes\tornillos.jpg

FUNCIONAMIENTO DEL SISTEMA
1. Carga de imagen
El usuario proporciona la ruta de una imagen para ser procesada.
2. Conversión a escala de grises
La imagen RGB se convierte a escala de grises para simplificar el procesamiento.
3. Filtro Gaussiano
Se aplica un filtro Gaussiano para reducir ruido y suavizar la imagen.
4. Umbralización Otsu
Se separan automáticamente los objetos del fondo usando un umbral automático.
5. Segmentación
Se detectan regiones conectadas correspondientes a cada objeto.
6. Conteo de objetos

Se cuentan los objetos detectados y se muestran sus propiedades:
- Área
- Alto
- Ancho
- Centroide
RESULTADOS
El sistema genera:
- Imágenes intermedias del procesamiento
- Imagen final con objetos detectados
- Conteo total de objetos
-----------------------------------------------------------
!!IMPORTANTE!!
LIMITACIONES
El sistema puede presentar errores cuando:
- Existen sombras fuertes
- Los objetos están pegados
- Hay reflejos intensos
- El fondo tiene colores similares al objeto
- Objetos de colores claros
- Objetos con etiqueta (en algunos casos)
Es por eso que dentro del sistema se recomienda usar fondos blancos y que los objetos sean de colores con grado de intensidad
no tan claros
Las imágenes de prueba se encuentran en la carpeta:

imagenes_prueba/
Con respecto a la carga de imagenes dentro del codigo, es necesario retirar las comillas de la direccion de acceso de la imagen.
---------------------------------------------------------------
Ejemplos utilizados
Se realizaron pruebas con:
- Tornillos
- Monedas
- Frutas
- Objetos aleatorios de casa
  
Autores
JOAQUIN ROMO MARQUEZ
DIEGO CAMARILLO SANCHEZ
JUAN PABLO VAZQUEZ CUEVAS
Ingeniería en Robótica 8°B 
VISION ROBOTICA
