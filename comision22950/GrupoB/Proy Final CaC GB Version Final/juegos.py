'''
En una casa de juego se puede optar entre juegos de dados y el piedra papel o tijeras (pipati)

Es sistema deberia tener un menu dinamico:

[1] Piedra Papel o tijeras
[2] Dados
[3] Estadisticas
[0] Salir

Piedra Papel o tijeras

Se puede jugar en 3 modos:
[1] Ruedas libres (Se juegan ruedass hasta que se decida no jugar mas, el resultado final de la partida sera la suma de quien gano cada rueda, Ejemplo se jugaron 22 ruedas vos ganaste 12, la Pc 6 y 4 empates el resultado fial fue: Vos 12 Pc 6)
[2] El que gana 5 ruedas, se termina cuando uno de los dos llegue a 5 victorias, un ejemplo de resulatado fianl seria:
Vos 3 Pc 5
[3] Ruedas fijas, por ejemplo se juegan 6 ruedas y si vos ganaste 1 pc 1 y hubo 4 empates el resultado final de la partida sera Vos 1 Pc 1


- El resultado de la partida (Vos x Pc x) Se guardara en un archivo para mantener el historico.

Dados

Se tiran 5 dados por ronda.

Puntuacion

- Los 5 dados iguales suma 20 puntos
- 4 dados iguales suma 12 puntos
- 3 dados iguales y un par suma 9 puntos
- 3 dados iguales suma 6 puntos
- 2 pares de dados iguales suma 5 puntos
- 1 par de dados iguales suma 2 puntos

Se jugaran 3 rondas.


Al finalizar las 3 rondas se suman los puntajes y ese es el resultado final de la partida, ese resultado se debera guardar en otro archivo.


Estadisticas

Usar la creatividad y mostrar diversas estadisticas de los archivos, por ejemplo numero de victorias en los dados, en el pipati, partidas jugadas en total, etc...
'''