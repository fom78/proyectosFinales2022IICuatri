def recuperarTrabajadores():
    listaTrabajadores = []
    archivo = open("trabajadores.dat", "r")
    for linea in archivo:
        datoLista = linea.replace("\n", "")
        datoLista = datoLista.split("-")
        if datoLista[4] == "True":
            estado = True
        else:
            estado = False
        datoDiccionario = {"nombre": datoLista[0], "edad": int(datoLista[1]), "dni": int(datoLista[2]), "profesion": datoLista[3], "estado": estado}
        listaTrabajadores.append(datoDiccionario)
    archivo.close()
    return listaTrabajadores

def almacenarTrabajador(dni, nombre, edad, profesion, estado):
    archivo = open("trabajadores.dat", "a")
    linea = (f"{nombre}-{edad}-{dni}-{profesion}-{estado}\n")
    archivo.write(linea)
    archivo.close()

def actualizarTrabajador(listaTrabajadores):
    archivo = open("trabajadores.dat", "w")
    listaArchivo = []
    for i in listaTrabajadores:
        linea = f"{i['nombre']}-{i['edad']}-{i['dni']}-{i['profesion']}-{i['estado']}\n"
        listaArchivo.append(linea)
    
    archivo.writelines(listaArchivo)
    archivo.close()
    