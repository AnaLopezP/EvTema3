import random

class nodoLista(object):
    '''
    Clase nodo lista
    '''
    info, sig = None, None #Información y siguiente
    
class Lista(object):
    #Clase de la lista simplemente enlazada
    def __init__(self):
        #Crea una lista vacía
        self.inicio = None #apunta al nodo que está al principio de la lista
        self.tamanio = 0 #Cantidad de lista.inicios lista
        
    def insertar (lista, dato, campo = None):
        '''
        Agrega el lista.inicio a la lista de manera ordenada
        '''
        nodo = nodoLista()
        nodo.info = dato #le pasamos dato q queremos añadir
        if (lista.inicio is None) or (Lista.criterio(lista.inicio.info, campo) > Lista.criterio(dato, campo)): #Mira si el lista.inicio que queremos añadir es el primero de la lista o es menor q el primero

            nodo.sig = lista.inicio #Se le asigna al siguiente del creado el inicio de la lista
            lista.inicio = nodo #Al inicio de la lista se le asigna la direción del nodo creado
        
        #Cuando es un dato que va a estar en medio o en el final de la lista
        else: #Se usan ant y act para barrer la lista y ver dónde vamos a colocar el dato
            ant = lista.inicio #anterior 
            act = lista.inicio.sig #actual
            while act is not None and Lista.criterio(act.info, campo) < Lista.criterio(dato, campo) : #Recore la lista para colocar dato
                ant = ant.sig
                act = act.sig 
            nodo.sig = act #Reconstruimos el enlace de los nodos
            ant.sig  = nodo
        lista.tamanio += 1
        return lista
    
    def lista_vacia(lista):
        '''
        Devuelve True si está vacía
        '''
        return lista.inicio is None
    
    def eliminar(lista, clave, campo = None):
        '''
        Elimina in lista.inicio de la lista y lo devulve si lo encuentra
        '''
        dato = None
        if Lista.criterio(lista.inicio.info, campo) == Lista.criterio(clave, campo): #Si el lista.inicio que queremos eliminar es el primero de la lista
            dato = lista.inicio.info #se saca el nodo que está al principio y lo almacenamos en dato
            lista.inicio = lista.inicio.sig #Reasignamos la primera posición al nodo siguiente
            lista.tamanio -= 1
        
        else: #El lista.inicio NO esá al principio de la lista
            anterior = lista.inicio #Asignamos los nodos para recorrer la lista y ver dónde está
            actual = lista.inicio.sig
            while actual is not None and Lista.criterio(actual.info, campo) != Lista.criterio(clave, campo):
                anterior = anterior.sig
                actual = actual.sig
            if actual is not None: #hemos encontrado el valor
                dato = actual.info #Almacenamos dicho valor en dato
                anterior.sig = actual.sig #Reconstruimos enlace
                lista.tamanio -=1
        return lista
    
    def tamanio(lista):
        '''
        Devuelve el número de lista.inicios de la lista
        '''
        return lista.tamanio
    
    def buscar(lista, buscado, campo= None):
        '''
        Devuelve la dirección del lista.inicio buscado
        '''
        aux = lista.inicio #Puntero auxiliar, que se le asigna la primera posición de la lista
        while aux is not None and aux.info != buscado: #Buscamos dato
            aux = aux.sig #hasta que no le encontremos iremos reasignando el valor de aux
        return aux

    def barrido(lista):
        '''
        Realiza un barrido de la lista, mostrando sus valores
        '''
        aux = lista.inicio
        while aux is not None:
            print(aux.info)
            aux = aux.sig
    
    def criterio(dato, campo = None):
        '''
        Determina con que debemos de comparar el dato
        ''' 
        dic = {}
        if hasattr(dato, '__dict__'):
            dic = dato.__dict__
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]

class Vehiculo(Lista):
    def __init__(self, nombre):
        self.nombre = nombre
        self.largo = random.randint(10, 100) #en metros
        self.tripulacion = random.randint(2, 10)
        self.num_pasajeros = random.randint(20, 50)
        super().__init__()

        if self.nombre == 'Estrella de la Muerte':
            print("HAS DADO CON LA ESTRELLA DE LA MUERTE")
            self.largo = 34.37
            self.tripulacion = 1381669
            self.num_pasajeros = 100000
        if self.nombre == 'Halcón Milenario':
            print("HAS DADO CON EL HALCÓN MILENARIO")
            self.largo = 34.75
            self.tripulacion = 4
            self.num_pasajeros = 3
    
    def lista(self, lista):
        lista.append(self.nombre)
        lista.append(self.largo)
        lista.append(self.tripulacion)
        lista.append(self.num_pasajeros)
        return lista

    def __str__(self) -> str:
        return "El vehiculo con nombre " + str(self.nombre) + " tiene un largo de " + str(self.largo) + " una tripulacion de " + str(self.tripulacion) + " y un numero de pasajeros " + str(self.num_pasajeros)


lista = Lista()
toda_info = []
dato = input("Ingresa el nombre de la nave: ")
info_lista = []
a = Vehiculo(dato)
Vehiculo.lista(a, info_lista)
toda_info.append(info_lista)
print(a)
while dato != '':
    Lista.insertar(lista, dato)
    dato = input("Ingresa el nombre de la nave: ")
    info_lista = []
    a = Vehiculo(dato)
    Vehiculo.lista(a, info_lista)
    toda_info.append(info_lista)
    print(a)

toda_info.pop(-1)
Lista.barrido(lista)

def ordenar_pasajeros(lis, filtro):
    i = 0
    control = True
    while i <= len(lis) - 2 and control:
        control = False
        for j in range(len(lis)-i-1):
            if lis[j][filtro] < lis[j + 1][filtro]:
                lis[j], lis[j + 1] = lis[j +1], lis[j]
                control = True
        i = i + 1
    return lis


list_ordenada = ordenar_pasajeros(toda_info, 3)
print("LAS NAVES CON EL MAYOR NUMERO DE PASAJEROS")
if len(info_lista) < 5:
    for i in range(len(list_ordenada)):
        print(str(list_ordenada[i][0]) + " con " + str(list_ordenada[i][3]) + " pasajeros")
else:
    for i in range(0, 5):
        print(str(list_ordenada[i][0]) + " con " + str(list_ordenada[i][3]) + " pasajeros")

list_ordenada_tamaño = ordenar_pasajeros(toda_info, 1)
print("La nave que requiere mayor numero de tripulacion es:")
print((list_ordenada_tamaño[0][0]) + " con un tamaño de " + str(list_ordenada_tamaño[0][1])) 

si_at = []
def at():
    if "AT" in str(lista.inicio.info):
        print(lista.inicio.info)
        si_at.append(lista.inicio.info)
        Lista.eliminar(lista.inicio.info)
        #lista.inicio.sig = lista.inicio
        at()
    else:
        print(lista.inicio.info)
        Lista.eliminar(lista.inicio.info)
        #lista.inicio.sig = lista.inicio
        at()
    return si_at

while lista.lista_vacia != True:
    at()
    lista.lista_vacia()
    

