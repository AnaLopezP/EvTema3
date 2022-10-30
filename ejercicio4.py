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

def eliminar(pol, term):
    for i in range(len(pol)):
        if pol[i] == term:
            pol.pop(i)
            return pol
    return "No esta en el polinomio"
    

pol1 = crear_polinomio()
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
elegir = input("Introduzca un polinomio de los anteriores para eliminar uno de sus elementos: ")
elim = input("Introduzca un elemento a eliminar: ")
pol_nuevo = eliminar(elegir, elim)
print(pol_nuevo)
