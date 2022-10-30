pol1 = [3, -4, 5]
pol2 = [1, 5, -3]
pol1_conx = []

def restar_polinomios(pol1, pol2):
    pass

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

def polinomio(lista):
        for i in lista:
            lista[i] = int(lista[i])
            print(lista[i])
        result = sum(lista)
        return result

pol1_conx = print_term(pol1, 2, 0, pol1_conx)
print(pol1_conx)
pol1_bien = polinomio(pol1_conx)
print(pol1_bien)



