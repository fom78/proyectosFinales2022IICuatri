# Modulos de consultora_v1
import os


# decora con 2 lineas de caracteres a elejir
def decorar(simbolo1="#", simbolo2="~", limpiar="n", largo=60):
    # y limpia la pantalla al poner "s" en el argumento limpiar
    if limpiar.lower() == "s":
        os.system("cls")
        print(simbolo1*largo)
        print(simbolo2*largo)
    else:
        print(simbolo1*largo)
        print(simbolo2*largo)


# ingreso de datos del trabajador
def ingreso_trabajador(nom_archivo):
    
        nombre = input("Nombre: ").capitalize()
        edad = controlErrorNumero("Edad: ", "\tIngrese su edad en forma numerica")
        dni = controlErrordni("Dni: ", "Ingrese un dni valido")
        profesion = input("Profesion: ").capitalize()
        activo = input("Trabajando (s/n)?: ").capitalize()
        if activo == "S":
            activo = True
        else:
            activo = False
            
        with open("trabajadores.dat","r") as listado: 
            listado.seek(0,os.SEEK_END)
            vacio = listado.tell() == 0
            if vacio == True:
                with open(nom_archivo, "a") as usuarios:
                 usuarios.write(f"{nombre}-{edad}-{dni}-{profesion}-{activo}")
    
            else:
                with open(nom_archivo, "a") as usuarios:
                 usuarios.write(f"\n{nombre}-{edad}-{dni}-{profesion}-{activo}")


def busqueda_por_dni(nom_archivo):                                  # funcionando
    dni = controlErrordni("Ingrese el número de dni del trabajador: ==>")
    with open(nom_archivo, "r") as usuarios:
        for usuario in usuarios.readlines():
            usuario_ok = usuario.replace("\n", "")
            usuario_ok = usuario_ok.split("-")
            if (usuario_ok[2]) == dni:
                return usuario_ok


def controlErrores(leyenda, msjError="\tDebe ingresar un entero", num_opciones=99):
    while True:
        try:
            entero = int(input(leyenda))  # 5
            if entero < num_opciones:  # 5 < 5+1
                break
            else:
                print("\t Por favor ingrese una opcion valida !!!!")
        except ValueError:
            print(msjError)
    return entero


def controlErrorNumero(texto, msjError="Debe ingresar un número entero"):
    while True:
        try:
            entero = int(input(texto))
            break
        except ValueError:
            print(msjError)
    return entero


def controlErrordni(texto, msjError="Debe ingresar un número entero"):
    while True:
        try:
            entero = int(input(texto))
            entero = str(entero)
            if len(entero) == 8:
                break
            else:
                print("ingrese un numero valido de 8 digitos")
        except ValueError:
            print(msjError)
    return entero


def eliminar_linea(nom_archivo, num_linea):  # funcionando
    datos = open(nom_archivo, "r")
    lineas = datos.readlines()
    datos.close()

    datos = open(nom_archivo, "w")

    linea = lineas[num_linea-1]
    lineas.remove(linea)
    for linea in lineas:
        datos.write(linea)
    datos.close()


def encuentra_lineas(nom_archivo, id):  # funcionando
    with open(nom_archivo, 'r') as datos:
        resultado = [numero for numero, linea in enumerate(
            datos.readlines(), start=1) if id in linea]
    return resultado[0]


# funcionando(los parametros son:1ro nombre del archivo, 2do el indice de la lista donde buscar, 3ro la palabra a buscar
def mostrar_dato(nom_archivo, indice_elemento="99", palabra_a_buscar="All"):
    try:
        usuario_ok = []
        elementos = []  # 2do el numero del indice donde se realiza la buqueda,
        with open(nom_archivo, "r") as usuarios1:  # 3ro el elemento a buscar en formato str
            for usuario in usuarios1.readlines():
                usuario = usuario.replace("\n", "")
                usuario = usuario.split("-")
                usuario_ok.append(usuario)
            for elemento in usuario_ok:
                if indice_elemento == "99" or palabra_a_buscar.capitalize() == "All":
                    elementos.append(elemento)
                elif elemento[indice_elemento].capitalize() == palabra_a_buscar.capitalize():
                    elementos.append(elemento)
        return elementos

    except FileNotFoundError:
        with open(nom_archivo, "a") as usuarios1:
            print("no hay registros en la base de datos")
            elementos = [[""]]
        return elementos

    


