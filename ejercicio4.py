
pol1 = [3, -4, 5]
pol2 = [1, 5, -3]
pol1_conx = []
pol2_conx = []

def restar_polinomios(pol1, pol2):
    pol_nuevo = []
    if len(pol1) < len(pol2):
        pass
    elif len(pol1) > len(pol2):
        pass
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
        print_term(pol, grad, i, pol1_conx)
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

pol1_conx = print_term(pol1, 2, 0, pol1_conx)
print(pol1_conx)
pol2_conx = print_term(pol2, 2, 0, pol2_conx)
print(pol2_conx)

pol3 = restar_polinomios(pol1, pol2)
print(pol3)
pol3_conx = []
pol3_conx = print_term(pol3, 2, 0, pol3_conx)
print(pol3_conx)

