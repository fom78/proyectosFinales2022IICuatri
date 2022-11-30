from controlerrores import controlErrornumerico, controlCadenas
from colorama import Style, Fore, init
init()

def transformarArchivos (miarchivo):
    archivo= open(miarchivo, "r")
    lista=[]
    for line in archivo.readlines():
        l=line.replace('\n','')
        l=l.split(",")
        
        dicc= {"NomyApe":l[0], 
               "Edad":int(l[1]),
               "Dni":int(l[2]),
               "Localidad":l[3],
               "Profesion":l[4],
               "Activo":l[5]}
        lista.append(dicc)
    archivo.close()   
    return lista  

def agregarEmpleado(listado): 
   
   nomApellido=controlCadenas(leyenda=Fore.CYAN+"NOMBRE Y APELLIDO: ")
   edad=controlErrornumerico(leyenda=Fore.CYAN+"EDAD: ", msjError="EN ESTE CAMPO SOLO PUEDE INGRESAR NÚMEROS")
   dni= int(input(Fore.CYAN+"DNI: "))
   localidad=controlCadenas(leyenda=Fore.CYAN+"LOCALIDAD: ")
   prof=controlCadenas(leyenda=Fore.CYAN+"PROFESIÓN: ")
  
   while True: 
            activo= input(Fore.CYAN+"ACTIVO ¿S/N?: ")
            if activo.upper()=="S":
               activo=True
               break
            elif activo.upper()=="N":
                 activo=False
                 break
            else:
                print(Fore.RED+ Style.BRIGHT+"INTRODUZCA [S] O [N] PARA CONTINUAR"+ Fore.RESET+Style.NORMAL)
                continue     
    
  
   dicc= {"Nombre y Apellido":nomApellido.title(), 
          "Edad":edad,
          "Dni":dni,
          "Localidad":localidad.title(),
          "Profesion":prof.title(),
          "Activo":activo}
    
   listado.append(dicc)

   archivo = open("BDempleados.txt","a")
   linea = f"\n{nomApellido.title()},{edad},{dni},{localidad.title()},{prof.title()},{activo}"

   archivo.write(linea)
   archivo.close()
   





