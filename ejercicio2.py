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

#funcion de sarrus iterativa
def sarrus_it(matriz):
    element1 = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[1][0]*matriz[2][1]*matriz[0][2]) + (matriz[0][1]*matriz[1][2]*matriz[2][0])
    element2 = (matriz[0][2]*matriz[1][1]*matriz[2][0]) + (matriz[1][2]*matriz[2][1]*matriz[0][0]) + (matriz[0][1]*matriz[1][0]*matriz[2][2])
    print("EL DETERMINANTE DE ESTA MATRIZ ES:")
    determinante = element1 - element2
    return determinante

'''mat = crear_mat(matriz)
print(mat)
det = sarrus_it(mat)
print(det)'''

#funcion de sarrus recursiva
def sarrus_rec():
    pass