def imp_lista(listas, lista_unica_si_o_no="no"):

    if listas == []:
        print("No hay registros de usuarios cargados")

    elif lista_unica_si_o_no.lower() == "si":

        if listas[4] == "True":
            listas[4] = "trabajando"
        else:
            listas[4] = "desocupado"
        print(
            f"\nNombre: {listas[0]}, edad: {listas[1]}, dni: {listas[2]}, profesion: {listas[3]}, status: {listas[4]}")

    else:
        # acá listas tiene este valor [[perro,7,marron],[gato,5,blanco],[loro,6,verde]]
        for lista in listas:
            # lista =[perro,7,marron,"\n"] el for itera cada lista y le agrega el salto de linea al final
            lista.append("\n")
            # este if es para que en vez de que salga true o false, salga trabajando o desocupado
            if lista[4] == "True":
                lista[4] = "trabajando"
            else:
                lista[4] = "desocupado"
            print(
                f"\nNombre: {lista[0]}, edad: {lista[1]}, dni: {lista[2]}, profesion: {lista[3]}, status: {lista[4]}")

            # en la iteracion se pide imprimir cada una de las partes de la lista con el f str
            # [perro,7,marron,"\n"] quedaria asi: nombre: perro, edad: 7, dni: marron. y el salto de linea,
            # es para que el proximo trabajador salga en la sig linea


def lista_por_edad(lista):
    usuarios_rango = []
    edad1 = controlErrorNumero("Ingrese edad, desde: ")
    edad2 = controlErrorNumero("hasta: ")
    edadRango = list(range(edad1, edad2+1))
    for usuario in lista:
        for num in edadRango:
            if num == int(usuario[1]):
                usuarios_rango.append(usuario)
    return usuarios_rango


def modificarDatos(archivo, lista, dni):
    for trabajador in lista:
        if trabajador[2] == dni:
            trabajador_elegido = trabajador
            imp_lista(trabajador_elegido, "si")
            if trabajador_elegido[4] == "trabajando":
                trabajador_elegido[4] = "True"
            else:
                trabajador_elegido[4] = "False"
            opcion = controlErrores("""
                    Que dato desea modificar ?

                [1]Nombre
                [2]Edad
                [3]Dni
                [4]Profesion
                [5]Status
                [0]Salir

                ==> """,6)

            if opcion == 1:
                nombreNuevo = input("ingrese nuevo nombre: ").capitalize()
                trabajador.pop(0)
                trabajador.insert(0, nombreNuevo)
                break
            elif opcion == 2:
                edadNueva = controlErrorNumero(
                    "Ingrese la edad nueva: ", "\tIngrese su edad en forma numerica")
                trabajador.pop(1)
                trabajador.insert(1, edadNueva)
                break
            elif opcion == 3:
                dniNuevo = controlErrordni(
                    "Ingrese nuevo N° de dni: ", "Ingrese un dni valido")
                trabajador.pop(2)
                trabajador.insert(2, dniNuevo)
                break

            elif opcion == 4:
                profesionNueva = input(
                    "Ingrese la profesion nueva: ").capitalize()
                trabajador.pop(3)
                trabajador.insert(3, profesionNueva)
                break
            elif opcion == 5:
                activoNuevo = input(
                    "Ingrese el status: A/I Activo ó inactivo ==> ").capitalize()
                if activoNuevo == "A":
                    activoNuevo = "True"
                else:
                    activoNuevo = "False"
                trabajador.pop(4)
                trabajador.insert(4, activoNuevo)
                break
            elif opcion == 0:
                break

    with open(archivo, "w") as archivo1:
        contador = 0
        for elemento in lista:
            if contador == 0:
                archivo1.writelines(
                    f"{elemento[0]}-{elemento[1]}-{elemento[2]}-{elemento[3]}-{elemento[4]}")
            else:
                archivo1.writelines(
                    f"\n{elemento[0]}-{elemento[1]}-{elemento[2]}-{elemento[3]}-{elemento[4]}")
            contador = contador + 1
