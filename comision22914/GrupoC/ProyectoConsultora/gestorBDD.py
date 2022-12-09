import sqlite3

conexion = sqlite3.connect("ProyectoTrabajadores.db")

cursor = conexion.cursor()

def normalizarTexto(texto):
    texto = str(texto).lower()
    texto = texto.capitalize()
    return texto

def almacenarTrabajadorDB(dni, nombre, edad, profesion, estado):
    nombre = normalizarTexto(nombre)
    profesion = normalizarTexto(profesion)
    query = f"INSERT INTO trabajadores VALUES ({dni},'{nombre}',{edad},'{profesion}','{estado}')"
    cursor.execute(query)
    conexion.commit()

def updateTrabajador(dni, nombre, edad, profesion):
    nombre = normalizarTexto(nombre)
    profesion = normalizarTexto(profesion)
    query = f"UPDATE trabajadores SET nombre = '{nombre}', edad = {edad}, profesion = '{profesion}' WHERE dni = {dni}"
    cursor.execute(query)
    conexion.commit()

def updateStatus(dni, estado):
    query = f"UPDATE trabajadores SET estado = '{estado}' WHERE dni = {dni}"
    cursor.execute(query)
    conexion.commit()

def deleteTrabajador(dni):
    query = f"DELETE FROM trabajadores WHERE dni = {dni}"
    cursor.execute(query)
    conexion.commit()

def getActivos():
    query = f"SELECT dni, nombre, edad, profesion FROM trabajadores WHERE estado = 'True'"
    cursor.execute(query)
    listaActivos = cursor.fetchall()
    return listaActivos

def getInactivos():
    query = f"SELECT dni, nombre, edad, profesion FROM trabajadores WHERE estado = 'False'"
    cursor.execute(query)
    listaInactivos = cursor.fetchall()
    return listaInactivos

def getTrabajadoresPorEdad(edadMinima, edadMaxima):
    query = f"SELECT dni, nombre, edad, profesion FROM trabajadores WHERE estado = 'False' AND edad >= {edadMinima} AND edad <= {edadMaxima}"
    cursor.execute(query)
    listaPorEdad = cursor.fetchall()
    return listaPorEdad

def getTrabajadoresPorProfesion(profesion):
    profesion = normalizarTexto(profesion)
    query = f"SELECT dni, nombre, edad, estado FROM trabajadores WHERE profesion = '{profesion}'"
    cursor.execute(query)
    listaPorProfesion = cursor.fetchall()
    return listaPorProfesion