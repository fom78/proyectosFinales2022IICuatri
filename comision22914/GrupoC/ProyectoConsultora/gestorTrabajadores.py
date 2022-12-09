from persistenciaTrabajadores import actualizarTrabajador, almacenarTrabajador
from validaciones import dniValido, edadValida, dniExiste

def ingresarTrabajador(listaTrabajadores):
    while True: 
        try:
            dni = int(input(">>> INGRESAR DNI: "))
            if dniValido(dni): # VERIFICO QUE SEA VALIDO
                if not dniExiste(dni,listaTrabajadores): # VERIFICO QUE NO EXISTA EN LA LISTA
                    break
                else:
                    print(f">>> YA EXISTE UN TRABAJADOR INGRESADO CON EL DNI {dni}")
            else:
                print(f">>> EL DNI {dni} NO ES VALIDO")
        except:
            print(">>> DATO NO VALIDO")

    nombre = input(">>> INGRESE NOMBRE: ")

    while True:
        try:
            edad = int(input(">>> INGRESE EDAD: "))
            if edadValida(edad):
                break
            else:
                print(">>> LA EDAD INGRESADA DEBE SER UNA ENTRE 18-100")
        except:
            print(">>> LA EDAD INGRESADA DEBE SER UNA ENTRE 18-100")
    
    profesion = input(">>> INGRESAR PROFESION: ")

    print(">>> ESTADO:")
    print(" >>> [1] ACTIVO")
    print(" >>> [2] INACTIVO")
    while True:
        try:
            estado = int(input(" >>> OPCION: "))
            if estado == 1:
                estado = True
                break
            elif estado == 2:
                estado = False
                break
            else:
                print(">>> LA OPCION NO ES VALIDA")
        except:
            print(">>> LA OPCION NO ES VALIDA")
    print("")
    listaTrabajadores.append({"nombre": nombre, "edad": edad, "dni": dni, "profesion": profesion, "estado": estado})
    almacenarTrabajador(dni, nombre, edad, profesion, estado)
    print(f"     >>> USUARIO [{nombre}] INGRESADO EXITOSAMENTE <<<")
    print("")

def modificarTrabajador(listaTrabajadores):
    huboModificacion = True
    while True: 
        try:
            dni = int(input(">>> INGRESAR DNI: "))
            if dniValido(dni): # VERIFICO QUE SEA VALIDO
                if dniExiste(dni,listaTrabajadores): # VERIFICO QUE EXISTA EN LA LISTA
                    break
                else:
                    print(f">>> NO SE ENCUENTRA TRABAJADOR CON DNI {dni}")
            else:
                print(f">>> EL DNI {dni} NO ES VALIDO")
        except:
            print(">>> DATO NO VALIDO")
    print("")

    for i in listaTrabajadores:
        if i["dni"] == dni:
            nombre = i["nombre"]
            edad = i["edad"]
            profesion = i["profesion"]
            print(f"TRABAJADOR > {nombre} | {dni} | {edad} | {profesion} ")
            print("")       
            newNombre = input(">>> INGRESE NUEVO NOMBRE    | [ENTER] NO MODIFICAR: ")
            while True:
                try:
                    newEdad = (input(">>> INGRESE NUEVA EDAD      | [ENTER] NO MODIFICAR: "))
                    if newEdad == "":
                        break
                    else:
                        newEdad = int(newEdad)
                        if edadValida(newEdad):
                            break
                        else:
                            print(">>> LA EDAD INGRESADA DEBE SER UNA ENTRE 18-100")
                except:
                    print(">>> LA EDAD INGRESADA DEBE SER UNA ENTRE 18-100")
            newProfesion = input(">>> INGRESE NUEVA PROFESION | [ENTER] NO MODIFICAR: ")
            print("")
            if newNombre != "":
                i["nombre"] = newNombre
                nombre = newNombre
                print(f" > NOMBRE MODIFICADO CON EXITO - NOMBRE ACTUAL -> {newNombre}")
            if newEdad != "":
                i["edad"] = newEdad
                edad = newEdad
                print(f" > EDAD MODIFICADA CON EXITO - EDAD ACTUAL -> {newEdad}")   
            if newProfesion != "":
                i["profesion"] = newProfesion
                profesion = newProfesion
                print(f" > PROFESION MODIFICADA CON EXITO - PROFESION ACTUAL -> {newProfesion}")
            if (newNombre == "") & (newEdad == "") & (newProfesion == ""):
                print(" > NINGUN DATO HA SIDO MODIFICADO")
                huboModificacion = False
            print("")
            print(f"TRABAJADOR > {nombre} | {dni} | {edad} | {profesion}")
            print("")
            break

    if huboModificacion:
        actualizarTrabajador(listaTrabajadores)         
        
def eliminarTrabajador(listaTrabajadores):
    while True: 
        try:
            dni = int(input(">>> INGRESAR DNI: "))
            if dniValido(dni): # VERIFICO QUE SEA VALIDO
                if dniExiste(dni,listaTrabajadores): # VERIFICO QUE EXISTA EN LA LISTA
                    break
                else:
                    print(f">>> NO SE ENCUENTRA TRABAJADOR CON DNI {dni}")
            else:
                print(f">>> EL DNI {dni} NO ES VALIDO")
        except:
            print(">>> DATO NO VALIDO")
    print("")
    indice = 0       
    for i in listaTrabajadores:
        if i["dni"] == dni:
            nombre = i["nombre"]
            edad = i["edad"]
            profesion = i["profesion"]
            estado = i["estado"]
            if estado == True:
                estado = "Activo"
            else:
                estado = "Inactivo"
            print(f"TRABAJADOR > {nombre} | {dni} | {edad} | {profesion} | {estado}")
            print("")       
            print(f" > ¿DESEA ELIMINAR AL TRABAJADOR {nombre}?")
            print(" > [1] CONFIRMAR")
            print(" > [2] RECAHAZAR")
            while True:
                option = input(" > INGRESAR OPCION: ")
                print("")
                if option == "1":
                    listaTrabajadores.pop(indice)
                    print(f" > ¡ EL USUARIO [{nombre}] HA SIDO ELIMINADO CON EXITO !")
                    actualizarTrabajador(listaTrabajadores)
                    break
                elif option == "2":
                    print(" > ¡ NO SE HAN ELIMINADO USUARIOS !")
                    break
                else:
                    print("OPCION INVALIDA")
            break
        indice = indice + 1

 
        