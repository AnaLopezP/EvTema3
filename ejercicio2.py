
#sarrus
matriz = [
    [2, 3, 5],
    [4, 6, 8],
    [7, 9, 1]
]


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
'''def sarrus_rec(matriz):
    suma = 0
    if len(matriz) == 2 and len(matriz[0]) == 2:
        suma = matriz[0][0] * matriz[1][1] - matriz[1][0] *matriz[0][1]
    else:
        for i in range(len(matriz)):
            copia = matriz
            copia.remove(matriz[0])
            for j in range(len(copia)):
                copia[j] = copia[j][0:i] + copia[j][i + 1:]
            suma += (-1) ** (i%2)*matriz[0][i] *sarrus_rec(copia)
        return suma'''

