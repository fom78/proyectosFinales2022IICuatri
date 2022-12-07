from ABMtrabajadores import salida

# funciones para diferenciar trabajadores ocupados y desocupados
def comparaTrue(lista):
	for var in lista:
		if var["estado"] == True:
			salida(var)
		elif var["estado"] == "True":
			salida(var)

def comparaFalse(lista):
	for var in lista:
		if var["estado"] == False:
			salida(var)
		elif var["estado"] == "False":
			salida(var)