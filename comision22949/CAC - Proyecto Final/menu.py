from defDecoraciones import nuevaLineaSuperior,nuevoTextoCentrado,nuevaLineasinContenidoInteriorVacio,contInterior,nuevaLineaInferior,contExterior,limpiar 
import defMenu
import time   

time.sleep(1)
print("  ____    _                                         _       _                       ")
print(" | __ )  (_)   ___   _ __   __   __   ___   _ __   (_)   __| |   ___                ")
print(" |  _ \  | |  / _ \ | '_ \  \ \ / /  / _ \ | '_ \  | |  / _` |  / _ \   /  __ _  \  ")
print(" | |_) | | | |  __/ | | | |  \ V /  |  __/ | | | | | | | (_| | | (_) | |  / _` |  | ")
print(" |____/  |_|  \___| |_| |_|   \_/    \___| |_| |_| |_|  \__,_|  \___/   \ \__,_| /  ")
time.sleep(4)
limpiar()

while True:
    time.sleep(1)
    print(f" \n ")
    nuevoTextoCentrado("@2022 - Codo a Codo - Grupo A - Prof: Fernando Massino",146)
    nuevaLineaSuperior(146)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    contInterior("░                                                                                             ░",138)
    contInterior("░  ▓▓▓▓▓  ▓       ▓▓▓▓▓   ▓▓▓▓  ▓▓▓▓▓    ▓▓▓▓▓  ▓   ▓        ▓   ▓   ▓  ▓▓▓▓▓   ▓▓▓▓   ▓▓▓    ░",138)
    contInterior("░  ▓      ▓       ▓      ▓   ▓    ▓        ▓    ▓   ▓        ▓   ▓   ▓  ▓      ▓   ▓  ▓   ▓   ░",138)
    contInterior("░  ▓      ▓       ▓      ▓        ▓        ▓    ▓   ▓        ▓   ▓   ▓  ▓      ▓      ▓   ▓   ░",138)
    contInterior("░  ▓▓▓▓▓  ▓       ▓▓▓▓▓  ▓ ▓▓▓    ▓        ▓    ▓   ▓        ▓   ▓   ▓  ▓▓▓▓▓  ▓ ▓▓▓  ▓   ▓   ░",138)
    contInterior("░  ▓      ▓       ▓      ▓   ▓    ▓        ▓    ▓   ▓    ▓   ▓   ▓   ▓  ▓      ▓   ▓  ▓   ▓   ░",138)
    contInterior("░  ▓      ▓       ▓      ▓   ▓    ▓        ▓    ▓   ▓    ▓   ▓   ▓   ▓  ▓      ▓   ▓  ▓   ▓   ░",138)
    contInterior("░  ▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓      ▓     ▓▓▓      ▓▓▓     ▓▓▓   ▓▓▓▓▓   ▓▓▓    ▓▓▓    ░",138)
    contInterior("░                                                                                             ░",138)
    contInterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
    nuevaLineasinContenidoInteriorVacio(140)
    contInterior("┌──────────────────────────┐      ┌─────────────────────────────────────────────────────┐   ┌──────────────────────────┐",138)
    contInterior("│                          │      │                                                     │   │             █            │",138)
    contInterior("│                          │      │                                              ██     │   │            ▄▄▄           │",138)
    contInterior("│      █▀▀▀▀▀▀▀▀▀▀▀█       │      │  █▀▀▀▀▀▀█▀▀▄                      ▄▄▄▄      ██      │   │           █   █          │",138)
    contInterior("│      █  ▀        █       │      │  █      █   ▀▄                   █    █    ██       │   │           ▄▀▀▀▄          │",138)
    contInterior("│      █     ▀     █       │      │  █      ▀▀▀▀▀█                    ▀▀▀▀▀▀▀███        │   │         ▄▀  █  ▀▄        │",138)
    contInterior("│      █        ▀  █       │      │  █           █     ▄▀▀▀▀▀▀▀▀▀▀▄      ▄▄▄▄█▀▀▀▀▀▀▀▀▀ │   │        ▀    █    ▀       │",138)
    contInterior("│      █▄▄▄▄▄▄▄▄▄▄▄█       │      │  █           █   ▄▀            ▀▄   █    █          │   │           ▄▀ ▀▄          │",138)
    contInterior("│                          │      │  █▄▄▄▄▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   ▀▀▀▀           │   │         ▄▀     ▀▄        │",138)
    contInterior("│                          │      │                                                     │   │        ▀         ▀       │",138)
    contInterior("├──────────────────────────┤      ├─────────────────────────────────────────────────────┤   ├──────────────────────────┤",138)
    contInterior("│     [1] Juego de Dados   │      │         [2] Juego de Piedra, Papel o Tijera         │   │   [3] Juego del Ahorcado │",138)
    contInterior("└──────────────────────────┘      └─────────────────────────────────────────────────────┘   └──────────────────────────┘",138)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineasinContenidoInteriorVacio(140)
    nuevaLineaInferior(146)
    contExterior("┌──────────────────────┐    ┌─────────────────────┐  ┌─────────────────────┐    ┌─────────────────────┐",138)
    contExterior("│   [4] Estadísticas   │    │     [5] Créditos    │  │  [6] Activar Música │    │       [0] Salir     │",138)
    contExterior("└──────────────────────┘    └─────────────────────┘  └─────────────────────┘    └─────────────────────┘",138)
    print(f" \n ")

    menu =input("MENU PRINCIPAL: Ingrese una opción: → ")

    if menu == "1": # Opcion 1 Juego de Dados..
      defMenu.dados()

    elif menu == "2": # Opcion 2 Piedra, Papel o Tijera..
      defMenu.pipati()

    elif menu == "3": # Opcion 3 Juego del Ahorcado..
      defMenu.ahorcado()

    elif menu == "4": #Opcion 4 Estadisticas..
      defMenu.estadisticas()

    elif menu == "5": # Opcion 5 Visualizar los creditos..
        defMenu.creditos()

    elif menu == "6": # Opcion 6 Activar Música..
        defMenu.musica()

    elif menu == "0":
      limpiar()
      time.sleep(0.6)
      print("     ___                     _             ") 
      print("    / __|  _ _   __ _   __  (_)  __ _   ___") 
      print("   | (_ | | '_| / _` | / _| | | / _` | (_-<") 
      print("    \___| |_|   \__,_| \__| |_| \__,_| /__/") 
      time.sleep(0.6)
      print("    _ __   ___   _ _ ") 
      print("   | '_ \ / _ \ | '_|") 
      print("   | .__/ \___/ |_|  ") 
      print("   |_|               ") 
      time.sleep(0.6)
      print("      _                              _ ") 
      print("     (_)  _  _   __ _   __ _   _ _  | |") 
      print("     | | | || | / _` | / _` | | '_| |_|") 
      print("    _/ |  \_,_| \__, | \__,_| |_|   (_)") 
      print("   |__/         |___/                  ")
      time.sleep(3)
      print(f" \n ")
      limpiar()
      break

    else:
      time.sleep(1)
      print(f" \n ")
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      contExterior("░                                                              ░",138)
      contExterior("░                      Opcion invalida!!!                      ░",138)
      contExterior("░                                                              ░",138)
      contExterior("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",138)
      time.sleep(3)
      limpiar()
      continue