"""Este Modulo contiene las funciones a utilizar para decorar la salida del programa"""

import os
def decorarTitulos(frase,caracter, cantidad):
   #os.system("cls")
   print(caracter*cantidad)
   print(frase.center(50,"-"))
   print(caracter*cantidad)


def decorarMenu():
   lineaDibujada="▄"*5+"█"+"▄"*44
   lineaDibujada2="▄"*50
   print(lineaDibujada2)
   print(f"█ Nº █\t\t\t\t\tOpcion█")
   print(lineaDibujada)
   listaDeOpciones={
      1:"Gestion de Trabajadores",
      2:"Reportes",
      3:"Cambiar status trabajador",
      4:"Listado de Trabajadores",
      0:"Salir"
      }
   
   for clave,valor in listaDeOpciones.items():
      print("█{:2}  █{:>40}█".format(clave,valor))
      print(lineaDibujada) 
      
   print()   



def decorarMenuTrabajador():
   lineaDibujada="▄"*5+"█"+"▄"*44
   lineaDibujada2="▄"*50
   print(lineaDibujada2)
   print(f"█ Nº █\t\t\t\t\tOpcion█")
   print(lineaDibujada)
   listaDeOpciones={
      1:"Ingresar nuevo Trabajador",
      2:"Modificar datos Trabajador",
      3:"Eliminar trabajador",
      0:"Volver al menu principal"
      }
   
   for clave,valor in listaDeOpciones.items():
      print("█{:2}  █{:>40}█".format(clave,valor))
      print(lineaDibujada) 
      
   print()   

def decorarListaTrabajador(listado):
   encabezado = '{:10}{:10}{:10}{:10}{:10}{:10}'.format("NOMBRE","APELLIDO","EDAD","DNI","PROFESION","ESTADOACTUAL")
   print(encabezado)
   for linea in listado:
      linea= '{:10}{:10}{:10}{:10}{:10}{:10}'.format(linea["nombre"],linea["apellido"],linea["edad"],linea["dni"],linea["profesion"],linea["estadoactual"])
      print(linea)