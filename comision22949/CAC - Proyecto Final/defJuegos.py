from random import randint
import random 
from defDecoraciones import nuevaLineaSuperior,nuevaLineasinContenidoInteriorVacio,contInterior,nuevaLineaInferior,limpiar,volviendoAlMenuEstadisticas,contExterior,volviendoAlMenuDados,volviendoAlMenuPipati,volviendoAlMenuAhorcado
import time
import os


"""ESTÁ PARTE ES DE LA LÓGICA DEL PIEDRA, PAPEL Y TIjERA"""


def logicaPipati (opcUsu, opcPc):# Lógica principal del juego
  if opcUsu == opcPc:
    time.sleep(1)
    print(f" \n ")
    print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("         ░                                                              ░")
    print("         ░                           EMPATE!!                           ░")
    print("         ░                                                              ░")
    print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    time.sleep(1)
    print(f" \n ")
    os.system('pause')
    limpiar()
    return "emp"
    
  elif opcUsu == 1: # Piedra
    if opcPc == 2: # Papel
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░            Gana Computadora, Papel mata a piedra.            ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")
      os.system('pause')
      limpiar()
      return "com"
    else:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░               Ganaste, Piedra mata a Tijeras.                ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")
      os.system('pause')
      limpiar()      
      return "usu"
  elif opcUsu == 2: # Papel
    if opcPc == 1: # Piedra
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░                Ganaste, Papel mata a Piedra.                 ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")
      os.system('pause')
      limpiar()
      return "usu"
    else:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░            Gana Computadora, Tijeras mata a Papel.           ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")
      os.system('pause')
      limpiar()
      return "com"
  elif opcUsu == 3 and opcPc == 1: # Tijeras
    time.sleep(1)
    print(f" \n ")
    print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("         ░                                                              ░")
    print("         ░           Gana Computadora, Piedra mata a Tijeras.           ░")
    print("         ░                                                              ░")
    print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    time.sleep(1)
    print(f" \n ")
    os.system('pause')
    limpiar()
    return "com"
  elif opcUsu == 3 and opcPc == 2:
    time.sleep(1)
    print(f" \n ")
    print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("         ░                                                              ░")
    print("         ░                Ganaste, Tijeras mata a Papel.                ░")
    print("         ░                                                              ░")
    print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    time.sleep(1)
    print(f" \n ")
    os.system('pause')
    limpiar()
    return "usu"

