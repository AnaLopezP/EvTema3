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
        helpers.limpiar_pantalla()

        input("\nPresiona ENTER  para continuar")