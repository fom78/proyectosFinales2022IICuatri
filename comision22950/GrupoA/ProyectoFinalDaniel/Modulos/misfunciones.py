import os
from os import system
from Modulos.decoradores import cabecera, pie, cabeceraJuegos
from Modulos.juegodados import juegoDados
cPath = os.getcwd() + "/"

def archivosyCarpetas():
    cCarpeta = "Datos"
    siExiste(cCarpeta, True) # Verificar si existe la Carpeta Datos con parametro True
    os.chdir(cPath + cCarpeta)
    
    archivoDato = "jugador.dat"
    estructura = {"dni":"99999999", "nombre":"Anonimo","activo":True, "juego1": 0, "acumulado": 0, "juego2": 0, "ganapc": 0, "ganausu": 0, "empate": 0 }
    siExiste(archivoDato, False, estructura) # Verificar sie existe el archivo con parametro False
    
    archivoDato = "pipati.dat"
    siExiste(archivoDato, False) # Verificar sie existe el archivo con parametro False
    
    archivoDato = "dados.dat"
    siExiste(archivoDato, False) # Verificar sie existe el archivo con parametro False
    
    os.chdir(cPath)
    
    return None

def siExiste(carpetaArchivo, esCarpeta, estructura = ""):
    lExiste = os.path.exists(carpetaArchivo) # Verifica si existe la carpeta y si no la crea cuando esCarpeta = True, 
    if not lExiste:
        if esCarpeta:
            os.mkdir(cPath + carpetaArchivo)
        else:
            crearBaseDatos(carpetaArchivo, estructura, "a+")
    return None


def crearBaseDatos(nombreBase, estructura, formaAbrir):  # ("a" Append, "r" read, lectura, "w" sólo escritura(se borrará si existe con el mismo nombre), r+ abre el archivo para lectura y escritura)
    archivo = open(nombreBase, formaAbrir)
    jugador = f"{estructura['dni']},{estructura['nombre']},{estructura['activo']},{estructura['juego1']},{estructura['acumulado']},{estructura['juego2']},{estructura['ganapc']},{estructura['ganausu']},{estructura['empate']}\n"
    archivo.write(jugador)
    archivo.close()
    return None


def abrirBaseDatos(nombreBase, formaAbrir):  # ("a" Append, "r" read, lectura, "w" sólo escritura(se borrará si existe con el mismo nombre), r+ abre el archivo para lectura y escritura)
    archivo = open(nombreBase, formaAbrir)
    return (archivo)

