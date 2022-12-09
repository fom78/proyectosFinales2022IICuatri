from persistenciaTrabajadores import recuperarTrabajadores
from validaciones import edadValida

def mostrarTrabajadoresActivos(listaTrabajadores):
    contador = 1
    for i in listaTrabajadores:
        if (i["estado"] == True):
            nombre = i["nombre"]
            edad = i["edad"]
            dni = i["dni"]
            profesion = i["profesion"]
            print(f"#{contador} > NOMBRE: {nombre:15} | EDAD: {edad} | DNI: {dni:3} | PROFESION: {profesion:5}")
            contador = contador + 1
    if contador == 1:
        print("¡ NO SE ENCONTRARON TRABAJADORES ACTIVOS !")
    print("")
    
def mostrarTrabajadoresDesocupados(listaTrabajadores):
    contador = 1
    for i in listaTrabajadores:
        if (i["estado"] == False):
            nombre = i["nombre"]
            edad = i["edad"]
            dni = i["dni"]
            profesion = i["profesion"]
            print(f"#{contador} > NOMBRE: {nombre:15} | EDAD: {edad} | DNI: {dni:3} | PROFESION: {profesion:5}") 
            contador = contador + 1
    if contador == 1:
        print("¡ NO SE ENCONTRARON TRABAJADORES DESOCUPADOS !")
    print("")

def mostrarDesocupadosPorEdad(listaTrabajadores):
    while True:
        try:
            edadMinima = int(input(">>> INGRESE LA EDAD MINIMA: "))
            if edadValida(edadMinima):
                break
            else:
                print("LA EDAD INGRESADA DEBE SER UNA ENTRE 18-100")
        except:
            print("LA EDAD INGRESADA NO ES UN VALOR VALIDO")

    while True:
        try:
            edadMaxima = int(input(">>> INGRESE LA EDAD MAXIMA: "))
            if edadMaxima >= edadMinima:
                if edadValida(edadMaxima):
                    break
                else:
                    print("LA EDAD INGRESADA DEBE SER UNA ENTRE 18-100")
            else:
                print(f"ERROR > LA EDAD MAXIMA [{edadMaxima}] NO PUEDE SER MENOR A LA EDAD MINIMA [{edadMinima}]")
        except:
            print("LA EDAD INGRESADA NO ES UN VALOR VALIDO")
    print("")
    print(f">>> LISTADO DE TRABAJADORES DESOCUPADOS ENTRE {edadMinima} - {edadMaxima} AÑOS")
    print("")
    contador = 1
    for i in listaTrabajadores:
        if (i["edad"] >= edadMinima) & (i["edad"] <= edadMaxima):
            if (i["estado"] == False):
                nombre = i["nombre"]
                edad = i["edad"]
                dni = i["dni"]
                profesion = i["profesion"]
                print(f"#{contador} > NOMBRE: {nombre:15} | EDAD: {edad} | DNI: {dni:3} | PROFESION: {profesion:5}")
                contador = contador + 1

    if contador == 1:
        print(f" > NO HAY TRABAJADORES DESOCUPADOS ENTRE {edadMinima}-{edadMaxima}")
    print("")

def mostrarTrabajadoresPorProfesion(listaTrabajadores):
    contador = 1
    filtroProfesion = input(">>> INGRESE PROFESION: ")
    print("")
    print(">>> LISTADO DE TRABAJADORES CON PROFESION", filtroProfesion.upper())
    print("")
    for i in listaTrabajadores:
        profesion = str(i["profesion"]).lower()
        filtroProfesion = filtroProfesion.lower()
        if profesion == filtroProfesion:
            nombre = i["nombre"]
            edad = i["edad"]
            dni = i["dni"]
            estado = i["estado"]
            if estado ==  True:
                estado = "ACTIVO"
            elif estado == False:
                estado == "INACTIVO"
            print(f"#{contador} > NOMBRE: {nombre:15} | EDAD: {edad} | DNI: {dni:3} | ESTADO: {estado:5}")
            contador = contador + 1
    if contador == 1:
        print(f">>> NO HAY TRABAJADORES CON PROFESION {filtroProfesion} CARGADOS EN ESTE MOMENTO")
    print("")