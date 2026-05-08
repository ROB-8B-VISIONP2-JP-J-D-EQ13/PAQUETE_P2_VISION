import cv2

def contar_objetos(binaria, img_rgb):

    #Invertir imagen
    binaria_inv = cv2.bitwise_not(binaria)

    #Componentes conectados
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binaria_inv,
        4
    )

    resultado = img_rgb.copy()

    conteo = 0

    print("OBJETOS DETECTADOS")

    for i in range(1, num_labels):

        x, y, ancho, alto, area = stats[i]

        #Filtrar ruido
        if area > 500:

            conteo += 1

            #Información
            print(f"Objeto {conteo}")
            print(f" Area = {area}")
            print(f" Ancho = {ancho} pix")
            print(f" Alto = {alto} pix")

    print(f"Total de objetos detectados: {conteo}")

    return resultado, conteo