def buscaJugador(titulo, opcionTitulo, condicion):
    while True:
        system("cls")
        cabecera(titulo, opcionTitulo)
        try:
            numeroDocumento = ingresoDocumento("Ingrese su Nro. de Documento de 8 dígitos, (0) Para Retornar al Menú Anterior: ")
        except ValueError:
            print("Debes ingresar un número!!!")
            system("pause")
            continue
        numeroDocumento = int(numeroDocumento)
        if numeroDocumento == 0:
            break
        elif len(str(numeroDocumento)) != 8:
            print(f"Verifique su numero de documento: {numeroDocumento} porque no tiene 8 dígitos")
            system("pause")
            continue
        else:
            encontrado = [False]
            nroRegistro = [0]
            datosJugador = verificaJugador(numeroDocumento, encontrado, nroRegistro)
            if condicion == "A":  # Verifica, de no existir el DNI, permite Agregar
                if not encontrado[0]:
                    print(f"Su numero de documento: {numeroDocumento} no se encuentra")
                    elije = input("Sí desea agregarlo Pulse (S), caso contrario cualquier tecla: ")
                    if elije.upper() == "S":
                        datosJugador = agregaJugador(numeroDocumento)
                        print(f"Jugador agregado con éxito!!")
                    else:
                        print(f"No se realizó el ingreso del nuevo Jugador")
                else:
                    informeJugador(datosJugador) 
                system('pause')
            elif condicion == "M":  # Modificar Jugador
                if encontrado[0]:
                    informeJugador(datosJugador)
                    datosJugador = modificaJugador(datosJugador, nroRegistro)
                else:
                    print(f'Jugador con DNI: {numeroDocumento} No Encontrado!!!')
                    system("pause")
            elif condicion == "E":  # Eliminar un Jugador x DNI
                if encontrado[0]:
                    informeJugador(datosJugador)
                    elije = input("Se procederá a Eliminar el Jugador Pulse (S), caso contrario cualquier tecla: ")
                    if elije.upper() == "S":
                        datosJugador = eliminaJugador(datosJugador)
                        print(f"Jugador Eliminado con éxito!!")
                    else:
                        print(f"No se realizó la eliminación del Jugador")    
                else:
                    print(f'Jugador con DNI: {numeroDocumento} No Encontrado!!!')
                system("pause")
            elif condicion == "T":  # Activa/Desactiva Jugador
                if encontrado[0]:
                    informeJugador(datosJugador)
                    elije = input("Se procederá a Cambiar el Estado del Jugador Pulse (S), caso contrario cualquier tecla: ")
                    if elije.upper() == "S":
                        datosJugador = cambiaEstadoJugador(datosJugador)
                        print(f"Tarea realizada con éxito!!")
                    else:
                        print(f"No se llevó a cabo la Operación")    
                else:
                    print(f'Jugador con DNI: {numeroDocumento} No Encontrado!!!')
                system("pause")
            elif condicion == "J":  # Ingreso al Módulo de Juego x DNI 
                if encontrado[0]:
                    while True:
                        system("cls")
                        informeJugador(datosJugador)
                        cabeceraJuegos(1)
                        try:
                            nElije = int(input("Ingrese una opción: "))
                        except ValueError:
                            print("Debes ingresar un número!!!")
                            system("pause")
                            continue
                        if nElije == 0:
                            break
                        elif nElije == 1:
                            juegoDados(2)
                        elif nElije == 2:
                            titulo = "Juego de Pidra - Papel - Tijera"
                else:
                    print(f'Jugador con DNI: {numeroDocumento} No Encontrado!!!')
                    system("pause")
    return None

def ingresoDocumento(mensaje):
    nroDocumento = float(input(mensaje))
    while nroDocumento != int(nroDocumento) or nroDocumento < 0:
        nroDocumento = float(input("Error. " + mensaje))
    return (nroDocumento)

    
def verificaJugador(nroDocumento, encontrado, nroRegistro):
    cCarpeta = "Datos"
    os.chdir(cPath + cCarpeta)
    archivoDato = "jugador.dat"
    cBaseDato = abrirBaseDatos(archivoDato, "r+")
    
    #estructura = {"dni":"99999999", "nombre":"Anonimo","activo":True, "juego1": 0, "acumulado": 0, "juego2": 0, "ganapc": 0, "ganausu": 0, "empate": 0 }
    
    listaJugadores = []
    listaJugadores = obtenerLista(listaJugadores, cBaseDato)
    
    nroRecno = 0
    for jugador in listaJugadores:
        nroRecno += 1
        if jugador["dni"] == nroDocumento:
            encontrado[0] = True
            nroRegistro[0] = nroRecno
            break        
    cBaseDato.close()
    os.chdir(cPath)
    return (jugador)

def agregaJugador(nroDocumento):
    while True:
        try:
            nombre = input("Ingrese su Nombre: ")
        except ValueError:
            print("Debes ingresar un Nombre por favor!!!")
            system("pause")
            continue
        if len(nombre) == 0:
            print(f"No deje Nombre vacío: {nombre}")
            system("pause")
            continue
        estructura = {"dni":str(nroDocumento),"nombre":nombre,"activo":True, "juego1": 0, "acumulado": 0, "juego2": 0, "ganapc": 0, "ganausu": 0, "empate": 0 }
        jugador = f"{estructura['dni']},{estructura['nombre']},{estructura['activo']},{estructura['juego1']},{estructura['acumulado']},{estructura['juego2']},{estructura['ganapc']},{estructura['ganausu']},{estructura['empate']}\n"
        cCarpeta = "Datos"
        os.chdir(cPath + cCarpeta)
        archivoDato = "jugador.dat"
        cBaseDato = abrirBaseDatos(archivoDato, "a")
        cBaseDato.write(jugador)
        cBaseDato.close()
        os.chdir(cPath)
        break
    return (estructura)

