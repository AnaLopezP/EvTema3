import random
#sarrus
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

#creamos una matriz aleatoria 3x3
def crear_mat(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = random.randint(0, 20)
    return matriz

