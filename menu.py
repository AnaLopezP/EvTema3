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

        decision = input("> ")
        if decision == 1:
            aguja1 = ejercicio1.Pila()
            aguja2 = ejercicio1.Pila()
            aguja3 = ejercicio1.Pila()

            for i in range(0, 75):
                aguja1.apilar(i)
                print(i)

            aguja_prov = aguja1
            while aguja3.tamanio != aguja_prov.tamanio:
                ejercicio1.comparar(aguja1.cima.info, aguja2.cima.info)
                ejercicio1.añadir_discoadisco(aguja1.cima.info, aguja2.cima.info, aguja3.cima.info, aguja1, aguja2, aguja3)
        
        elif decision == 2:
            mat = ejercicio2.crear_mat(ejercicio2.matriz)
            print(mat)
            det = ejercicio2.sarrus_it(mat)
            print(det)
        
        
        helpers.limpiar_pantalla()

        input("\nPresiona ENTER  para continuar")