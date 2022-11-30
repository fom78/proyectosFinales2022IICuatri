from decoracion import decorar


def validarIngresoEntero(leyenda=" "):
  while True:
    try:
      entero = int(input(leyenda))
      break
    except ValueError:
      print("Por favor debe ingresar un numero entero.")
      decorar()
  return entero