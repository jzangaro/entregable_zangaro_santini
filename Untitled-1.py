
class MenuNoValido (Exception):
    def __init__ (self, opcion, mensaje = "Opcion de menu no valida"):
        self.opcion = opcion
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EntradaInvalida (Exception):
    def __init__(self, mensaje = 'Entrada inválida, porfavor intentelo denuevo.'):
        self.mensaje = mensaje 
        super().__init__(self.mensaje)


# Clase Base 
class Empleado:
    def __init__(self, id_empleado, nombre, fecha_nacimiento, nacionalidad, salario):
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario




    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, value):
        if len(value) != 8:
            raise ValueError("El ID del empleado debe tener exactamente 8 dígitos.")

        for i in value:
            if i < '0' or i > '9':
                raise ValueError("El ID del empleado debe contener solo números del 0 al 9.")
        
        self._id_empleado = value




    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value:  
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value




    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):

        # Se espera que el formato de la fecha sea DD/MM/AAAA.

        partes = value.split('/')
        if len(partes) == 3:
            dia, mes, año = partes
            if not (len(dia) == 2 and all(char in '0123456789' for char in dia) and 
                    len(mes) == 2 and all(char in '0123456789' for char in mes) and
                    len(año) == 4 and all(char in '0123456789' for char in año)):
                raise ValueError("Fecha de nacimiento debe estar en formato DD/MM/AAAA y ser válida.")
            self._fecha_nacimiento = value
        else:
            raise ValueError("Fecha de nacimiento debe estar en formato DD/MM/AAAA.")
        



    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, value):
        if not value:
            raise ValueError("La nacionalidad no puede estar vacía.")
        self._nacionalidad = value



    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        if type(value) not in [int, float] or value <= 0:
            raise ValueError("El salario debe ser un número positivo.")
        self._salario = value

