from ejercicio3 import Vehiculo
import ejercicio3
if __name__ == '__main__':
    lista = ejercicio3.Lista()
    dato = input("Ingresa el nombre de la nave: ")
    info = []
    a = ejercicio3.Vehiculo(dato)
    ejercicio3.Vehiculo.lista(a, info)
    print(a)
    print(info)
    while dato != '':
        ejercicio3.Lista.insertar(lista, dato)
        dato = input("Ingresa el nombre de la nave (pulsa enter para cerrar la lista): ")
        info = []
        a = ejercicio3.Vehiculo(dato)
        ejercicio3.Vehiculo.lista(a, info)
        print(a)
        print(info)


    ejercicio3.Lista.barrido(lista)