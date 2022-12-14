# -*- coding: utf-8 -*-
from defDecoraciones import nuevaLineaSuperior,nuevoTextoCentrado,nuevaLineasinContenidoInteriorVacio,contInterior,nuevaLineaInferior,contExterior,limpiar,volviendoAlMenuPrincipal,volviendoAlMenuDados,volviendoAlMenuPipati,volviendoAlMenuAhorcado
from defJuegos import juegodados,ruedaslibres,elmejorde,ruedasfijas,juegoahorcados,tablaEstadisticasDados,tablaEstadisticasPipati
import os
import time

def estadisticas():
  while True:
    limpiar()
    time.sleep(1)
    print(f" \n ")
    nuevoTextoCentrado("@2022 - Codo a Codo - Grupo A - Prof: Fernando Massino",146)
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contInterior("░                                                                                         ░",138)
    contInterior("░  ▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓   ▓▓▓▓   ▓▓▓▓   ▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓  ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓    ▓▓▓   ░",138)
    contInterior("░  ▓      ▓   ▓    ▓    ▓    ▓  ▓   ▓    ▓    ▓   ▓    ▓      ▓    ▓       ▓    ▓  ▓   ▓  ░",138)
    contInterior("░  ▓      ▓▓▓      ▓    ▓    ▓  ▓   ▓    ▓    ▓▓▓      ▓      ▓    ▓       ▓    ▓  ▓▓▓    ░",138)
    contInterior("░  ▓▓▓▓▓     ▓     ▓    ▓▓▓▓▓▓  ▓   ▓    ▓       ▓     ▓      ▓    ▓       ▓▓▓▓▓▓     ▓   ░",138)
    contInterior("░  ▓      ▓   ▓    ▓    ▓    ▓  ▓   ▓    ▓    ▓   ▓    ▓      ▓    ▓       ▓    ▓  ▓   ▓  ░",138)
    contInterior("░  ▓      ▓   ▓    ▓    ▓    ▓  ▓   ▓    ▓    ▓   ▓    ▓      ▓    ▓       ▓    ▓  ▓   ▓  ░",138)
    contInterior("░  ▓▓▓▓▓   ▓▓▓     ▓    ▓    ▓  ▓▓▓▓   ▓▓▓▓▓   ▓▓▓     ▓    ▓▓▓▓▓   ▓▓▓▓▓  ▓    ▓   ▓▓▓   ░",138)
    contInterior("░                                                                                         ░",138)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [1] Estadísticas de dados    │",138) 
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [2] Estadísticas de pipati   │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [0] Volver al menú principal │",138)
    contInterior("└────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")
    opcionEstadistica = int (input("MENU Estadísticas: Ingrese una opción: →  "))
    if opcionEstadistica == 1:
      tablaEstadisticasDados()
      continue
    elif opcionEstadistica == 2:
      tablaEstadisticasPipati()
      continue
    elif opcionEstadistica == 0:
      volviendoAlMenuPrincipal()
      break
    else:
      print(f" \n ")
      time.sleep(1)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      contExterior("░                                                              ░",138)
      contExterior("░                      Opcion invalida!!!                      ░",138)
      contExterior("░                                                              ░",138)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      time.sleep(3)
      continue

def ahorcado():
  while True:
    limpiar()
    time.sleep(1)
    print(f" \n ")
    nuevoTextoCentrado("@2022 - Codo a Codo - Grupo A - Prof: Fernando Massino",146)
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contInterior("░                                                          ░",138)
    contInterior("░   ▓▓▓   ▓   ▓   ▓▓▓   ▓▓▓▓    ▓▓▓    ▓▓▓   ▓▓▓▓    ▓▓▓   ░",138)
    contInterior("░  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ░",138)
    contInterior("░  ▓   ▓  ▓   ▓  ▓   ▓  ▓▓▓▓   ▓      ▓   ▓  ▓   ▓  ▓   ▓  ░",138)
    contInterior("░  ▓▓▓▓▓  ▓▓▓▓▓  ▓   ▓  ▓ ▓    ▓      ▓▓▓▓▓  ▓   ▓  ▓   ▓  ░",138)
    contInterior("░  ▓   ▓  ▓   ▓  ▓   ▓  ▓  ▓   ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ░",138)
    contInterior("░  ▓   ▓  ▓   ▓   ▓▓▓   ▓   ▓   ▓▓▓   ▓   ▓  ▓▓▓▓    ▓▓▓   ░",138)
    contInterior("░                                                          ░",138)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [1] Jugar                    │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [2] Instrucciones del Juego  │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [0] Volver al menú principal │",138)
    contInterior("└────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")
    opcionAhorcado=int(input("MENU Ahorcado: Ingrese una opción: → "))
    if opcionAhorcado==1:
      juegoahorcados("ahorcado.txt") 
      continue
    if opcionAhorcado==2:
      reglasahorcado()
      continue            
    if opcionAhorcado==0:
      volviendoAlMenuPrincipal()
      break
    else:
      print(f" \n ")
      time.sleep(1)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      contExterior("░                                                              ░",138)
      contExterior("░                      Opcion invalida!!!                      ░",138)
      contExterior("░                                                              ░",138)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      time.sleep(3)
      continue