#Ruedas Libres
def ruedaslibres():#Juega por defecto al ruedas libres
  puntajeUsuario = 0
  puntajePc = 0

  while True:
    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │      PIPATI - Ruedas libres     │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │  ┌────────────────────────────┐ │",138)
    contInterior(" │  │     A Jugar > Elige:       │ │",138)
    contInterior(" │  ├────────────────────────────┤ │",138)
    contInterior(" │  │   [1] Piedra               │ │",138)
    contInterior(" │  │   [2] Papel                │ │",138)
    contInterior(" │  │   [3] Tijera               │ │",138)
    contInterior(" │  │   [0] Salir                │ │",138)
    contInterior(" │  └────────────────────────────┘ │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")
    time.sleep(0.5)

    miOpcion = int(input('''Ingrese una opción: -→ '''))

    computadoraOpcion = randint(1,3) # Un numero del 1 al 3
    if miOpcion == 0:
      break
    ganador = logicaPipati(miOpcion,computadoraOpcion)
    #Genera el contador de victorias del usuario o pc
    if ganador == "usu":
      puntajeUsuario=puntajeUsuario +1
    elif ganador == "com":
      puntajePc = puntajePc + 1
    
  agregarPartida("puntajepipati.txt",puntajeUsuario,puntajePc)#Agrega las partidas al archivo.

  time.sleep(2)
  limpiar()
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░                                    PUNTAJE FINAL                                    ░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(f" ░                         Vos:{puntajeUsuario:<26}Pc:{puntajePc:<27}░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  time.sleep(2)
  print(f" \n ")
  os.system('pause')
  volviendoAlMenuPipati()

#El mejor de 5
def elmejorde():
  puntajeUsuario = 0
  puntajePc = 0

  while True:
    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │      PIPATI - El mejor de 5     │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │  ┌────────────────────────────┐ │",138)
    contInterior(" │  │     A Jugar > Elige:       │ │",138)
    contInterior(" │  ├────────────────────────────┤ │",138)
    contInterior(" │  │   [1] Piedra               │ │",138)
    contInterior(" │  │   [2] Papel                │ │",138)
    contInterior(" │  │   [3] Tijera               │ │",138)
    contInterior(" │  │   [0] Salir                │ │",138)
    contInterior(" │  └────────────────────────────┘ │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")
    time.sleep(0.5)

    miOpcion = int(input(f'''Ingrese una opción: -→ ''')) 

    computadoraOpcion = randint(1,3) # Un numero del 1 al 3
    if miOpcion == 0:
      break
    ganador = logicaPipati(miOpcion,computadoraOpcion)
    #Genera el contador de victorias del usuario o pc
    if ganador == "usu":
      puntajeUsuario=puntajeUsuario +1
    elif ganador == "com":
      puntajePc = puntajePc + 1

    if puntajePc == 5 or puntajeUsuario == 5:
      break
  
  agregarPartida("puntajepipati.txt",puntajeUsuario,puntajePc)#Agrega las partidas al archivo.

  time.sleep(2)
  limpiar()
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░                                    PUNTAJE FINAL                                    ░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(f" ░                         Vos:{puntajeUsuario:<26}Pc:{puntajePc:<27}░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  time.sleep(2)
  print(f" \n ")
  os.system('pause')
  volviendoAlMenuPipati()

#Ruegas Fijas
def ruedasfijas():
  puntajeUsuario = 0
  puntajePc = 0
  partidas = 0

  while True:
    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │      PIPATI - Ruedas fijas      │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │  ┌────────────────────────────┐ │",138)
    contInterior(" │  │     A Jugar > Elige:       │ │",138)
    contInterior(" │  ├────────────────────────────┤ │",138)
    contInterior(" │  │   [1] Piedra               │ │",138)
    contInterior(" │  │   [2] Papel                │ │",138)
    contInterior(" │  │   [3] Tijera               │ │",138)
    contInterior(" │  │   [0] Salir                │ │",138)
    contInterior(" │  └────────────────────────────┘ │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")
    time.sleep(0.5)
    miOpcion = int(input(f'''Ingrese una opción: -→ '''))

    computadoraOpcion = randint(1,3) # Un numero del 1 al 3

    if miOpcion == 0:
      break
    ganador = logicaPipati(miOpcion,computadoraOpcion)
    #Genera el contador de victorias del usuario o pc
    if ganador == "usu":
      puntajeUsuario=puntajeUsuario +1
    elif ganador == "com":
      puntajePc = puntajePc + 1

    partidas = partidas + 1
    if partidas == 6:
      break

  agregarPartida("puntajepipati.txt",puntajeUsuario,puntajePc)#Agrega las partidas al archivo.

  time.sleep(2)
  limpiar()
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░                                    PUNTAJE FINAL                                    ░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(f" ░                         Vos:{puntajeUsuario:<26}Pc:{puntajePc:<27}░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  time.sleep(2)
  print(f" \n ")
  os.system('pause')
  volviendoAlMenuPipati()


"""ESTÁ PARTE ES DE LA LÓGICA DEL JUEGO DE DADOS"""


def logicaDados(dados,puntaje):
  triple = 0
  par1 = 0
  par2 = 0
  #dados = [5, 5, 2, 4, 5]
  for dado in dados:
    if dados.count(dado) == 5:
      puntaje = puntaje + 20
      break
    elif dados.count(dado) == 4:
      puntaje = puntaje + 12
      break
    elif dados.count(dado) == 3:
      if triple == 0:
        triple = dado
    elif dados.count(dado) == 2:
      if par1 == 0:
        par1 = dado
      elif par1 != dado and par2 == 0:
        par2 = dado

  if par1 !=0 and par2 != 0:
    puntaje = puntaje + 5
  elif par1 !=0 or par2 !=0:
    if triple !=0: 
      puntaje = puntaje + 9
    else:
      puntaje = puntaje + 2
  else:
    if triple !=0:
      puntaje = puntaje + 6

  return puntaje

def juegodados():
  import time 
  #ronda=1
  dadosUsu = []
  dadosPc = []
  puntajeUsu = 0
  puntajePc = 0
  puntajeTotalUsu = 0
  puntajeTotalPc = 0
  for ronda in range(1,4):
    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │            Ronda # {}            │".format(ronda),138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │                                 │",138)
    contInterior(" │          █▀▀▀▀▀▀▀▀▀▀▀█          │",138)
    contInterior(" │          █  ▀        █          │",138)
    contInterior(" │          █     ▀     █          │",138)
    contInterior(" │          █        ▀  █          │",138)
    contInterior(" │          █▄▄▄▄▄▄▄▄▄▄▄█          │",138)
    contInterior(" │                                 │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    time.sleep(1)

    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │            Ronda # {}            │".format(ronda),138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │                                 │",138)
    contInterior(" │          █▀▀▀▀▀▀▀▀▀▀▀█          │",138)
    contInterior(" │          █     ▀     █          │",138)
    contInterior(" │          █     ▀     █          │",138)
    contInterior(" │          █     ▀     █          │",138)
    contInterior(" │          █▄▄▄▄▄▄▄▄▄▄▄█          │",138)
    contInterior(" │                                 │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    time.sleep(1)

    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │            Ronda # {}            │".format(ronda),138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │                                 │",138)
    contInterior(" │          █▀▀▀▀▀▀▀▀▀▀▀█          │",138)
    contInterior(" │          █        ▀  █          │",138)
    contInterior(" │          █     ▀     █          │",138)
    contInterior(" │          █  ▀        █          │",138)
    contInterior(" │          █▄▄▄▄▄▄▄▄▄▄▄█          │",138)
    contInterior(" │                                 │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    time.sleep(1)

    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │            Ronda # {}            │".format(ronda),138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │                                 │",138)
    contInterior(" │          █▀▀▀▀▀▀▀▀▀▀▀█          │",138)
    contInterior(" │          █           █          │",138)
    contInterior(" │          █  ▀  ▀  ▀  █          │",138)
    contInterior(" │          █           █          │",138)
    contInterior(" │          █▄▄▄▄▄▄▄▄▄▄▄█          │",138)
    contInterior(" │                                 │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    time.sleep(1)

    limpiar()
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │            Ronda # {}            │".format(ronda),138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior(" ┌─────────────────────────────────┐",138)
    contInterior(" │                                 │",138)
    contInterior(" │          █▀▀▀▀▀▀▀▀▀▀▀█          │",138)
    contInterior(" │          █  ▀        █          │",138)
    contInterior(" │          █     ▀     █          │",138)
    contInterior(" │          █        ▀  █          │",138)
    contInterior(" │          █▄▄▄▄▄▄▄▄▄▄▄█          │",138)
    contInterior(" │                                 │",138)
    contInterior(" └─────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    time.sleep(1)

    for i in range(5):
      dadosUsu.append(randint(1,6))

    for i in range(5):
      dadosPc.append(randint(1,6))
    
    contExterior( " ┌────────────────────────────────────────────┐┌──────────────────────────────────────────────┐",138)
    contExterior( " │                                            ││                                              │",138)
    contExterior(" │     Tus dados son: {}         ││    Los dados Pc son: {}         │".format(dadosUsu,dadosPc),138)
    contExterior( " │                                            ││                                              │",138)
    contExterior( " └────────────────────────────────────────────┘└──────────────────────────────────────────────┘",138)

    puntajeUsu = logicaDados(dadosUsu,puntajeUsu)
    time.sleep(0.5)
    if puntajeUsu == 20:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░    Felicitaciones sacaste 5 dados iguales (sumas 20 ptos)    ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")

    elif puntajeUsu== 12:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░    Felicitaciones sacaste 4 dados iguales (sumas 12 ptos)    ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")

    elif puntajeUsu == 9:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░                Hiciste full! Sumas 9 puntos                  ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")

    elif puntajeUsu == 6:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░                 Sacaste trio! Sumas 6 puntos                 ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")

    elif puntajeUsu == 5:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░               Sacaste doble par! Sumas 5 ptos                ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")

    elif puntajeUsu == 2:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░             Sacaste par simple! Sumas 2 puntos               ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")

    else:
      time.sleep(1)
      print(f" \n ")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("         ░                                                              ░")
      print("         ░                        No sacaste nada                       ░")
      print("         ░                                                              ░")
      print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      time.sleep(1)
      print(f" \n ")
    
    puntajeTotalUsu = puntajeTotalUsu + puntajeUsu
    puntajeUsu = 0
    dadosUsu.clear()

    puntajePc = logicaDados(dadosPc,puntajePc)
    puntajeTotalPc = puntajeTotalPc + puntajePc
    puntajePc = 0
    dadosPc.clear()
    os.system('pause')

  agregarPartida("puntajedados.txt",puntajeTotalUsu,puntajeTotalPc)

  time.sleep(2)
  limpiar()
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░                                    PUNTAJE FINAL                                    ░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(f" ░                         Vos:{puntajeTotalUsu:<26}Pc:{puntajeTotalPc:<27}░",138)
  contExterior(" ░                                                                                     ░",138)
  contExterior(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  time.sleep(2)
  print(f" \n ")
  os.system('pause')
  volviendoAlMenuDados()


"""ESTÁ PARTE ES DE LA LÓGICA DEL JUEGO AHORCADOS"""


def mostrar_escenario(errores):

    if errores == 0:
      limpiar()
      nuevaLineaSuperior(146)
      nuevaLineasinContenidoInteriorVacio(140)
      contInterior("┌─────────────────────────────────┐",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("└─────────────────────────────────┘",138)
      nuevaLineasinContenidoInteriorVacio(140)
      nuevaLineaInferior(146)

    elif errores == 1:
      limpiar()
      nuevaLineaSuperior(146)
      nuevaLineasinContenidoInteriorVacio(140)
      contInterior("┌─────────────── █ ───────────────┐",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("└─────────────────────────────────┘",138)
      nuevaLineasinContenidoInteriorVacio(140)
      nuevaLineaInferior(146)
    elif errores == 2:
      limpiar()
      nuevaLineaSuperior(146)
      nuevaLineasinContenidoInteriorVacio(140)
      contInterior("┌─────────────── █ ───────────────┐",138)
      contInterior("│                █                │",138)
      contInterior("│               ▄▄▄               │",138)
      contInterior("│              █   █              │",138)
      contInterior("│               ▀▀▀               │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("└─────────────────────────────────┘",138)
      nuevaLineasinContenidoInteriorVacio(140)
      nuevaLineaInferior(146)

    elif errores == 3:
      limpiar()
      nuevaLineaSuperior(146)
      nuevaLineasinContenidoInteriorVacio(140)
      contInterior("┌─────────────── █ ───────────────┐",138)
      contInterior("│                █                │",138)
      contInterior("│               ▄▄▄               │",138)
      contInterior("│              █   █              │",138)
      contInterior("│              ▄▀▀▀               │",138)
      contInterior("│            ▄▀  █                │",138)
      contInterior("│           ▀    █                │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("└─────────────────────────────────┘",138)
      nuevaLineasinContenidoInteriorVacio(140)
      nuevaLineaInferior(146)

    elif errores == 4:
      limpiar()
      nuevaLineaSuperior(146)
      nuevaLineasinContenidoInteriorVacio(140)
      contInterior("┌─────────────── █ ───────────────┐",138)
      contInterior("│                █                │",138)
      contInterior("│               ▄▄▄               │",138)
      contInterior("│              █   █              │",138)
      contInterior("│              ▄▀▀▀▄              │",138)
      contInterior("│            ▄▀  █  ▀▄            │",138)
      contInterior("│           ▀    █    ▀           │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("│                                 │",138)
      contInterior("└─────────────────────────────────┘",138)
      nuevaLineasinContenidoInteriorVacio(140)
      nuevaLineaInferior(146)

    elif errores == 5:
      limpiar()
      nuevaLineaSuperior(146)
      nuevaLineasinContenidoInteriorVacio(140)
      contInterior("┌─────────────── █ ───────────────┐",138)
      contInterior("│                █                │",138)
      contInterior("│               ▄▄▄               │",138)
      contInterior("│              █   █              │",138)
      contInterior("│              ▄▀▀▀▄              │",138)
      contInterior("│            ▄▀  █  ▀▄            │",138)
      contInterior("│           ▀    █    ▀           │",138)
      contInterior("│              ▄▀                 │",138)
      contInterior("│            ▄▀                   │",138)
      contInterior("│           ▀                     │",138)
      contInterior("└─────────────────────────────────┘",138)
      nuevaLineasinContenidoInteriorVacio(140)
      nuevaLineaInferior(146)

    elif errores == 6:
      limpiar()
      nuevaLineaSuperior(146)
      nuevaLineasinContenidoInteriorVacio(140)
      contInterior("┌─────────────── █ ───────────────┐",138)
      contInterior("│                █                │",138)
      contInterior("│               ▄▄▄               │",138)
      contInterior("│              █   █              │",138)
      contInterior("│              ▄▀▀▀▄              │",138)
      contInterior("│            ▄▀  █  ▀▄            │",138)
      contInterior("│           ▀    █    ▀           │",138)
      contInterior("│              ▄▀ ▀▄              │",138)
      contInterior("│            ▄▀     ▀▄            │",138)
      contInterior("│           ▀         ▀           │",138)
      contInterior("└─────────────────────────────────┘",138)
      nuevaLineasinContenidoInteriorVacio(140)
      nuevaLineaInferior(146)

def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
      print(casilla , end=' ')
    print(f" \n ")
    print(f" \n ")
    if len(letras_erroneas) > 0:
      print('Letras erróneas:', *letras_erroneas)
      print(f" \n ")

def juegoahorcados(archivo):
    diccionario = []
    palabras = open(archivo,"r")
    for i in palabras.readlines():
      i= i.replace("\n","")
      diccionario.append(i)
    palabras.close()
    
    # print(diccionario)
    palabra = random.choice(diccionario).lower()
    tablero = ['_']*len(palabra)
    letras_erroneas = []

    while len(letras_erroneas) < 6:
      mostrar_escenario(len(letras_erroneas))
      mostrar_tablero(tablero, letras_erroneas)

      valida = False
      while not valida:
        letra = input('Introduce una letra (a-z): ').lower()
        valida = 'a' <= letra <= 'z' and len(letra) == 1
        if not valida:
          time.sleep(1)
          print(f" \n ")
          print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
          print("         ░                                                   ░")
          print("         ░    Error, la letra tiene que estar entre a y z.   ░")
          print("         ░                                                   ░")
          print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
          time.sleep(3)
          print(f" \n ")
        else:
          valida = letra not in tablero + letras_erroneas
          if not valida:
            time.sleep(1)
            print(f" \n ")
            print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            print("         ░                                                   ░")
            print("         ░              Error, letra repetida.               ░")
            print("         ░                                                   ░")
            print("         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            time.sleep(3)
            print(f" \n ")

      if letra in palabra:
        for indice, letra_palabra in enumerate(palabra):
          if letra == letra_palabra:
            tablero[indice] = letra
      else:
        letras_erroneas.append(letra)

      if '_' not in tablero:
        time.sleep(0.5)
        mostrar_escenario(len(letras_erroneas))
        print(f" \n ")
        time.sleep(1)
        mostrar_tablero(tablero, letras_erroneas)
        time.sleep(1)
        contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
        contExterior("░                                                   ░",138)
        contExterior("░             ¡Felicitaciones, ganaste!             ░",138)
        contExterior("░                                                   ░",138)
        contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
        print(f" \n ")
        os.system('pause')
        volviendoAlMenuAhorcado()
        break
    else:
      time.sleep(0.5)
      print(f" \n ")
      mostrar_escenario(len(letras_erroneas))
      time.sleep(1)
      print(f" \n ")
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      contExterior("░                                                   ░",138)
      contExterior("░                     Perdiste!!                    ░",138)
      contExterior("░                                                   ░",138)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      print(f" \n ")
      contExterior(f"La palabra era: {palabra}",138)
      time.sleep(2)
      print(f" \n ")
      os.system('pause')
      volviendoAlMenuAhorcado()


"""ESTÁ PARTE ES DE LA LÓGICA DE LAS ESTADISTICAS"""


def controlInput (leyenda,msjError="Debe ingresar un número entero"):#verificar ingreso solo de valores numericos
    while True:
       try:
          entero = int(input(leyenda))
          break
       except ValueError:
         print(msjError)
    return entero

def leerArchivo (archivo): #transformar datos del archivo a listas
  try:# Habre el archivo en modo lectura/Lo crea si no existe
    partidas = open(archivo,"r")
  except FileNotFoundError:
    partidas = open(archivo,"a")
    partidas.close()
    partidas = open(archivo,"r")

    #partidas=open(archivo,"r")
  listaDePartidas=[]
  for i in partidas.readlines():
    partida= i.replace("\n","")
    partida= partida.split(":")
              
    partida[1]=int(partida[1])
    partida[3]=int(partida[3])
              
    listaDePartidas.append(partida)
  partidas.close()
  return listaDePartidas

def agregarPartida(archivo,Usuario,Pc):#Agrega las partidas al archivo
  partidas = leerArchivo(archivo)
  if len(partidas) == 0: # Si el archivo esta vacio agrega en la primer fila
    partida = open(archivo, "a")
    partida.write(f"Vos:{Usuario}:pc:{Pc}")
  else: # Si el archivo tiene contenido agrega en una nueva fila
    partida = open(archivo, "a")
    partida.write(f"\nVos:{Usuario}:pc:{Pc}")
  partida.close()

def partidasGanPerdEmp (archivo): #total de victorias,derrotas y empates en los diferentes juegos
  listaDePartidas = leerArchivo(archivo)
  victoriasUsuario=0
  victoriasPc=0
  empate=0
  for partida in listaDePartidas: 
    if partida[1] > partida[3]:
      victoriasUsuario = victoriasUsuario + 1
    elif partida[1] < partida[3]:
      victoriasPc = victoriasPc + 1
    else:
      empate = empate + 1
  return victoriasUsuario,victoriasPc,empate  

def conteoPartidas(archivo): #total de partidas jugadas
     lista=leerArchivo(archivo) 
     cantPartidas=len(lista) 
     return cantPartidas

def tablaEstadisticasDados():
  #listaPartidas= leerArchivo("puntajedados.txt")
  listaDePartidas = leerArchivo("puntajedados.txt")
  if len(listaDePartidas) == 0: #Aquí controla si el archivo está vacio.
    time.sleep(1)
    print(f" \n ")
    contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contExterior("░                                                              ░",138)
    contExterior("░      No hay estadisticas!! Por favor inicie un juego...      ░",138)
    contExterior("░                                                              ░",138)
    contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    time.sleep(0.6)
    print(f" \n ")
    os.system('pause')
    return

  limpiar()
  time.sleep(1)
  print(f" \n ")
  contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  contExterior("░                                      ░",138)
  contExterior("░    ESTADÍSTICAS DEL JUEGO DE DADOS   ░",138)
  contExterior("░                                      ░",138)
  contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  time.sleep(0.6)
  print(f" \n ")
  victorias,derrotas,empates=partidasGanPerdEmp("puntajedados.txt")
  contExterior("+--------------------------------------+",138)  
  contExterior("│          ESTADISTICAS DADOS:         │",138)
  contExterior("+-------------+-------------+----------+",138)
  contExterior("│  Victorias  │  Derrotas   │ Empates  │",138) 
  contExterior("+-------------+-------------+----------+",138)
  cadena = "│{:<13}│{:<13}│{:<10}│".format(victorias,derrotas,empates)
  contExterior (cadena,138)
  contExterior("+-------------+-------------+----------+",138)
  time.sleep(0.6)
  print(f" \n ")
  contExterior("+-------------+-------------+----------+",138)
  cantPartidas=conteoPartidas("puntajedados.txt")
  texto="Cant. de partidas jugadas:"
  cadena2="│{:<27}│{:<10}│".format(texto,cantPartidas)
  contExterior(cadena2,138)
  contExterior("+---------------------------+----------+",138)
  print(f" \n ")
  time.sleep(0.6)
  os.system('pause')
  volviendoAlMenuEstadisticas()
  limpiar()

def tablaEstadisticasPipati():
   #listaPartidas= leerArchivo("puntajepipati.txt")
  listaDePartidas = leerArchivo("puntajepipati.txt")
  if len(listaDePartidas) == 0: #Aquí controla si el archivo está vacio.
    time.sleep(1)
    print(f" \n ")
    contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contExterior("░                                                              ░",138)
    contExterior("░      No hay estadisticas!! Por favor inicie un juego...      ░",138)
    contExterior("░                                                              ░",138)
    contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    time.sleep(0.6)
    print(f" \n ")
    os.system('pause')
    return
  
  limpiar()
  time.sleep(1)
  print(f" \n ")
  contExterior("  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  contExterior("  ░                                                       ░",138)
  contExterior("  ░    ESTADÍSTICAS DEL JUEGO DE PIEDRA, PAPEL Y TIJERA   ░",138)
  contExterior("  ░                                                       ░",138)
  contExterior("  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
  print(f" \n ")
  time.sleep(0.6)
  victorias,derrotas,empates=partidasGanPerdEmp("puntajepipati.txt")
  contExterior("+--------------------------------------+",138)  
  contExterior("│         ESTADISTICAS PIPATI:         │",138)
  contExterior("+-------------+-------------+----------+",138)
  contExterior("│  Victorias  │  Derrotas   │ Empates  │",138)
  contExterior("+-------------+-------------+----------+",138)
  cadena = "│{:<13}│{:<13}│{:<10}│".format(victorias,derrotas,empates)
  contExterior (cadena,138)
  contExterior("+-------------+-------------+----------+",138)
  print(f" \n ")
  time.sleep(0.6)
  contExterior("+-------------+-------------+----------+",138)
  cantPartidas=conteoPartidas("puntajepipati.txt")
  texto="Cant. de partidas jugadas:"
  cadena2="│{:<27}│{:<10}│".format(texto,cantPartidas)
  contExterior(cadena2,138)
  contExterior("+---------------------------+----------+",138)
  print(f" \n ")
  time.sleep(0.6)
  os.system('pause')
  volviendoAlMenuEstadisticas()
  limpiar()
