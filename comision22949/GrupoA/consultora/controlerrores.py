from colorama import Fore, Style, init
init()

def controlErrornumerico (leyenda,msjError="Debe ingresar un número entero"):
    while True:
       try:
          entero = int(input(leyenda))
          break
       except ValueError:
         print(Fore.RED+Style.BRIGHT+msjError+Fore.RESET+Style.NORMAL)
    return entero


def controlCadenas(leyenda):
    while True:
          cadena = input(leyenda)
          S=cadena.replace(" ", "S")
          validar=S.isalpha()
          if validar==True:
             break
          else:
              print(Fore.RED+Style.BRIGHT+"EN ESTE CAMPO SOLO PUEDE INGRESAR LETRAS"+Fore.RESET+Style.NORMAL)
    return cadena
               
