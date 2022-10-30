import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio5
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("QUE EJERCICIO QUIERES VER:")
        print("[1] Ejercicio 1")
        print("[2] Ejercicio 2")
        print("[3] Ejercicio 3")
        print("[4] Ejercicio 4")
        print("[5] Ejercicio 5")
        print("[6] Ninguno")

        decision = int(input("> "))
        if decision == 1:
            aguja1 = ejercicio1.Pila()
            aguja2 = ejercicio1.Pila()
            aguja3 = ejercicio1.Pila()

            for i in range(0, 75):
                aguja1.apilar(i)

            ejercicio1.jugar(aguja1.cima.info, aguja1, aguja2, aguja3)
        
        if decision == 2:
            mat = ejercicio2.crear_mat(ejercicio2.matriz)
            print(mat)
            det = ejercicio2.sarrus_it(mat)
            print(det)

        if decision == 3:
            lista = ejercicio3.Lista()
            toda_info = []
            dato = input("Ingresa el nombre de la nave: ")
            info_lista = []
            a = ejercicio3.Vehiculo(dato)
            ejercicio3.Vehiculo.lista(a, info_lista)
            toda_info.append(info_lista)
            print(a)
            while dato != '':
                ejercicio3.Lista.insertar(lista, dato)
                dato = input("Ingresa el nombre de la nave: ")
                info_lista = []
                a = ejercicio3.Vehiculo(dato)
                ejercicio3.Vehiculo.lista(a, info_lista)
                toda_info.append(info_lista)
                print(a)

            toda_info.pop(-1)
            ejercicio3.Lista.barrido(lista)

            list_ordenada = ejercicio3.ordenar_pasajeros(toda_info, 3)
            print("LAS NAVES CON EL MAYOR NUMERO DE PASAJEROS")
            if len(info_lista) < 5:
                for i in range(len(list_ordenada)):
                    print(str(list_ordenada[i][0]) + " con " + str(list_ordenada[i][3]) + " pasajeros")
            else:
                for i in range(0, 5):
                    print(str(list_ordenada[i][0]) + " con " + str(list_ordenada[i][3]) + " pasajeros")

            list_ordenada_tamaño = ejercicio3.ordenar_pasajeros(toda_info, 1)
            print("La nave que requiere mayor numero de tripulacion es:")
            print((list_ordenada_tamaño[0][0]) + " con un tamaño de " + str(list_ordenada_tamaño[0][1])) 

            si_at = []
            print("lista que empiza por AT:")
            print(ejercicio3.at(lista, si_at))

            print("Las naves que llevan seis o más pasajeros:")
            nvs_6omas = []
            for i in range(len(list_ordenada)):
                if list_ordenada[i][3] >= 6:
                    nvs_6omas.append(list_ordenada[i])
                else:
                    pass
            print(nvs_6omas)

            print("La nave más grande es: ")
            print(list_ordenada_tamaño[0])
            print("La nave más pequeña es:")
            print(list_ordenada_tamaño[-1])


        if decision == 4:
            pol1 = ejercicio4.crear_polinomio()
            print(pol1)
            y1 = []
            y1 = ejercicio4.print_term(pol1, len(pol1)-1, 0, y1)
            print("y1 es " + str(y1))
            pol2 = ejercicio4.crear_polinomio()
            print(pol2)
            y2 = []
            y2 = ejercicio4.print_term(pol2, len(pol2)-1, 0, y2)
            print("y2 es " + str(y2))
            pol3 = ejercicio4.restar_polinomios(pol1, pol2)
            print(pol3)
            y3 = []
            y3 = ejercicio4.print_term(pol3, len(pol3)-1, 0, y3)
            print("y3 es " + str(y3))
            print("Introduzca un numero para eliminar un valor del polinomio correspondiente: ")
            elegir = int(input())
            if elegir == 1:
                elim = input("Introduzca el grado del elemento a eliminar: ")
                pol_nuevo = ejercicio4.eliminar(y1, elim)
            elif elegir == 2:
                elim = input("Introduzca el grado del elemento a eliminar: ")
                pol_nuevo = ejercicio4.eliminar(y2, elim)
            elif elegir == 3:
                elim = input("Introduzca el grado del elemento a eliminar: ")
                pol_nuevo = ejercicio4.eliminar(y3, elim)
            else:
                print("Ese polinomio no existe")
            print(pol_nuevo)
        
        if decision == 5:
            pass

        #helpers.limpiar_pantalla()

        input("\nPresiona ENTER  para continuar")

iniciar()