class NodoPila:
    info, sig = None, None 

class Pila(object):
    def __init__(self):
        self.cima = None 
        self.tamanio = 0 
    
    def apilar(pila, dato):
        nodo = NodoPila() 
        nodo.info = dato 
        nodo.sig = pila.cima 
        pila.cima = nodo 
        pila.tamanio += 1
        return nodo 

    def desapilar(pila):
        x = pila.cima.info 
        pila.cima = pila.cima.sig 
        pila.tamanio -= 1 
        return x
    
    def pila_vacia(pila):
        return pila.cima == None

    def en_cima(pila):
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None
    def tamaño(pila):
        return pila.tamaño


    def barrido(pila):
        paux = Pila()
        while not pila.pila_vacia():
            dato = pila.desapilar()
            print(dato)
            paux.apilar(dato)
            return dato
        while not paux.pila_vacia():
            dato = paux.desapilar()
            print(dato)
            pila.apilar(dato)
            return dato

aguja1 = Pila()
aguja2 = Pila()
aguja3 = Pila()

def añadir(num):
    if num < 75:
        aguja1.apilar(num)
        print(aguja1.en_cima)
        añadir(num + 1)
    else:
        pass

añadir(1)
#El disco mas pequeño es el que corresponde al numero 74
#El mas grande es el 1

def comparar(num1, num2):
    if num1 > num2:
        print("El disco es más pequeño que el que hay, por lo tanto, se puede poner encima")
        return True
    elif num2 == None:
        #El numero 2 es none, es decir, en la cima de la pila no hay ningun disco todavia
        return True
    else:
        print("El disco es más grande que el que hay, no se puede poner encima, lo ponemos en otra aguja")
        return False

def añadir_discoadisco(num1, num2, num3, aguja_inicial, aguja_quequiero, aguja_quesobra):
    if comparar(num1, num2) == True:
        #Me añades el disco a la aguja que teniamos prevista
            aguja_inicial.desapilar(num1)
            aguja_quequiero.apilar(num1)
    elif comparar(num1, num2) == False:
        aguja_inicial.desapilar(num1)
        comparar(num1, num3)
        if comparar(num1, num3) == True:
            aguja_inicial.desapilar(num1)
            aguja_quesobra.apilar(num1)

aguja_prov = aguja1
while aguja3.tamanio != aguja_prov.tamanio:
    comparar(aguja1.cima.info, aguja2.cima.info)
    añadir_discoadisco(aguja1.cima.info, aguja2.cima.info, aguja3.cima.info, aguja1, aguja2, aguja3)

