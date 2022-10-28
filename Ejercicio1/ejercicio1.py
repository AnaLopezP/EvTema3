class NodoPila:
    info, sig = None, None #Cuando definimos la clase, los valores iniciales siempre son none
    #Atributos: INFORMACION, SIGUIENTE

class Pila(object):
    def __init__(self):
        #Creamos una pila vacía
        self.cima = None #Puntero que apunta al nodo que está en la cima de la pila
        self.tamanio = 0 #Tamaño de la pila.
    
    def apilar(pila, dato):
        #apila un dato en la cima dela pila
        nodo = NodoPila() #Cuando queremos apilar un nuevo elemento, creamos una variable del tipo NodoPila.
        nodo.info = dato #Como su informacion metemos el valor del elemento ingresado como dato
        nodo.sig = pila.cima #Aqui se le guarda la dirección de referencia de la cima
        pila.cima = nodo #Se le asigna la direccion del nodo creado
        pila.tamanio += 1 #Aumentamos el tamaño

    def desapilar(pila):
        #Desapila el elemento que se situa en la cima y lo devuelve
        x = pila.cima.info #Almacenamos en una variable auxiliar la informacion del nodo en la cima
        pila.cima = pila.cima.sig #Ponemos en la cima de la pila el dato siguiente
        pila.tamanio -= 1 #Le quitamos uno al tamaño
        return x
    
    def pila_vacia(pila):
        #Devuelve true si la pila está vacía
        return pila.cima == None

    def en_cima(pila):
        #Devualve el valor almacenado en la cima de la pila
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None
    def tamaño(pila):
        #Devuelve el numero de elementos en la pila
        return pila.tamaño


    def barrido(pila):
        #Muestra el contenido de una pila sin perder datos
        #creamos una pila adicional llamada paux, donde vamos a reapilar los datos de la pila principal. 
        #Vamos sacando uno por uno los datos de la pila y damos su valor, luego los metemos a paux
        #cuando terminamos, desapilamos paux y los volvemos a meter a la primera pila
        paux = Pila()
        while not paux.pila_vacia():
            dato = paux.desapilar()
            print(dato)
            paux.apilar(paux, dato)
            return dato
        while not paux.pila_vacia():
            dato = paux.desapilar()
            print(dato)
            paux.apilar(pila, dato)
            return dato

aguja1 = Pila()
aguja2 = Pila()
aguja3 = Pila()

n = 0
while n < 75:
    aguja1.apilar(n)
    print(n)
    n += 1

aguja1.barrido()