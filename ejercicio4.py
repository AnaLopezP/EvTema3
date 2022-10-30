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
        
    


