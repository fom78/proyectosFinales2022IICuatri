import os
from os import system
from Modulos.misfunciones import archivosyCarpetas, buscaJugador, informeJugadores
from Modulos.decoradores import cabecera



def main():
    ''' Proyecto Final: Distintos Juegos
        Menú Jugadores
        Opciones:
        [1] Jugar
        [2] Agregar
           DNI: 16768058
           Nombre:"Daniel F. Somoza"
           lActivo := True
           Juego1:"dados.dat"
           NroPartida: int() + 1
           AcumuPartida: int() + nPuntos
           Juego2:"pipati.dat"
           NroPartida: int() + 1
           AcumuComputadora: int() + nComputadora
           AcumuUsuario: int() + nUsuario
           AcumuEmpate: int() + nEmpates
           AcumuPartida: int() + nComutadora + nUsuario + nEmpates
        [3] Midificar Jugador
        [4] Listados de Jugadores Totales, Activos, No Activos
        [5] Activar o Desactivar Estado del Jugador
        [6] Eliminar Jugador + Todas sus partidas Jugadas
        [0] Salir
    '''
    cPath = os.getcwd() + "/"
    archivosyCarpetas()
    
    while True:
        titulo = 'Juegos "Pura Timba S.A."'
        cabecera(titulo, 1)
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Debes ingresar un número!!!")
            system("pause")
            continue
        if opcion == 0:
            break
        elif opcion == 1:
            titulo = "Menú Juegos"
            buscaJugador(titulo, 2, "J")
        elif opcion == 2:
            titulo = "Altas de Jugadores"
            buscaJugador(titulo, 3, "A")
        elif opcion == 3:
            titulo = "Modificar datos del Jugador"
            buscaJugador(titulo, 4, "M")
        elif opcion == 4:
            titulo = "Informe de Jugadores"
            informeJugadores(titulo, 5)
        elif opcion == 5:
            titulo = "Activa/Desactiva Jugador"
            buscaJugador(titulo, 6, "T")
        elif opcion == 6:
            titulo = "Eliminar Jugador"
            buscaJugador(titulo, 7, "E")
    system("cls")
    print("Salida del programa!!")

main()