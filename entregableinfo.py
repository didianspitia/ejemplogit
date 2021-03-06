class sistema():
    def __init__(self):
        self.__dicEstudiantes = {}

    #metodos
    def verdicEstudiantes(self):
        return self.__dicEstudiantes

    def asignardicEstudiantes(self,n):
        self.__dicEstudiantes[n.verCedula()] = n

    def buscarEstudiante(self,n):
        return self.__dicEstudiantes.get(n,False)

    def buscarMateria(self,n,a):
        return self.__dicEstudiantes[n].verdicMateria().get(a,False)

class materia():
    def __init__(self):
        self.__codigo = 0
        self.__nombre = ' '
        self.__horario = ' '
        
    #ver
    def verNombre(self):
        return self.__nombre
    def verCodigo(self):
        return self.__codigo
    def verHorario(self):
        return self.__horario
    

    #asignar
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCodigo(self,n):
        self.__codigo = n
    def asignarHorario(self,n):
        self.__horario = n
    

class carrera(materia):
    def __init__(self):
        self.__version = 0
    
    def verVersion(self):
        return self.__version
    def asignarVersion(self,n):
        self.__version = n

    
class electiva(materia):
    def __init__(self):
        self.__creditos = 0

    def verCreditos(self):
        return self.__creditos
    def asignarCreditos(self,n):
        self.__creditos = n

class estudiante(): 
    def __init__(self):
        self.__nombre = ' '
        self.__cedula = 0
        self.__edad = 0
        self.__dicMateria = {}
    #ver
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verEdad(self):
        return self.__edad
    def verdicMateria(self):
        return self.__dicMateria
    #asignar
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCedula(self,n):
        self.__cedula = n
    def asignarEdad(self,n):
        self.__edad = n 
    def asignardicMateria(self,n):
        self.__dicMateria[n.verCodigo()] = n

class horarios():
    def __init__(self):
        self.__listaProfesores = ['Lince', 'Solanlle', 'Parra', 'Angelower']
        self.__listaHorarios = {'Lince':'Lunes','Solanlle':'Martes','Parra':'Miercoles', 'Angelower' : 'Jueves'}
    def verHorarios(self):
        return self.__listaHorarios 
    def verProfesores(self):
        return self.__listaProfesores

class ssofi():
    def __init__(self):
        self.__listassofi = []
    def verListassofi(self):
        return self.__listassofi
    def asignarSolicitud(self,n):
        self.__listassofi.append(n)


def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Ingrese un dato num??rico")
    return valor

def validarStr(msj):
    while True:
        if msj.isalpha() is False:
            msj = input('ingrese solo letras: ')
            continue
        else:
            break
    return msj     


