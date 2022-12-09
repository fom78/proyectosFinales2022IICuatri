def edadValida(edad):
    if (edad > 17) & (edad < 101):
        return True
    else:
        return False

def dniValido(dni):
    dni = str(dni)
    if (len(dni) > 6) and (len(dni) < 9):
        return True
    else:
        return False

def dniExiste(dni,lista):
    for i in lista:
        if i["dni"] == dni:
            return True
    return False