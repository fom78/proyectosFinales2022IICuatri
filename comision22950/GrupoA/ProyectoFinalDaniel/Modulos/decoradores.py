from os import system

def cabecera(titulo, opciones):
    system("cls")  # Limpia la consola
    print("#"*42, end='->')
    print(titulo, end='<-')
    print("#"*43, end='')
    if opciones == 1:
        print('''
            [1] Ingreso al menú de Juegos
            [2] Altas de Jugadores
            [3] Modifica datos del Jugador
            [4] Listado de Jugadores Totales, Activos, No Activos
            [5] Activar/Desactivar Estado del Jugador para Jugar
            [6] Eliminar Jugador y todas sus partidas
            [0] Salir
            '''
        )
        pie()
    elif opciones == 2:
        print('''\t
            Esta opción permite seleccionar entre dos Juegos.
            Ingresando por su DNI. 
            Puede Jugar con DNI: 99999999 en Modo Anónimo
            '''
        )
    elif opciones == 3:
        print('''\t
            Permite Agregar Jugadores por su Número de Documento.
            Si existe, muestra su Datos, caso contrario permite Agregarlo
            El DNI 99999999 -> Está ingresado como Anónimo y Activo
            '''
        )
    elif opciones == 4:
        print('''\t
            
            Permite Modificar los datos del Jugador por su Número de Documento.
            
            '''
        )
    elif opciones == 5:
        print('''\t
            
            Informe de Jugadores Activos, No activos, etc.
            
            '''
        )
    elif opciones == 6:
        print('''\t
            
            Permite Activar y Desactivar Jugador por su Número de Documento.
            
            '''
        )
    elif opciones == 7:
        print('''\t
            
            Permite Eliminar el Jugador y sus datos por su Número de Documento.
            
            '''
        )
    return None

def pie():
    print("")
    print("-"*46, end="")
    print("-> by  Grupo A <-", end="")
    print("-"*46)
    return None

def cabeceraJuegos(opciones):
    """ print("#"*42, end='->')
    print(titulo, end='<-')
    print("#"*43, end='') """
    if opciones == 1:
        print('''\t
            [1] Juego de Dados
            [2] Juego de Piedra - Papel - Tijera
            [0] Salir
            '''
        )
    elif opciones == 2:
        print('''\t
            Menú Juego de Dados
            [1] Jugar Dados
            [2] Estadísticas del Juego
            [0] Retornar al Menú Anterior
            '''
        )
    elif opciones == 3:
        print('''\t
            Menú Juego de Piedra - Papel - Tijera
            [1] Jugar 
            [2] Estadísticas del Juego
            [0] Retornar al Menú Anterior
            '''
        )
    return None
