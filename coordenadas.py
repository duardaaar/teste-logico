import math


def calcular_distancia(ponto1, ponto2):

    # desempacotando as coordenadas dos pontos

    x1, y1 = ponto1
    x2, y2 = ponto2

    # calculando a distância euclidiana

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

ponto1 = (float(input("Digite a coordenada x do primeiro ponto: ")), float(input("Digite a coordenada y do primeiro ponto: ")))
ponto2 = (float(input("Digite a coordenada x do segundo ponto: ")), float(input("Digite a coordenada y do segundo ponto: ")))


distancia = calcular_distancia(ponto1, ponto2)
print(f"A distância euclidiana entre os pontos é {distancia:.2f}")