def pipati():
  while True:
    limpiar()
    time.sleep(1)
    print(f" \n ")
    nuevoTextoCentrado("@2022 - Codo a Codo - Grupo A - Prof: Fernando Massino",146)
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contInterior("░                                    ░",138)
    contInterior("░  ▓▓▓▓   ▓  ▓▓▓▓    ▓▓▓   ▓▓▓▓▓  ▓  ░",138)
    contInterior("░  ▓   ▓  ▓  ▓   ▓  ▓   ▓    ▓    ▓  ░",138)
    contInterior("░  ▓   ▓  ▓  ▓   ▓  ▓   ▓    ▓    ▓  ░",138)
    contInterior("░  ▓▓▓▓   ▓  ▓▓▓▓   ▓▓▓▓▓    ▓    ▓  ░",138)
    contInterior("░  ▓      ▓  ▓      ▓   ▓    ▓    ▓  ░",138)
    contInterior("░  ▓      ▓  ▓      ▓   ▓    ▓    ▓  ░",138)
    contInterior("░                                    ░",138)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│     Modos de Juego             │",138)
    contInterior("├────────────────────────────────┤",138)
    contInterior("│   [1] Ruedas libres            │",138)
    contInterior("│   [2] El mejor de 5            │",138)
    contInterior("│   [3] Ruedas fijas             │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [4] Instrucciones del Juego  │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [0] Volver al menú principal │",138)
    contInterior("└────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")
    dificultad=int(input("MENU PIPATI: Ingrese una opción: → "))
    if dificultad==1:
      ruedaslibres()
      continue
    if dificultad==2:
      elmejorde()
      continue
    if dificultad==3:
      ruedasfijas()
      continue
    if dificultad==4:
      reglaspiedra()                
      continue
    if dificultad==0:
      volviendoAlMenuPrincipal()
      break
    else:
      print(f" \n ")
      time.sleep(1)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      contExterior("░                                                              ░",138)
      contExterior("░                      Opcion invalida!!!                      ░",138)
      contExterior("░                                                              ░",138)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      time.sleep(3)
      continue

def dados():
  while True:
    limpiar()
    time.sleep(1)
    print(f" \n ")
    nuevoTextoCentrado("@2022 - Codo a Codo - Grupo A - Prof: Fernando Massino",146)
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contInterior("░                                     ░",138)
    contInterior("░  ▓▓▓▓    ▓▓▓   ▓▓▓▓    ▓▓▓    ▓▓▓   ░",138)
    contInterior("░  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ░",138)
    contInterior("░  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ▓▓▓    ░",138)
    contInterior("░  ▓   ▓  ▓▓▓▓▓  ▓   ▓  ▓   ▓     ▓   ░",138)
    contInterior("░  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ▓   ▓  ░",138)
    contInterior("░  ▓▓▓▓   ▓   ▓  ▓▓▓▓    ▓▓▓    ▓▓▓   ░",138)
    contInterior("░                                     ░",138)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [1] Jugar                    │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [2] Instrucciones del Juego  │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [0] Volver al menú principal │",138)
    contInterior("└────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")
    opcionDados=int(input("MENU Dados: Ingrese una opción: → "))
    if opcionDados==1:
      juegodados() 
      continue
    if opcionDados==2:
      reglasdado()
      continue
    if opcionDados==0:
      volviendoAlMenuPrincipal()
      break
    else:
      print(f" \n ")
      time.sleep(1)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      contExterior("░                                                              ░",138)
      contExterior("░                      Opcion invalida!!!                      ░",138)
      contExterior("░                                                              ░",138)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      time.sleep(3)
      continue

