def crear_polinomio():
    pol = []
    termino = input("Introduzca numero para el termino: ")
    pol.append(termino)
    while termino != '':
        termino = input("Introduzca numero para el termino: ")
        pol.append(termino)
    pol.pop(-1)
    return pol
    


def restar_polinomios(pol1, pol2):
    pol_nuevo = []
    if len(pol1) < len(pol2):
        for i in range(len(pol2)-len(pol1)):
            pol1.insert(0, 0)
        for i in range(len(pol1)):
            pol_nuevo.append(int(pol1[i]) - int(pol2[i]))
    elif len(pol1) > len(pol2):
        for i in range(len(pol1)-len(pol2)):
            pol2.insert(0, 0)
        for i in range(len(pol1)):
            pol_nuevo.append(int(pol1[i]) - int(pol2[i]))
    else:
        for i in range(len(pol1)):
            pol_nuevo.append(int(pol1[i]) - int(pol2[i]))
    return pol_nuevo

def print_term(pol, grad, i, lista):
    ing = "x"
    if i < len(pol):
        term = str(pol[i]) + str(ing) + "^" + str(grad)
        lista.append(term)
        i = i + 1
        grad = grad - 1
        print_term(pol, grad, i, lista)
        return lista
    else:
        pass

def polinomio(lista, len):
    cont = 0
    if cont < len:
        resultado = str(lista[cont]) + " + " +str(lista[cont + 1])
        cont = cont + 1
        print(resultado)
    else:
        resultado = resultado + str(lista[-1])
        print(resultado)
    return resultado

def buscar(pol, term):
    for i in range(len(pol)):
        if pol[i] == term:
            return True
    return "No esta en el polinomio"


def eliminar(pol, grado):
    pol = list(reversed(pol))
    pol.pop(int(grado))
    pol = list(reversed(pol))
    return pol
        
    

'''pol1 = crear_polinomio()
print(pol1)
y1 = []
y1 = print_term(pol1, len(pol1)-1, 0, y1)
print("y1 es " + str(y1))
pol2 = crear_polinomio()
print(pol2)
y2 = []
y2 = print_term(pol2, len(pol2)-1, 0, y2)
print("y2 es " + str(y2))
pol3 = restar_polinomios(pol1, pol2)
print(pol3)
y3 = []
y3 = print_term(pol3, len(pol3)-1, 0, y3)
print("y3 es " + str(y3))
print("Introduzca un numero para eliminar un valor del polinomio correspondiente: ")
elegir = int(input())
if elegir == 1:
    elim = input("Introduzca el grado del elemento a eliminar: ")
    pol_nuevo = eliminar(y1, elim)
elif elegir == 2:
    elim = input("Introduzca el grado del elemento a eliminar: ")
    pol_nuevo = eliminar(y2, elim)
elif elegir == 3:
    elim = input("Introduzca el grado del elemento a eliminar: ")
    pol_nuevo = eliminar(y3, elim)
else:
    print("Ese polinomio no existe")

print(pol_nuevo)'''
