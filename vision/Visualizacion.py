import matplotlib.pyplot as plt

#Ploteo del proceso
def mostrar_proceso(img_rgb, gray, blur, bordes, binaria):
    plt.figure(figsize=(15,10))

    #Original
    plt.subplot(2,3,1)
    plt.imshow(img_rgb)
    plt.title("Imagen original")
    plt.axis('off')

    #Grises
    plt.subplot(2,3,2)
    plt.imshow(gray, cmap='gray')
    plt.title("Escala de grises")
    plt.axis('off')

    #Blur
    plt.subplot(2,3,3)
    plt.imshow(blur, cmap='gray')
    plt.title("Filtro Blur Gauss")
    plt.axis('off')

    #Bordes
    plt.subplot(2,3,4)
    plt.imshow(bordes, cmap='gray')
    plt.title("Bordes")
    plt.axis('off')
    #Umbral Otsu
    plt.subplot(2,3,5)
    plt.imshow(binaria, cmap='gray')
    plt.title("Umbral Otsu")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
#Resultado
def mostrar_resultado(resultado, conteo):
    plt.figure(figsize=(8,8))
    plt.imshow(resultado)
    plt.title(f"Objetos detectados: {conteo}")
    plt.axis('off')
    plt.show()