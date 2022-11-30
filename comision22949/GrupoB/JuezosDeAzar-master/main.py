from borra import cleaning
from decoracion import decorar, decorar1
from errores import validarIngresoEntero
from GpoBJuegoDeDados import juegosDados
from GpoBPiedraPapelTijeras import JuegoPPYJ
from abm import leerArchivoDados,grabarArchivoDados,leerArchivoPPT,grabarArchivoPPT

cleaning()
print("#"*45)
print("Mi Cajita de Juegos".center(45,"="))

acuResul = [0,0,0]

while True:
    
    print(
        f'''
        \t Menu
        [1] Piedra Papel o tijeras
        [2] Dados
        [3] Estadisticas
        [0] Salir
        '''
        )
       
    opcion = validarIngresoEntero("Seleccione una opcion: ")
    cleaning()
    if opcion == 1:
        while True:
            
            print(
                f'''
                \t Menu
                [1] Ruedas Libres
                [2] 5 Ruedas
                [3] Ruedas Fijas
                [0] Salir
                '''
                )
            decorar()
            opcion1 = validarIngresoEntero("Seleccione una opcion: ")
            if opcion1 == 1:
                acuResul = [0,0,0]
                while True:
                    print("Ruedas Libres")
                    r = JuegoPPYJ()
                    print(r)
                    if r == 'Us':
                        acuResul[0] = acuResul[0] + 1
                    elif r == 'Pc':
                        acuResul[1] = acuResul[1] + 1
                    elif r== 'E' :
                        acuResul[2] = acuResul[2] + 1    
                    decorar1()
                    salir=input("\tDesea seguir Jugando?(s/n): ")
                    if salir == "s":
                        continue
                    elif salir =="n":
                        print (acuResul)
                        grabarArchivoPPT("RegPiPaTi.txt",acuResul)
                        break
                    else:
                        print(f"{salir} no es una opción valida, vas a  seguir jugando hasta que tipees la letra n")
                        
            elif opcion1 == 2:
                acuResul = [0,0,0]
                #victorias = 0
                while acuResul[0] <5 and acuResul[1] <5 :
                   # print("5 Ruedas Ganadas")
                    r = JuegoPPYJ()
                    if r == 'Us':
                        acuResul[0] = acuResul[0] + 1
                    elif r == 'Pc':
                        acuResul[1] = acuResul[1] + 1
                    elif r== 'E' :
                        acuResul[2] = acuResul[2] + 1 
                    decorar1()
                    print (acuResul)
                    #victorias = victorias + 1
                print ("terminó la partida,", acuResul)      

                if acuResul[0] == 5:
                     ganador = "Usuario"
                elif acuResul[1] == 5:
                     ganador = "Computadora"
                print ("El ganador es:", ganador) 
                grabarArchivoPPT("RegPiPaTi.txt",acuResul)
                acuResul = [0,0,0]         

            elif opcion1 == 3:
                acuResul = [0,0,0]
                print("Ruedas Fijas")
                cantRuedas= validarIngresoEntero("Ingrese Cantidad de ruedas a jugar: ")
                decorar1()
                i=0
                for i in range(cantRuedas):
                    r = JuegoPPYJ()
                    if r == 'Us':
                        acuResul[0] = acuResul[0] + 1
                    elif r == 'Pc':
                        acuResul[1] = acuResul[1] + 1
                    elif r== 'E' :
                        acuResul[2] = acuResul[2] + 1 
                    decorar1()
                    print (acuResul)
                    decorar1()
                grabarArchivoPPT("RegPiPaTi.txt",acuResul)
            elif opcion1 == 0:
                print("Vuelve pronto a jugar!!")
                decorar1() 
                break       
            else:
                decorar()
                print("Por favor, Elija una opción dentro del menu:")
                decorar()

    elif opcion == 2:
        cleaning()
        print("¡¡Elegiste Dados!!")
        puntaje = juegosDados()  
        print(puntaje) 
        grabarArchivoDados("RegDados.txt",puntaje)     
    elif opcion == 3:
        print("A continuación te mostramos las Estadisticas!!")
        salida = False
        while salida == False:
            opcion2 = validarIngresoEntero("Desea ver las estadisticas de los dados[1], Pipati[2] => ")
            if opcion2 == 1:
                salida = True
                cleaning()
                print("¡¡Registro de Juegos de Dados!!")
                resp = leerArchivoDados("RegDados.txt")
                decorar()
                for x in resp :
                    fecha = x["TimeStamp"]
                    punt =  x["puntaje"]
                    pantalla = linea =f"Dia y hora de Jugada: {str(fecha)}   puntaje: {str(punt)}"
                    print(pantalla)
                decorar()
            elif opcion2 == 2:
                salida = True
                print("¡¡Registro de Juegos Piedra, papel y Tijera!!")
                resp = leerArchivoPPT("RegPiPaTi.txt")
                decorar()
                for x in resp :
                    fecha = x["TimeStamp"]
                    puntU =  x["puntU"]
                    puntPc = x["puntPc"]
                    empate = x["empate"]
                    pantalla = linea =f"Dia y hora de Jugada: {str(fecha)}   Usuario: {str(puntU)}  Pc: {str(puntPc)}   Empate: {str(empate)}"
                    print(pantalla)
                #datos = {"id":int(0),"TimeStamp":0000,"Usuario":int(0),"Pc":int(0),"Empate":int(0)}
                decorar()
            else:
                print("Ingrese opcion 1 o 2")
    elif opcion == 0:
        print("¡ Gracias por jugar con nosotros, te esperamos pronto !") 
        decorar()
        break
    else:
        decorar()
        print("Por favor, Elija una opción dentro del menu:")
        decorar()