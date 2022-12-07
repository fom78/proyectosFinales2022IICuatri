from validaciones import validarIngresoEntero

def obtenerTrabajadores(nombreArchivo):
	try:
		archivo = open(nombreArchivo, "r")
	except FileNotFoundError:
		archivo = open(nombreArchivo, "a")
		archivo.write("45434543,Juan,23,electricista,True")
		archivo.close()
		archivo = open(nombreArchivo, "r")

	trabajadores=[]
	for linea in archivo.readlines():
		trabajador=linea.replace("\n", "")
		trabajador=trabajador.split(",")
		trabajador= {"dni":int(trabajador[0]),"nombre":(trabajador[1]),"edad":int(trabajador[2]),"profesion":(trabajador[3]),"estado":(trabajador[4])}
		trabajadores.append(trabajador)
	archivo.close()
	return trabajadores


def agregarTrabajadores(listado):
	dni = validarIngresoEntero("dni: ")
	nombre = input("nombre: ")
	edad = validarIngresoEntero("edad: ")
	profesion = input("profesion: ")
	estado = input("está empleado? s/n: ")
	if estado == "s":
		estado = True
	else:
		estado = False
	
	# Crea el trabajador y lo guarda en el listado
	trabajador = {"dni": dni,"nombre":nombre,"edad":edad,"profesion":profesion,"estado":estado}
	listado.append(trabajador)

	# Agrega al trabajador en el archvio
	archivo = open("trabajadores.txt", "a")
	linea = f"\n{dni},{trabajador['nombre']},{trabajador['edad']},{trabajador['profesion']},{trabajador['estado']}"
	archivo.write(linea)
	archivo.close()

# función para generar una cadena con el diccionario de cada trabajador
def salida(i):
	print(f"DNI: {i['dni']} Nombre: {i['nombre']} Edad:{i['edad']} Profesion: {i['profesion']} Estado: {i['estado']}" ) 

# funcion para modificar un trabajador

def modificarTrabajador(listado, dni):
	for trab in listado:
		if trab["dni"] == dni:
			salida(trab)
			nombre = input("Nombre: (presiona Enter para mantener) ")
			if nombre == "":
				nombre = trab["nombre"]
			edad = validarIngresoEntero("Edad: ")
			edad = trab["edad"]
			profesion = input("Profesion: (presione Enter para mantener) ")
			if profesion == "":
				profesion = trab["profesion"]
			estado = trab["estado"]
			
			trab["nombre"]=nombre
			trab["edad"]=edad
			trab["profesion"]=profesion
			trab["estado"]=estado
			break
	
	archivo = open("trabajadores.txt", "w")
	cont = []
	for trab in listado:
		linea = f"\n{trab['dni']},{trab['nombre']},{trab['edad']},{trab['profesion']},{trab['estado']}"
		cont.append(linea)
	cont[0] = cont[0].replace("\n", "")
	archivo.writelines(cont)
	archivo.close()

def eliminarTrabajador(listado, dni):
	indice = 0
	for trab in listado:
		if trab["dni"] == dni:
			print(trab)
			listado.pop(indice)
			break
		indice = indice + 1

	archivo = open("trabajadores.txt", "w")
	cont = []
	for trab in listado:
		linea = f"\n{trab['dni']},{trab['nombre']},{trab['edad']},{trab['profesion']},{trab['estado']}"
		cont.append(linea)
	cont[0] = cont[0].replace("\n", "")
	archivo.writelines(cont)
	archivo.close()


def modificarEstadoTrabajador(listado, dni):
	for trab in listado:
		if trab["dni"] == dni:
			salida(trab)
			nombre = trab["nombre"]
			edad = trab["edad"]
			profesion = trab["profesion"]
			estado = input("Para pasar a trabajador ocupado, persione 's', para trabajador desocupado, presion 'n': ")
			if estado == "s":
				estado = True
			else:
				estado = False	
			trab["nombre"]=nombre
			trab["edad"]=edad
			trab["profesion"]=profesion
			trab["estado"]=estado
			break
	
	archivo = open("trabajadores.txt", "w")
	cont = []
	for trab in listado:
		linea = f"\n{trab['dni']},{trab['nombre']},{trab['edad']},{trab['profesion']},{trab['estado']}"
		cont.append(linea)
	cont[0] = cont[0].replace("\n", "")
	archivo.writelines(cont)
	archivo.close()



