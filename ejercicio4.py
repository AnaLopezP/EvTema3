
pol1 = [3, -4, 5]
pol2 = [1, 5, -3]
pol4 = [1, 2, 3, 4, 5]
pol5 = [7, 8]


def restar_polinomios(pol1, pol2):
    pol_nuevo = []
    if len(pol1) < len(pol2):
        for i in range(len(pol2)-len(pol1)):
            pol1.insert(0, 0)
        for i in range(len(pol1)):
            pol_nuevo.append(pol1[i] - pol2[i])
    elif len(pol1) > len(pol2):
        for i in range(len(pol1)-len(pol2)):
            pol2.insert(0, 0)
        for i in range(len(pol1)):
            pol_nuevo.append(pol1[i] - pol2[i])
    else:
        for i in range(len(pol1)):
            pol_nuevo.append(pol1[i] - pol2[i])
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

'''pol1_conx = []
pol1_conx = print_term(pol1, 2, 0, pol1_conx)
print(pol1_conx)
pol2_conx = []
pol2_conx = print_term(pol2, 2, 0, pol2_conx)
print(pol2_conx)

pol3 = restar_polinomios(pol1, pol2)
pol3_conx = []
pol3_conx = print_term(pol3, 2, 0, pol3_conx)
print(pol3_conx)'''

jsjs = restar_polinomios(pol1, pol4)
print(jsjs)
ahuevo = restar_polinomios(pol2, pol5)
print(ahuevo)
