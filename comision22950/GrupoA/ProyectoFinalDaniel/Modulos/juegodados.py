from array import array
from ast import While
from os import system
import random
from Modulos.decoradores import cabeceraJuegos

def juegoDados(opcion):
    ''' Juego de Dados
        Se tiran 5 dados por ronda
        Puntuacion
        - 5 dados iguales suma 20 puntos
        - 4 dados iguales suma 12 puntos
        - 3 dados iguales y un par suma 9 puntos
        - 3 dados iguales suma 6 puntos
        - 2 pareas de dados iguales suma 5 puntos
        - 1 par de dados iguales suma 2 puntos
        Se juegan 5 rondas
    '''
    while True:
        cabeceraJuegos(opcion)
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Debes ingresar un número!!!")
            system("pause")
            continue
        if opcion == 0:
            break
        elif opcion == 1:
            jugarDados(1)
            break
        elif opcion == 2:
            jugarDados(2)
            break
    return None

def jugarDados(opciones):
    if opciones == 1:
        cantidadDeJugadas = 5
        cantidadDeDados = 5
        rondasJugadas = range(cantidadDeJugadas)
        cantidadDados = range(cantidadDeDados)
        sumaAcumulada = 0
        suma_Punto = []
        suma_Acumulada = []
        renglon = "|             " 
        jugada  = "|Jugada Nro: "
        dicRonda = {}
        primero = True
        for ronda in rondasJugadas:
            listValorDado = []
            for dado in cantidadDados:
                if primero:
                    renglon += "| Dado Nro: " + str(dado + 1) + " " 
                listValorDado.append(random.randint(1, 6))
            primero = False
            dicRonda[ronda + 1] = listValorDado
            listValorDado.sort()
            nVeces = 0
            indice = 0
            tresIguales = False
            dosIguales = 0
            sumaPunto = 0
            while indice < len(listValorDado):
                nElemento = listValorDado[indice]
                nVeces = listValorDado.count(nElemento)
                if nVeces%5 == 0:   ## 5 dados iguales
                    sumaPunto+= 20
                elif nVeces%4 == 0: ## 4 dados iguales
                    sumaPunto+= 12
                elif nVeces%3 == 0: ## 3 dados iguales
                    sumaPunto+= 6
                    tresIguales = True
                elif nVeces%2 == 0: ## 2 dados iguales
                    sumaPunto+= 2
                    dosIguales += 1
                indice += nVeces

            if dosIguales == 1:
                if tresIguales:
                    sumaPunto+= 3
            elif dosIguales == 2:
                sumaPunto+=1
            elif dosIguales == 3:
                sumaPunto+= 1
            sumaAcumulada+= sumaPunto
            suma_Punto.append(sumaPunto)
            suma_Acumulada.append(sumaAcumulada)
        renglon += "|    Puntos   | Acumulado  "
        print("-"*112)
        print(renglon + "|")
            
        for i in range(len(dicRonda)):
            print(jugada + str(i+1), end="")
            for dado in dicRonda[i+1]:
                print(f'|     {dado}      ', end=" ")
            print(f'|{suma_Punto[i]:^12.0f}', end=" ")
            print(f'|{suma_Acumulada[i]:^12.0f}|')   
        print("")
        print("-"*46, end="")
        print("-> by  DFSistemas <-", end="")
        print("-"*46)
        system("Pause")
    elif opciones == 2:
            titulo = "Estadísticas Juego de Dados"
    return None    