def modificaJugador(datosJugador, nroRegistro):
    error = False
    copiaDatosJugador = datosJugador
    nRecnoActual = nroRegistro
    nroDocumentoAnterior = datosJugador['dni']
    while True:
        if not error:
            nroDocumento = datosJugador['dni']
            nombreAnterior = nombre = datosJugador['nombre']
            activo = datosJugador['activo']
            juego1 = datosJugador['juego1']
            acumulado = datosJugador['acumulado']
            juego2 = datosJugador['juego2']
            ganapc = datosJugador['ganapc']
            ganausu = datosJugador['ganausu']
            empate = datosJugador['empate']
        else:
            nroDocumento = copiaDatosJugador['dni']
            nombreAnterior = nombre = copiaDatosJugador['nombre']
            activo = copiaDatosJugador['activo']
            juego1 = copiaDatosJugador['juego1']
            acumulado = copiaDatosJugador['acumulado']
            juego2 = copiaDatosJugador['juego2']
            ganapc = copiaDatosJugador['ganapc']
            ganausu = copiaDatosJugador['ganausu']
            empate = copiaDatosJugador['empate']
            error = False
        estructura = {"dni":str(nroDocumento),"nombre":nombre,"activo":activo, "juego1": juego1, "acumulado": acumulado, "juego2": juego2, "ganapc": ganapc, "ganausu": ganausu, "empate": empate }
        jugador = f"{estructura['dni']},{estructura['nombre']},{estructura['activo']},{estructura['juego1']},{estructura['acumulado']},{estructura['juego2']},{estructura['ganapc']},{estructura['ganausu']},{estructura['empate']}\n"
        try:
            print(f"Su Nro. de Documento: {nroDocumento:<25}", end= " ")
            nroDocumento = ingresoDocumento("Su nuevo Nro. de Documento de 8 dígitos, (0) Para Retornar: ")
            nroDocumento = int(nroDocumento)
            if nroDocumento == 0:
                break
            elif len(str(nroDocumento)) != 8:
                print(f"Verifique su numero de documento: {nroDocumento} porque no tiene 8 dígitos")
                system("pause")
                continue
            else:
                encontrado = [False]
                nroRegistro = [0]
                datosJugador = verificaJugador(nroDocumento, encontrado, nroRegistro) 
                if encontrado[0] and nroRegistro[0] != nRecnoActual[0]:
                    print(f'Ese DNI: {nroDocumento}  ya se Encuentra y pertenece a: {datosJugador["nombre"]}')
                    system('pause')
                    break
            
            print(f"Nombre actual {nombre:<25}", end=" ")
            nombre = input("Su Nuevo Nombre: ")
            if len(nombre) == 0:
                nombre = nombreAnterior
            if activo:
                esActivo = "Activo"
            else:
                esActivo = "      "
            print(f"Estado actual {esActivo:<25}", end=" ")
            esActivo = input("Estado (S)->Activo, (N)->No Activo: ")
            if esActivo.upper() == "S":
                activo = True
            elif esActivo.upper() == "N":
                activo = False
            print(f"Partidas de Dados Actuales {juego1:<25}", end=" ")
            juego1 = abs(int(input("Partidas Actuales: ")))
            print(f"Puntos Acumulados actuales {acumulado:<25}", end=" ")
            acumulado = abs(int(input("Nuevos Puntos Acumulados: ")))
            print(f"Partidas de PIPATI Actuales {juego2:<25}", end=" ")
            juego2 = abs(int(input("Partidas Actuales: ")))
            print(f"Partidas Ganadas PC actuales {ganapc:<25}", end=" ")
            ganapc = abs(int(input("Nuevas Partidas Ganadas Pc: ")))
            print(f"Partidas Ganadas Jugador actuales {ganausu:<25}", end=" ")
            ganausu = abs(int(input("Nuevas Partidas Ganadas Jugador: ")))
            print(f"Partidas Empatadas actuales {empate:<25}", end=" ")
            empate = abs(int(input("Nuevas Partidas Empatadas: ")))
            
        except ValueError:
            print("Debes ingresar un Valor Numérico por favor!!!")
            error = True
            system("pause")
            continue
        
        
        if juego1 == 0:
            acumulado = 0
        if juego2 == 0:
            ganapc = 0
            ganausu = 0
            empate = 0
        else:
            juego2 = ganapc + ganausu + empate

        cCarpeta = "Datos"
        os.chdir(cPath + cCarpeta)
        archivoDato = "jugador.dat"
        cBaseDato = abrirBaseDatos(archivoDato, "r+")
        listaJugadores = []
        listaJugadores = obtenerLista(listaJugadores, cBaseDato)
        cBaseDato.close()
        for jugador in listaJugadores:
            if jugador["dni"] == nroDocumentoAnterior:
                jugador['dni'] = nroDocumento
                jugador['nombre'] = nombre
                jugador['activo'] = activo
                jugador['juego1'] = juego1
                jugador['acumulado'] = acumulado
                jugador['juego2'] = juego2
                jugador['ganapc'] = ganapc
                jugador['ganausu'] = ganausu
                jugador['empate'] = empate
                break
        guardaLista(archivoDato, listaJugadores)
        os.chdir(cPath)
        break
    return (jugador)