def main():
    contrase??a = 123
    while True:
        contra = int(input('Ingrese la contrase??a: '))
        if contra == contrase??a:
            break
        else:
            print('contrase??a incorrecta')
            continue 
    
    sis = sistema()
    s = ssofi()
    while True:        
        e = estudiante()
        print("""
        1. Ingresar estudiante que solicita cupos
        2. Ver informacion de un estudiante
        3. Mostrar profesores  
        4. Mostrar horarios disponibles
        5. subir una solicitud al ssofi
        6. Guardar y cargar informacion a archivo txt
        7. salir""")
        menu = validar('menu: ')  
        if menu == 1:
            nombre = validarStr(input('Ingrese el nombre sin espacios: '))
            cedula = validar('Ingrese la cedula: ')
            edad = validar('Ingrese la edad: ')
            numMaterias = validar('ingrese el numero de materias que va a solicitar cupo: ')
            
            e.asignarNombre(nombre)
            e.asignarCedula(cedula)
            e.asignarEdad(edad)

            

            for i in range(0,numMaterias):
                nombreMateria = validarStr(input('Ingrese el nombre de la materia sin espacios: '))
                codigo = validar('Ingrese el codigo de la materia: ')
                horario = input('Ingrese el horario: ')
                tipo = validar('''ingrese que tipo de ajuste forzoso va a realizar: 
                1. materias de carrera
                2. materias de tronco comun
                3. materias electivas
                ''')
            
                if tipo == 1:
                    c = carrera()
                    version = validar('ingrese la version del pensum: ')
                    c.asignarVersion(version)
                    c.asignarNombre(nombreMateria)
                    c.asignarCodigo(codigo)
                    c.asignarHorario(horario)
                    e.asignardicMateria(c)
                
                elif tipo == 2:
                    m = materia()
                    m.asignarNombre(nombreMateria)
                    m.asignarCodigo(codigo)
                    m.asignarHorario(horario)
                    e.asignardicMateria(m)

                elif tipo == 3:
                    el = electiva()
                    cr = validar('ingrese los creditos minimos: ')
                    el.asignarCreditos(cr)
                    el.asignarNombre(nombreMateria)
                    el.asignarCodigo(codigo)
                    el.asignarHorario(horario)
                    e.asignardicMateria(el)

            sis.asignardicEstudiantes(e)
            print(e.verNombre())

            
            

        elif menu == 2:
            id = validar('Ingrese la cedula del estudiante que desea buscar: ')
            if sis.buscarEstudiante(id):
                estudiantes = sis.buscarEstudiante(id)
                print(f'''
                Nombre = {estudiantes.verNombre()}
                Cedula = {estudiantes.verCedula()}
                ''')
                codigos = validar('Ingrese el codigo de la materia a buscar: ')
                
                if sis.buscarMateria(id,codigos):
                    materias = sis.buscarMateria(id,codigos)
                    print(f'''
                    nombre = {materias.verNombre()}
                    codigo = {materias.verCodigo()}
                    horario = {materias.verHorario()}
                    ''')
                    try:
                        print(f'''
                        creditos = {materias.verCreditos()}''')
                        
                    except: AttributeError
                    try:
                        print(f'''
                        version = {materias.verVersion()}
                        ''')
                       
                    except: AttributeError
                        
                else:
                    print("la materia no se encuentra")
            else:
                print("el estudiante no est?? en la base de datos")
                
        elif menu == 3:
            h = horarios()
            l = ['Lince', 'Solanlle', 'Parra', 'Angelower']
            #h.asignarProfesores(l)
            print(f'profesores disponibles: {h.verProfesores()}')
        elif menu == 4:
            h = horarios()
            print(f'horarios disponibles: {h.verHorarios()}')
        elif menu == 5:
            n = validarStr(input('ingrese una solicitud al ssofi sin espacios: '))
            s.asignarSolicitud(n)
            print(f'solicitudes actuales: {s.verListassofi()}')
        elif menu == 6:
            # Cargar y guardar inforamacion a archivo txt
            id1 = validar("Ingrese Cedula del estudiante a subir: ")
            if sis.buscarEstudiante(id1):
                estudiantes1 = sis.buscarEstudiante(id1)
                codigos1 = validar('Ingrese el codigo de la materia a subir: ')
                if sis.buscarMateria(id1,codigos1):
                    materias1 = sis.buscarMateria(id1,codigos1)
    
                    archivo = open(f"Estudiante {estudiantes1.verNombre()}.txt",'a')
                    archivo.write('nombre: ' + estudiantes1.verNombre()+ "\n" )
                    archivo.write('cedula: ' + str(estudiantes1.verCedula())+ "\n" )
                    archivo.write('edad: '+str( estudiantes1.verEdad())+ "\n" )
                    archivo.write('Nombre de la materia: '+ materias1.verNombre()+ "\n" )
                    archivo.write('Codigo: '+ str (materias1.verCodigo())+ "\n" )
                    archivo.write('Horario: '+ materias1.verHorario()+ "\n" )
                    archivo.close()
                    print("Guardar y cargar informacion a archivo txt fue exitoso.")
                else:
                    print("no se encuentra la materia")
            else:
                print("no se encuentra")
            
        elif menu == 7:
            break




        
if __name__ == '__main__':
    main()
    