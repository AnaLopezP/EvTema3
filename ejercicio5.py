import ejercicio3


def crear_tabla(tamanio):
    #Creamos una tabla vacia
    tabla = [None] * tamanio #La tabla tiene todos los elementos none
    return tabla


def cantidad_elementos(tabla):
    #Devuelve la cantidad de elementos que no son nulos
    return len(tabla) - tabla.count(None)



def funcion_hash(dato):
    #Determina la posicion del dato en la tabla
    '''El objetivo de esta funcion es, que para cada dato, haya un codigo único (al menos, intentamos que lo sea)
    para que sea más fácil y rápido buscar el valor del dato en la tabla.
    Por ejemplo: si queremos buscar un nombre con apellidos, en vez de pasarle el nombre, que puede haber cientos, le pasas el código, que va a ser más exclusivo
    En este caso, el codigo es el resto de la longitud de la palabra (menos los espacios) entre el tamaño de la tabla.'''
    lista = []
    for i in range(len(dato)):
        lista.append(dato[i])
    for i in range(len(lista)):
        if ord(lista[i]) < 62:
            nueva_letra = chr(ord(lista[i]) + 4) + chr(ord(lista[i]) + 5) + chr(ord(lista[i]) + 6) + chr(ord(lista[i])  + 7) + chr(ord(lista[i])  + 8) + chr(ord(lista[i]) +9) +chr(ord(lista[i]) +10)+ chr(ord(lista[i]) +11)
        else:
            nueva_letra = chr(ord(lista[i]) - 4) + chr(ord(lista[i]) - 5) + chr(ord(lista[i]) - 6) + chr(ord(lista[i]) -7) + chr(ord(lista[i]) -8) + chr(ord(lista[i]) -9) +chr(ord(lista[i]) -10)+ chr(ord(lista[i]) -11)
        print(nueva_letra)
    return nueva_letra
        



def agregar(tabla, dato):
    #agregamos un elemento a la tabla encadenada
    posicion = funcion_hash(dato, len(tabla)) #usamos la funcion anterior para determinar la posicion mediante el codigo
    if (tabla[posicion]) is None: 
        tabla[posicion] = ejercicio3.Lista() #Si no ha habido anteriormente un elemento con ese dato, en vez de añadirlo a la lista que contiene el mismo codigo, la creamos 
    ejercicio3.Lista.insertar(tabla[posicion], dato) #Si la lista ya existe, lo añade como un elemento mas


def buscar(tabla, buscado):
    #determina si un elemento exsiste en la tabla y devuelve la posicion
    pos = None
    posicion = funcion_hash(buscado, len(tabla)) #determinamos el codigo del dato buscado
    if tabla[posicion] is not None: #Para ver si existe ese dato en la tabla
        pos = ejercicio3.Lista.buscar(tabla[posicion], buscado) #usamos una funcion extra para buscar el elemento en la lista
    return pos


def quitar(tabla, dato):
    #Quita un elemento de la tabla encadenada si existe
    dato = None
    posicion = funcion_hash(dato, len(tabla)) #determinamos la posicion del dato
    if tabla[posicion] is not None: #si la lista existe
        dato = ejercicio3.Lista.eliminar(tabla[posicion], dato) #eliminamos el dato de la lista
        if ejercicio3.Lista.lista_vacia(tabla[posicion]): #si no hay mas datos en la lista
            tabla[posicion] = None #igualamos la lista a None (borramos la lista)
    return dato
tabla1 = crear_tabla(93)
tabla2 = crear_tabla(93)
#agregar(tabla1, 'hola')
funcion_hash('Perra Sarnosa')