def eliminaJugador(datosJugador):
    nroDocumento = datosJugador['dni']
    cCarpeta = "Datos"
    os.chdir(cPath + cCarpeta)
    archivoDato = "jugador.dat"
    cBaseDato = abrirBaseDatos(archivoDato, "r+")
    listaJugadores = []
    listaJugadores = obtenerLista(listaJugadores, cBaseDato)
    cBaseDato.close()
    for jugador in listaJugadores:
        if jugador["dni"] == nroDocumento:
            listaJugadores.remove(jugador)
            break
    guardaLista(archivoDato, listaJugadores)
    os.chdir(cPath)
    return (jugador)

def cambiaEstadoJugador(datosJugador):
    nroDocumento = datosJugador['dni']
    activo = datosJugador['activo']
    print(f"Activo: {activo:<25}", end=" ")
    esActivo = input("Estado (S)->Activo, (N)->No Activo: ")
    if esActivo.upper() == "S":
        activo = True
    elif esActivo.upper() == "N":
        activo = False
    cCarpeta = "Datos"
    os.chdir(cPath + cCarpeta)
    archivoDato = "jugador.dat"
    cBaseDato = abrirBaseDatos(archivoDato, "r+")
    listaJugadores = []
    listaJugadores = obtenerLista(listaJugadores, cBaseDato)
    cBaseDato.close()
    for jugador in listaJugadores:
        if jugador["dni"] == nroDocumento:
            jugador['activo'] = activo
            break
    guardaLista(archivoDato, listaJugadores)
    os.chdir(cPath)
    return (jugador)

def guardaLista(archivoDato, listaJugadores):
    cBaseDato = abrirBaseDatos(archivoDato, "w")
    for jugador in listaJugadores:
        nroDocumento = jugador['dni']
        nombre = jugador['nombre']
        activo = jugador['activo']
        juego1 = jugador['juego1']
        acumulado = jugador['acumulado']
        juego2 = jugador['juego2']
        ganapc = jugador['ganapc']
        ganausu = jugador['ganausu']
        empate = jugador['empate']
        estructura = {"dni":str(nroDocumento),"nombre":nombre,"activo":activo, "juego1": juego1, "acumulado": acumulado, "juego2": juego2, "ganapc": ganapc, "ganausu": ganausu, "empate": empate }
        jugador = f"{estructura['dni']},{estructura['nombre']},{estructura['activo']},{estructura['juego1']},{estructura['acumulado']},{estructura['juego2']},{estructura['ganapc']},{estructura['ganausu']},{estructura['empate']}\n"
        cBaseDato.write(jugador)
    
    cBaseDato.close()
    return None


