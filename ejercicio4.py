'''def crear_polinomio():
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
'''


class Nodo(object):
    info, sig = None, None
    
class datoPolinomio(object):
    
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1
    
    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if termino > polinomio.grado:
            aux.sig = polinomio.termino_mayor
            while actual.sig is not None and termino < actual.sig.info.termino:
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux
    def modificar_termino(polinomio, termino, valor):
        aux = polinomio.termino_mayor
        while aux is not None and aux.info.termino != termino:
            aux = aux.sig
        aux.info.valor = valor
    
    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while aux is not None and aux.info.termino > termino:
            aux = aux.sig
        if aux is not None and aux.info.termino == termino:
            return aux.info.valor
        else: 
            return 0
    
    def sumar (polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor(polinomio2, i)
            if total != 0:
                Polinomio.agregar_termino(paux, i , total)
        return paux
    
    def multiplicar(polinomio1, polinomio2):
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while pol1 is not None:
            pol2 = polinomio2.termino_mayor
            while pol2 is not None:
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if Polinomio.obtener_valor(paux, termino) != 0:
                    valor += Polinomio.obtener_valor(paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux