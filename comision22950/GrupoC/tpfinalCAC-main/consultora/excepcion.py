def correccionErrores(mensaje="Ingrese una opción: ", msjError="Ingrese un numero entero"):
    while True:
        try:
            entero = int(input(mensaje))
            break
        except ValueError:
            print(msjError)
    return entero