# Pilotos
class Piloto(Empleado):
    def __init__(self, id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto):
        super().__init__(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = score
        self._numero_auto = numero_auto
        self._puntaje_campeonato = 0
        self._lesionado = False






    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if 1 <= value <= 99:
            self._score = value
        else:
            raise ValueError("El score debe ser un número entero entre 1 y 99.")






    @property
    def numero_auto(self):
        return self._numero_auto

    @numero_auto.setter
    def numero_auto(self, value):
        value_str = str(value)
        for char in value_str:
            if char not in '0123456789':
                raise ValueError("El número de auto debe ser un número entero positivo.")

        # Si todos los caracteres son dígitos, convertir a entero y verificar si es positivo

        numero = int(value_str)
        if numero <= 0:
            raise ValueError("El número de auto debe ser un número entero positivo.")

        self._numero_auto = numero

# Directores de equipo
class DirectorEquipo:
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario

# Mecanicos 
class Mecanico(Empleado):
    def __init__(self, id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        score_int = int(value)
        if score_int < 1 or score_int > 99:
            raise ValueError("El score debe ser un número entero entre 1 y 99.")
        self._score = score_int

# Jefes
class JefeEquipo(Empleado):
    def __init__ (self, id_empleado, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, "Jefe de Equipo")

# Autos
class Auto:
    def __init__(self, modelo, anio, score):
        self._modelo = modelo
        self._anio = anio
        self._score = score

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        if not value or type(value) is not str:
            raise ValueError("El modelo debe ser una cadena no vacía.")
        self._modelo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        try:
            anio_int = int(value)
            if anio_int < 1885 or anio_int > 2023:  # Rango de años válido
                raise ValueError("El año debe ser un entero que represente un año válido de fabricación de autos.")
            self._anio = anio_int
        except ValueError:
            raise ValueError("El año debe ser un número entero válido.")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        try:
            score_int = int(value)
            if score_int < 1 or score_int > 99:  # Rango de score válido
                raise ValueError("El score debe ser un número entero entre 1 y 99.")
            self._score = score_int
        except ValueError:
            raise ValueError("El score debe ser un número entero válido.")
        
# Equipos
class Equipo:
    def __init__(self, nombre):
        self._nombre = nombre
        self._empleados = []
        self._auto = None

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def asignar_auto(self, auto):
        self.auto = auto

    def obtener_informacion(self):
        info = "Equipo: " + self.nombre + "\n"
        info += "Empleados:\n"
        for empleado in self.empleados:
            info += " - " + empleado.nombre + "\n"
        info += "Auto: "
        if self.auto:
            info += self.auto.modelo
        else:
            info += "No asignado"
        info += "\n"
        return info



los_equipos = []
los_autos = []


# Menu
def menu_principal ():

    while True:
        print("MENU PRINCIPAL")
        print("1: Alta de Empleado ")
        print("2: Alta de Auto ")
        print("3: Alta de Equipo ")
        print("4: Simular carrera")
        print("5: Realizar consultas ")
        print("6: Finalizar programa ")

        
        opcion = int(input("Ingrese una opción: "))

        if opcion < 1 or opcion > 6:
            raise EntradaInvalida()

        if opcion == 1:
            alta_empleado()
        elif opcion == 2:
            alta_auto()
        elif opcion == 3:
            alta_equipo()
        elif opcion == 4:
            simuladorCarrera()
            pass
        elif opcion == 5:
            realizar_consultas()
        elif opcion == 6:
            print(" Finalizando programa...")
            break
        else: 
            raise MenuNoValido (opcion)
        
       

# Consultas
def realizar_consultas ():
    pass



# Altas
def alta_empleado():
        
        while True:
            try:
                id_empleado = input ("Ingrese su cedula: ")
                if len(id_empleado) != 8:
                    raise EntradaInvalida
                break
            except EntradaInvalida:
                print("La cedula no tiene la cantidad de digitos necesaria")
            

        nombre = input ("Ingrese su nombre: ")

        while True:
            try:
                fecha_nacimiento = input("Ingrese su fecha de Nacimiento: ")
                partes = fecha_nacimiento.split('/')
                if len(partes) != 3:
                    raise EntradaInvalida
                    
                dia, mes, año = partes
                if not (len(dia) == 2 and all (char in '0123456789' for char in dia) and 
                         len(mes) == 2 and all (char in '0123456789' for char in mes) and 
                         len(año) == 2 and all (char in '0123456789' for char in año)):
                        raise EntradaInvalida
                break
            except EntradaInvalida as e:
                print (e)

        nacionalidad = input ("Ingrese su nacionalidad: ")

        salario = float(input("Ingrese su salario: "))


        print("")
        print("Cargos: ")
        print(" 1: Piloto ")
        print(" 2: Piloto de Reserva ")
        print(" 3: Mecanico ")
        print(" 4: Jefe de equipo ")
        print("")

        cargo = int(input("Ingrese su cargo "))

        if cargo in [1,2]: 
            # Piloto principal y de reserva 
            score = int(input("Ingrese score: "))
            numero_auto = int(input("Ingrese número de auto: "))
            return Piloto (id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto)
        elif cargo == 3: 
            # Mecánico 
            score = int(input("Ingrese score: "))
            return Mecanico ((id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score))
        elif cargo == 4: 
            # Jefe de Equipo
            return JefeEquipo ((id_empleado, nombre, fecha_nacimiento, nacionalidad, salario))
        else:
            print ("Cargo no disponible.")
            return None 

def alta_auto ():
        modelo = input("Ingrese modelo del auto: ")
        anio = int(input("Ingrese año del auto: "))
        score = int(input(" Ingrese el score del auto: "))

        auto = Auto (modelo, anio, score)
        los_autos.append(auto)

        return auto

def alta_equipo ():
        nombre_equipo = input ("Ingrese nombre del equipo: ")
        equipo = Equipo(nombre_equipo)

        print("Datos del auto del equipo: ")
        auto = alta_auto()
        equipo.asignar_auto(auto)

        for i in range (12):
            empleado = alta_empleado()
            if empleado:
                equipo.agregar_empleado(empleado)

        los_equipos.append(equipo)
        
        return equipo







# Simulador de carrera
def simuladorCarrera():
    pass


# Main
menu_principal()







    






        









