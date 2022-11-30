import datetime

def leerArchivoDados(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"x")
    archivo.close()
    archivo = open(nombreArchivo,"r")

  datos=[]
  v = archivoVacio(nombreArchivo)
  if v==False:
    for linea in archivo.readlines():
      dato=linea.replace('\n','')
      dato=dato.split(",")
      dato = {"id":int(dato[0]),"TimeStamp":dato[1],"puntaje":int(dato[2])}
      datos.append(dato)
    archivo.close()
  else:
    datos = [{"id":int(0),"TimeStamp":"0000","puntaje":int(0)}]


  return datos


def grabarArchivoDados(archivo,datos):
    respuesta = leerArchivoDados(archivo)
    ultimoId= (respuesta[-1]['id'])
    id= ultimoId + 1
    ts= datetime.datetime.now()
    if id ==1 :
      linea =f"{str(id)},{str(ts)},{datos}"    
    else:
      linea =f"\n{str(id)},{str(ts)},{datos}"
    archivo = open("RegDados.txt","a")
    archivo.write(linea)
    archivo.close
    #print(linea)



def leerArchivoPPT(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"x")
    archivo.close()
    archivo = open(nombreArchivo,"r")

  datos=[]
  v = archivoVacio(nombreArchivo)
  if v==False:
    for linea in archivo.readlines():
      dato=linea.replace('\n','')
      dato=dato.split(",")
      dato = {"id":int(dato[0]),"TimeStamp":dato[1],"puntU":int(dato[2]),"puntPc":int(dato[3]),"empate":int(dato[2])}
      datos.append(dato)
    archivo.close()
  else:
    datos =[{"id":int(0),"TimeStamp":0000,"puntU":int(0),"puntPc":int(0),"empate":int(0)}]

  return datos



def grabarArchivoPPT(archivo,datos):
    respuesta = leerArchivoDados(archivo)
    ultimoId= (respuesta[-1]['id'])
    id= ultimoId + 1
    ts= datetime.datetime.now()
    if id==1:
      linea =f"{str(id)},{str(ts)},{datos[0]},{datos[1]},{datos[2]}"
    else:
      linea =f"\n{str(id)},{str(ts)},{datos[0]},{datos[1]},{datos[2]}"
    archivo = open("RegPiPaTi.txt","a")
    archivo.write(linea)
    archivo.close  

def archivoVacio(nombreArchivo):
    rta = True
    with open(nombreArchivo,'r') as objaLeer:
        primerCar = objaLeer.read(1)
    if not primerCar:   
       rta = True
    else:
       rta =False

    return rta
   


#res = leerArchivoDados("v.txt")  
#print(res)