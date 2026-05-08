import cv2

def cargar_imagen(ruta):
    img = cv2.imread(ruta)
    return img
#Convertir imagen a RGB
def convertir_rgb(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb
#Escala de grises
def convertir_grises(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

#Filtro Gauss
def aplicar_blur(gray, kernel):
    blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)
    return blur
#Umbral Otsu
def umbral_otsu(blur):
    _, binaria = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return binaria
#Bordes
def detectar_bordes(blur):
    bordes = cv2.Canny(blur, 100, 200)
    return bordes