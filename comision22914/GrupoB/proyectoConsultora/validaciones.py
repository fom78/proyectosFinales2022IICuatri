def validarIngresoEntero(leyenda):
	while True:
		try:
			entero = int(input(leyenda))
			break
		except ValueError:
			print("El número debe ser un entero")
	return entero