def leerArchivoDados(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"x")
    archivo.close()
    archivo = open(nombreArchivo,"r")

  datos=[]
  for linea in archivo.readlines():
    dato=linea.replace('\n','')
    dato=dato.split(",")
    dato = {"id":int(dato[0]),"TimeStamp":dato[1],"puntaje":int(dato[2])}
    datos.append(dato)
  archivo.close()
  return datos



#r = leerArchivoDados("RegDados.txt")
#for linea in r :
#  print(linea)

def leerArchivoPPT(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"x")
    archivo.close()
    archivo = open(nombreArchivo,"r")

  datos=[]
  for linea in archivo.readlines():
    dato=linea.replace('\n','')
    dato=dato.split(",")
    dato = {"id":int(dato[0]),"TimeStamp":dato[1],"puntU":int(dato[2]),"puntPc":int(dato[3]),"empate":int(dato[4])}
    datos.append(dato)
  archivo.close()
  return datos



#r = leerArchivoPPT("RegPiPaTi.txt")
#for linea in r :
#  print(linea)


'''r = leerArchivoDados("RegDados.txt")
print(r)
print(r[-1]['id'])
'''  
