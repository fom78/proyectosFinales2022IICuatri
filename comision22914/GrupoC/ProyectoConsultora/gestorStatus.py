from persistenciaTrabajadores import actualizarTrabajador
from validaciones import dniValido, dniExiste

def cambiarStatusTrabajador(listaTrabajadores):
    huboCambio = False
    while True:
        try:
            dni = int(input(" >>> INGRESE DNI DEL USUARIO: "))
            if dniValido(dni):
                if dniExiste(dni, listaTrabajadores):
                    break
                else:
                    print(f" >>> EL DNI {dni} NO SE ENCUENTRA")
            else:
                print(f" >>> EL DNI {dni} NO ES VALIDO")        
        except:
            print(" >>> DATO NO VALIDO")
    print("")
    for i in listaTrabajadores:
        if i["dni"] == dni:
            nombre = i["nombre"]
            estado = i["estado"]
            if estado == True:
                oldEstado = "ACTIVO"
                newEstado = "INACTIVO"
                estado = False
            else:
                oldEstado = "INACTIVO"
                newEstado = "ACTIVO"
                estado = True
            print(f" >>> EL ESTADO DEL USUARIO {nombre} es {oldEstado}")
            print(f" >>> CAMBIAR ESTADO [{oldEstado} --> {newEstado}]")
            print("     [1] CONFIRMAR")
            print("     [2] RECHAZAR")
            while True:
                optionCambio = input("     OPCION: ")
                if optionCambio == "1":
                    print("")
                    print(f" >>> EL ESTADO HA SIDO MODIFICADO CORRECTAMENTE - ESTADO ACTUAL [{newEstado}]")
                    i["estado"] = estado
                    actualizarTrabajador(listaTrabajadores)
                    huboCambio = True
                    break
                elif optionCambio == "2":
                    print("")
                    print(f" >>> EL ESTADO NO HA SIDO MODIFICADO - ESTADO ACTUAL [{oldEstado}]")
                    break
                else:
                    print(" >>> OPCION INVALIDA - [1] PARA CONFIRMAR - [2] PARA RECHAZAR")
            break

    print("")
    