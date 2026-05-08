from vision.Prosesamiento import *
from vision.Conteo import *
from vision.Visualizacion import *

ruta = input("Indique la ruta de la imagen: ")
img = cargar_imagen(ruta)
#Convertir RGB
img_rgb = convertir_rgb(img)
#Escala de grises
gray = convertir_grises(img)
#Blur gauss
blur = aplicar_blur(gray, 5)
#Bordes
bordes = detectar_bordes(blur)
#umbral
binaria = umbral_otsu(blur)

#Proceso
mostrar_proceso(
    img_rgb,
    gray,
    blur,
    bordes,
    binaria
)
#Conteo
resultado, conteo = contar_objetos(
    binaria,
    img_rgb
)
#Resultado
mostrar_resultado(
    resultado,
    conteo
)