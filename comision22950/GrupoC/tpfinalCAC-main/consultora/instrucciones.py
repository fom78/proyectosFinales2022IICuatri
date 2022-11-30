'''
Realizar un sistema que permita ejecutar distintas funciones a un empleado de una consultora de trabajo.

- La consultora guarda los datos de los trabajodores en un archivo llamado trabajadores.dat, la estructura de este archivo es la siguiente

Nombre,edad,dni,profesion,activo (Opcionalmente pueden agregar algunos datos mas.)
- En activo se define si esta o no trabajando dicho trabajador.
- Un ejemplo seria:
Enzo,12,3223233232,Gamer,True

El Menu principal del sistema debe mostrar las siguientes opciones:

[1] Gestion de Trabajadores
[2] Reportes
[3] Cambiar status trabajador
[0] Salir

Gestion de Trabajadores
Debera mostrar otro menu con estas opciones:
[1] Ingresar nuevo Trabajador
[2] Modificar dato de trabajador (file.writelines())
[3] Eliminar Trabajador

Reportes
[1] Mostrar trabajadores Activos
[2] Mostrar trabajadores desocupados
[3] Mostrar desocupados en un rango de edad
[4] Mostrar trabajadores segun la profesion

Cambiar status trabajador
En esta opcion se debe buscar el trabajador por dni y cambiarle el status activo, es cuando se da de alta/baja en un trabajo
'''