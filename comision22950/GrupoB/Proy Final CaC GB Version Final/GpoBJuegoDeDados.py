from random import randint
def juegosDados():  

  print()
  print("~"*50)
  print("""
  \tJuego de dados: 
  Se tiran 5 dados por ronda.
  Se jugarán 5 rondas.
  Puntuación
  - Los 5 dados iguales suma 20 puntos
  - 4 dados iguales suma 12 puntos
  - 3 dados iguales y un par suma 9 puntos
  - 3 dados iguales suma 6 puntos
  - 2 pares de dados iguales suma 5 puntos
  - 1 par de dados iguales suma 2 puntos
  """)
  print("~"*50)
  print()

  ronda=1
  dados=[]

  puntaje=0
  puntajeTotal=0

  while ronda<=3:
    print (f"\tRonda # {ronda}")
    print()
    tirarDados=input("\tTirar dados?(s/n): ")
    print()
    if tirarDados=="n":
      print("\tDebe tirar los dados hasta completar las rondas")
      continue
    for i in range (5):
      dados.append(randint(1,6))
    print ("Tus dados son ----------",dados)
    print()
    trio=0
    par1=0
    par2=0
    puntaje=0
    for dado in dados:
          if dados.count(dado)==5:
              print(f"\tGenerala de ---------- ({dado})".upper())
              puntaje=puntaje + 20
              break
          elif dados.count(dado)==4:
              print(f"\tPoker de ---------- ({dados})".upper())
              puntaje=puntaje + 12
              break
          elif dados.count(dado)==3:
            if trio==0:
              print(f"\tPierna de ---------- {dado}".upper())
              trio=dado
          elif dados.count(dado)==2:
            if par1==0:
                  print(f"\tPar de ----------{dado}".upper())
                  par1=dado
            elif par1!=dado and par2==0:
                  print(f"Segundo par de ---------- {dado}".upper())
                  par2=dado

    if par1 !=0 and par2 !=0:
      print(f"Doble par sumas 5 puntos".upper())
      puntaje=puntaje + 5
    elif par1 !=0 or par2 !=0:
      if trio!=0:
        print(f"\tFull sumas 9 puntos".upper())
        puntaje= puntaje + 9
      else:
        print(f"\tpar Simple sumas 2 puntos".upper())
        puntaje=puntaje + 2
    else:
      if trio!=0:
        print(f"\ttrio de {trio} sumas 6 puntos".upper())
        puntaje=puntaje+6
    print(f"\tPuntaje de la ronda: {puntaje}".upper())
    print()
      
    ronda=ronda + 1
    puntajeTotal=puntajeTotal+puntaje
    dados.clear()
  print(f"\tPuntaje total: {puntajeTotal}".upper())
  return puntajeTotal