def obtenerLista(listaJugadores, cBaseDato):
    for linea in cBaseDato.readlines():
        jugador = linea.replace('\n','')
        jugador = jugador.split(',')
        jugador = {"dni":int(jugador[0]),"nombre":jugador[1],"activo":jugador[2],"juego1":int(jugador[3]),"acumulado":int(jugador[4]),"juego2":int(jugador[5]),"ganapc":int(jugador[6]),"ganausu":int(jugador[7]),"empate":int(jugador[8])}
        listaJugadores.append(jugador)
    return listaJugadores


def string(cadena, cantcaracteres):
    nCanCara = len(cadena)
    if nCanCara <= cantcaracteres:
        cCadena = cadena.ljust(cantcaracteres)
    else:
        cCadena = cadena[0:cantcaracteres]
    return(cCadena)

def informeJugador(datosJugador):
    renglon = "|           |    DNI    |       Nombre       |Activo|Pdas. Dados|Acumulados |Pdas.PiPaTi|  Gdas. Pc |Gdas. Jdor.|  Empates  |"
    print("-"*125)
    print(renglon)
    cNombre = string(datosJugador['nombre'], 20)
    i = 1
    print(f"|Jugador:{i:^3}", end ="")
    print(f"|{datosJugador['dni']:^11.0f}|{cNombre}|{datosJugador['activo']:^6}|{datosJugador['juego1']:^11.0f}|{datosJugador['acumulado']:^11.0f}|{datosJugador['juego2']:^11.0f}|{datosJugador['ganapc']:^11.0f}|{datosJugador['ganausu']:^11.0f}|{datosJugador['empate']:^11.0f}|")
    print("-"*125)    
    pie()
    return None

def informeJugadores(titulo, opcionTitulo):
    system("cls")
    cabecera(titulo, opcionTitulo)
    elije = input("Sí procederá a Imprimir el Informe de Jugadores. Pulse (S) para realizarlo, caso contrario cualquier tecla: ")
    if elije.upper() == "S":
        cCarpeta = "Datos"
        os.chdir(cPath + cCarpeta)
        archivoDato = "jugador.dat"
        cBaseDato = abrirBaseDatos(archivoDato, "r+")
        listaJugadores = []
        listaJugadores = obtenerLista(listaJugadores, cBaseDato)
        cBaseDato.close()
        renglon = "|           |    DNI    |       Nombre       |Activo|Pdas. Dados|Acumulados |Pdas.PiPaTi|  Gdas. Pc |Gdas. Jdor.|  Empates  |"
        print("-"*125)
        print(renglon)
        i = 1
        sumaPdasDados = 0
        sumaAcumulado = 0
        sumaGanadasPc = 0
        sumaPdasPiPaTi = 0
        sumaGanadasUsu = 0
        sumaEmpatadas = 0
        for jugador in listaJugadores:
            cNombre = string(jugador['nombre'], 20)
            sumaPdasDados += jugador['juego1']
            sumaAcumulado += jugador['acumulado']
            sumaPdasPiPaTi += jugador['juego2']
            sumaGanadasPc += jugador['ganapc']
            sumaGanadasUsu += jugador['ganausu']
            sumaEmpatadas += jugador['empate']
            print(f"|Jugador:{i:^3}", end ="")
            print(f"|{jugador['dni']:^11.0f}|{cNombre}|{jugador['activo']:^6}|{jugador['juego1']:^11.0f}|{jugador['acumulado']:^11.0f}|{jugador['juego2']:^11.0f}|{jugador['ganapc']:^11.0f}|{jugador['ganausu']:^11.0f}|{jugador['empate']:^11.0f}|")
            i += 1
        print("-"*125)
        print(f'|                T o t a l e s :                    |', end="")
        print(f"{sumaPdasDados:^11.0f}|{sumaAcumulado:^11.0f}|{sumaPdasPiPaTi:^11.0f}|{sumaGanadasPc:^11.0f}|{sumaGanadasUsu:^11.0f}|{sumaEmpatadas:^11.0f}|")
        pie()
        system("pause")
    return None
