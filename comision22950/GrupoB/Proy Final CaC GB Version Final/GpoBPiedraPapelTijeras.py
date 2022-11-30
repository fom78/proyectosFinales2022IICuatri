from ast import If
from random import randint
def JuegoPPYJ():
    resultado = ""
    print("------------------------------------------")
    print("elegir piedra:(1), papel:(2),o tijera:(3) ")
    print("------------------------------------------")
    opcion=int(input("\tIngrese una Opcion  ".upper()))
    print("------------------------------------------")
    pcopcion=randint(1,3)
    if opcion==pcopcion:
        print("\tEmpate")
        print("------------------------------------------")
        resultado = "E"
    else:
        # Piedra
        if opcion==1:
            # Papel
            if pcopcion==2:
                print("\tGana Computadora, Papel mata a piedra")
                print("------------------------------------------")
                resultado ="Pc"
            else:
                print("\tGanaste, Piedra mata a Tijeras")
                print("------------------------------------------")
                resultado ="Us"
        else:
            # Papel
            if opcion==2:
            # Tijeras
                if pcopcion ==3:
                    print("\tGana Computadora, Tijeras mata a Papel")
                    print("------------------------------------------")
                    resultado = "Pc"
                else:
                    print("\tGanaste, Papel mata a Piedra")
                    print("------------------------------------------")
                    resultado = "Us"
            else:
                # Tijeras
                if opcion==3:
                    # Piedra
                    if pcopcion==1:
                        print("\tGana Computadora, Piedra mata a Tijeras")
                        print("------------------------------------------")
                        resultado = "Pc"
                    else:
                        print("\tGanaste, Tijeras mata a Papel")
                        print("------------------------------------------")
                        resultado = "Us"
    print("\tGracias".upper())
    print("------------------------------------------")
    return resultado
 