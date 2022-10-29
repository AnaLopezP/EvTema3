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
            pila.apilar(dato)
            return dato
        while not paux.pila_vacia():
            dato = paux.desapilar()
            print(dato)
            paux.apilar(dato)
            return dato

aguja1 = Pila()
aguja2 = Pila()
aguja3 = Pila()

'''n = 0
while n < 75:
    aguja1.apilar(n)
    n += 1'''

for i in range(1, 75):
    aguja1.apilar(i)
    #print(aguja1.apilar(i))

aguja1.barrido()