def musica():
  while True:
    limpiar()
    time.sleep(1)
    print(f" \n ")
    nuevoTextoCentrado("@2022 - Codo a Codo - Grupo A - Prof: Fernando Massino",146)
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contInterior("░                                                                  ░",138)
    contInterior("░  ▓▓    ▓▓  ▓     ▓   ▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓        ▓▓▓▓▓▓▓▓  ░",138)
    contInterior("░  ▓▓▓  ▓▓▓  ▓     ▓  ▓   ▓    ▓    ▓       ▓    ▓       ▓      ▓  ░",138)
    contInterior("░  ▓  ▓▓  ▓  ▓     ▓  ▓▓▓      ▓    ▓       ▓    ▓       ▓      ▓  ░",138)
    contInterior("░  ▓      ▓  ▓     ▓     ▓     ▓    ▓       ▓▓▓▓▓▓       ▓      ▓  ░",138)
    contInterior("░  ▓      ▓  ▓     ▓  ▓   ▓    ▓    ▓       ▓    ▓    ▓▓▓▓   ▓▓▓▓  ░",138)
    contInterior("░  ▓      ▓   ▓▓▓▓▓    ▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓  ▓    ▓                 ░",138)
    contInterior("░                                                                  ░",138)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [1] Acceso a Internet        │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [2] Sin Acceso a Internet    │",138)
    contInterior("└────────────────────────────────┘",138)
    contInterior("┌────────────────────────────────┐",138)
    contInterior("│   [0] Volver al menú principal │",138)
    contInterior("└────────────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    print(f" \n ")

    musica=int(input("MENU de MÚSICA: Ingrese una opción: → "))

    if musica==1:
      print("El inicio puede tardar unos segudos...")
      import webbrowser
      webbrowser.open("https://www.youtube.com/watch?v=E2U5GoX4dew&list=PLTY-fHX-ZIGwdsXnDUPhGYLkhvH9TmtXD", new=2, autoraise=True)
      volviendoAlMenuPrincipal()
      break

    if musica==2:
      while True:
        limpiar()
        time.sleep(1)
        print(f" \n ")
        nuevaLineaSuperior(146)
        nuevaLineasinContenidoInteriorVacio(140)
        contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
        contInterior("░                                                              ░",138)
        contInterior("░          MENÚ DE OPCIONES - BIBLIOTECA DE CANCIONES          ░",138)
        contInterior("░                                                              ░",138)
        contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
        nuevaLineasinContenidoInteriorVacio(140)
        nuevaLineasinContenidoInteriorVacio(140)
        contInterior(" ┌──────────────────────────────────────────────────────────────┐",138)
        contInterior(" │     [1]     │    Toad Harbor - Mario Kart 8                  │",138)
        contInterior(" │             │                                                │",138)
        contInterior(" │─────────────│────────────────────────────────────────────────│",138)
        contInterior(" │     [2]     │    Floral Fury - Cuphead original soundtrack   │",138)
        contInterior(" │             │                                                │",138)
        contInterior(" │─────────────│────────────────────────────────────────────────│",138)
        contInterior(" │     [3]     │    Mario Circuit - Mario Kart 8                │",138)
        contInterior(" │             │                                                │",138)
        contInterior(" │─────────────│────────────────────────────────────────────────│",138)
        contInterior(" │     [0]     │    Volver al menú principal                    │",138)
        contInterior(" │             │                                                │",138)
        contInterior(" └──────────────────────────────────────────────────────────────┘",138)
        nuevaLineasinContenidoInteriorVacio(140)
        nuevaLineaInferior(146)
        print(f" \n ")
      
        eleccion=int(input("MENU de OPCIONES: Ingrese una opción: → :"))

        if eleccion==1:
          print("El inicio puede tardar unos segundos...")
          os.system("start toad.wav")
          break
        if eleccion==2:
          print("El inicio puede tardar unos segundos...")
          os.system("start cup.wav")
          break
        if eleccion==3:
          print("El inicio puede tardar unos segundos...")
          os.system("start mario.wav")
          break
        else:
          print(f" \n ")
          time.sleep(1)
          contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
          contExterior("░                                                              ░",138)
          contExterior("░                      Opcion invalida!!!                      ░",138)
          contExterior("░                                                              ░",138)
          contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
          time.sleep(3)
          continue

    if musica==0:
      volviendoAlMenuPrincipal()
      break

    else:
      print(f" \n ")
      time.sleep(1)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      contExterior("░                                                              ░",138)
      contExterior("░                      Opcion invalida!!!                      ░",138)
      contExterior("░                                                              ░",138)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      time.sleep(3)
      continue

def reglasdado():
  limpiar()
  print(f" \n ")
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│                INSTRUCCIONES DE JUEGO DE DADOS                │",138)
  time.sleep(0.5)
  contExterior("+-------------+-------------+-----------------------------------+",138)
  time.sleep(0.5)
  contExterior("│  --> Se tiran 5 dados por ronda                               │",138)
  time.sleep(0.5)
  contExterior("│  --> Se jugarán 3 rondas                                      │",138)
  time.sleep(0.5)
  contExterior("│  --> Al finalizar las 3 rondas se suman los puntajes y ese    │",138)
  time.sleep(0.5)
  contExterior("│      es el resultado final de la partida                      │",138)
  time.sleep(0.5)
  contExterior("+-------------+-------------+-----------------------------------+",138)

  print(f" \n ")
  time.sleep(1)
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│               ¿COMO SE DETERMINAN LOS PUNTAJES?               │",138)
  time.sleep(0.5)
  contExterior("+-----------------+---------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("│     Puntaje     │                 Descripción                 │",138)
  time.sleep(0.5)
  contExterior("+-----------------+---------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("│     [20] -----------> 5 dados iguales suma 20 puntos          │",138)
  time.sleep(0.5)
  contExterior("│     [12] -----------> 4 dados iguales suma 12 puntos          │",138)
  time.sleep(0.5)
  contExterior("│     [9]  -----------> 3 dados iguales y un par suma 9 puntos  │",138)
  time.sleep(0.5)
  contExterior("│     [6]  -----------> 3 dados iguales suma 6 puntos           │",138)
  time.sleep(0.5)
  contExterior("│     [5]  -----------> 2 pares de dados iguales suma 5 puntos  │",138)
  time.sleep(0.5)
  contExterior("│     [2]  -----------> 1 par de dados iguales suma 2 puntos    │",138)
  time.sleep(0.5)
  contExterior("+-------------+-------------+-----------------------------------+",138)

  print(f" \n ")
  time.sleep(1)
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│                         ¿COMO SE GANA?                        │",138)
  time.sleep(0.5)
  contExterior("+-------------+-------------+-----------------------------------+",138)
  time.sleep(0.5)
  contExterior("│  --> En todos los modos, es quien al finalizar el juego,      │",138)
  time.sleep(0.5)
  contExterior("│      acumule mas puntos, GANA!                                │",138)
  time.sleep(0.5)
  contExterior("+-------------+-------------+-----------------------------------+",138)

  print(f" \n ")
  time.sleep(1)
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│                           HISTORIAL                           │",138)
  time.sleep(0.5)
  contExterior("+-------------+-------------+-----------------------------------+",138)
  time.sleep(0.5)
  contExterior("│  --> El resultado de la partida se guardará en un archivo     │",138)
  time.sleep(0.5)
  contExterior("│      para mantener el histórico                               │",138)
  time.sleep(0.5)
  contExterior("│  --> El historial de partidas se puede ver en estadisticas    │",138)
  time.sleep(0.5)
  contExterior("+-------------+-------------+-----------------------------------+",138)
  print(f" \n ")
  os.system('pause')
  limpiar()
  volviendoAlMenuDados()
  limpiar()
  return

def reglaspiedra():
  limpiar()
  contExterior("+-------------------------------------------------------------------------+",138)
  contExterior("│             INSTRUCCIONES DEL JUEGO PIEDRA, PAPEL Y TIJERA              │",138)
  time.sleep(0.5)
  contExterior("+-------------------------------------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("+-------------------+-----------------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("│  [Ruedas libres]  │  Se juegan ruedas hasta que se decida no jugar mas. │",138)
  time.sleep(0.5)
  contExterior("│                   │                                                     │",138)
  time.sleep(0.5)
  contExterior("│                   │  Cada victoria acumula un punto y al coseguirse     │",138)
  time.sleep(0.5)
  contExterior("│                   │                                                     │",138)
  time.sleep(0.5)
  contExterior("│                   │  un empate ninguno suma puntos.                     │",138)
  contExterior("+-------------------+-----------------------------------------------------+",138)
  
  time.sleep(0.5)
  contExterior("│  [El mejor de 5]  │  Se juegan ruedas indeterminadas y se termina       │",138)
  time.sleep(0.5)
  contExterior("│                   │                                                     │",138)
  time.sleep(0.5)
  contExterior("│                   │  cuando uno de los dos llegue a 5 victorias.        │",138)
  time.sleep(0.5)
  contExterior("│                   │                                                     │",138)
  time.sleep(0.5)
  contExterior("│                   │  Cada victoria acumula un punto y al coseguirse     │",138)
  time.sleep(0.5)
  contExterior("│                   │                                                     │",138)
  time.sleep(0.5)
  contExterior("│                   │  un empate ninguno suma puntos.                     │",138)
  contExterior("+-------------------+-----------------------------------------------------+",138)

  time.sleep(0.5)
  contExterior("│  [Ruedas fijas]   │  Se juegan 6 ruedas fijas ya determinadas.          │",138)
  time.sleep(0.5)
  contExterior("│                   │                                                     │",138)
  time.sleep(0.5)
  contExterior("│                   │  Cada victoria acumula un punto y al coseguirse     │",138)
  time.sleep(0.5)
  contExterior("│                   │                                                     │",138)
  time.sleep(0.5)
  contExterior("│                   │  un empate ninguno suma puntos.                     │",138)
  contExterior("+-------------------+-----------------------------------------------------+",138)

  print(f" \n ")
  time.sleep(1)
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│                         ¿COMO SE GANA?                        │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("│  --> En todos los modos, es quien al finalizar el juego,      │",138)
  time.sleep(0.5)
  contExterior("│      acumule mas puntos, GANA!                                │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)

  print(f" \n ")
  time.sleep(1)
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│                           HISTORIAL                           │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("│  --> El resultado de la partida se guardará en un archivo     │",138)
  time.sleep(0.5)
  contExterior("│      para mantener el histórico                               │",138)
  time.sleep(0.5)
  contExterior("│  --> El historial de partidas se puede ver en estadisticas    │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)
  print(f" \n ")
  os.system('pause')
  limpiar()
  volviendoAlMenuPipati()
  limpiar()
  return

def reglasahorcado():
  limpiar()
  contExterior("+-------------------------------------------------------------------------+",138)
  contExterior("│                   INSTRUCCIONES DEL JUEGO DE AHORCADO                   │",138)
  time.sleep(0.5)
  contExterior("+-------------------------------------------------------------------------+",138)
  time.sleep(0.5)

  print(f" \n ")
  time.sleep(1)
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│                        ¿COMO SE JUEGA?                        │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("│  --> La computadora tirara una palabra al azar y deberas      │",138)
  time.sleep(0.5)
  contExterior("│      adivinarla segun lo que sugiere por letras o dentro      │",138)
  time.sleep(0.5)
  contExterior("│      de un cierto numero de oportunidades.                    │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)

  print(f" \n ")
  time.sleep(1)
  contExterior("+---------------------------------------------------------------+",138)
  contExterior("│                        ¿COMO SE GANA?                         │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)
  time.sleep(0.5)
  contExterior("│ --> Tienes la posibilidad de fallar 6 intentos en los que     │",138)
  time.sleep(0.5)
  contExterior("│     tienes que ir descubriendo que letras tiene la palabra.   │",138)
  time.sleep(0.5)
  contExterior("│     A medida que vayas fallando se ira construyendo la horca. │",138)
  time.sleep(0.5)
  contExterior("│     Si llegas a 6 fallos estaras ahorcado(a). Si descubres    │",138)
  time.sleep(0.5)
  contExterior("│     la palabra ganaras                                        │",138)
  time.sleep(0.5)
  contExterior("+---------------------------------------------------------------+",138)
  print(f" \n ")
  os.system('pause')
  limpiar()
  volviendoAlMenuAhorcado()
  limpiar()
  return

def creditos():
  limpiar()
  print(f" \n ")
  nuevaLineaSuperior(146)
  nuevaLineasinContenidoInteriorVacio(140)
  contInterior(" ┌───────────────────────────────────────────┐",138)
  contInterior(" │            CREDITOS                       │",138)
  contInterior(" │-------------+-----------------------------│",138)
  time.sleep(0.5)
  contInterior(" │     Nro     │        Participantes        │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [1]     │    Agustín Contrera         │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [2]     │    Aylen Gabriela Frith     │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [3]     │    Elian Puig               │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [4]     │    Laura Fredez             │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [5]     │    Lorena Vivaldo           │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [6]     │    Natalia Florentin        │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [7]     │    Patricia Ruiz Paz        │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [8]     │    Ruth Vaccari             │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [9]     │    Sebastian Saavedra       │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [10]    │    Sofía A. Soto            │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [11]    │    Valentina Dal Molin      │",138)
  contInterior(" │─────────────│─────────────────────────────│",138)
  time.sleep(0.5)
  contInterior(" │     [12]    │    Victoria Ricardo         │",138)
  time.sleep(0.5)
  contInterior(" └───────────────────────────────────────────┘",138)
  nuevaLineasinContenidoInteriorVacio(140)
  nuevaLineaInferior(146)
  time.sleep(1)
  print(f" \n ")
  os.system('pause')
  limpiar()
  volviendoAlMenuPrincipal()
  limpiar()
  return
