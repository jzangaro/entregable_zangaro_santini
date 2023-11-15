

class MenuNoValido (Exception):
    def __init__ (self, opcion, mensaje = "Opcion de menu no valida"):
        self.opcion = opcion
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EntradaInvalida (Exception):
    def __init__(self, mensaje = 'Entrada inválida, porfavor intentelo denuevo.'):
        self.mensaje = mensaje 
        super().__init__(self.mensaje)

class Empleado:
    def __init__(self, id, nombre, fecha_nac, nacionalidad, salario):
        self._id = id
        self._nombre = nombre
        self._fecha_nac = fecha_nac
        self._nacionalidad = nacionalidad
        self._salario = salario

class Piloto (Empleado):
    def __init__(self, id, nombre, fecha_nac, nacionalidad, salario, score, numero_auto, puntaje_campeonato, esta_lesionado):
        super().__init__(self, id, nombre, fecha_nac, nacionalidad, salario, 'piloto')
        self._score = score
        self._numero_auto = numero_auto
        self._puntaje_campeonato = puntaje_campeonato
        self._esta_lesionado = esta_lesionado

class Mecanico (Empleado):
    def __init__(self, id, nombre, fecha_nac, nacionalidad, salario, score):
        super().__init__(self, id, nombre, fecha_nac, nacionalidad, salario, 'mecanico')
        self._score = score

class Director(Empleado):
    def __init__(self, id, nombre, fecha_nac, nacionalidad, salario):
        super().__init__(self, id, nombre, fecha_nac, nacionalidad, salario, 'director')

class Auto:
    def __init__(self, modelo, anio, score):
        self._modelo = modelo
        self._anio = anio
        self._score = score
        
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self._empleados = []
        self._pilotos = []
        self._director = None
        self._modelo_auto = None 

    def agregar_piloto(self, piloto):
        self.pilotos.append(piloto)

    def agregar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)

    def asignar_director(self, director):
        self.director = director

    def asignar_auto(self, auto):
        self.auto = auto



def alta_empleado():
    cedula = input("Ingrese cedula: ")
    nombre = input("Ingrese nombre: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
    nacionalidad = input("Ingrese nacionalidad: ")
    salario = float(input("Ingrese salario: "))
    cargo = int(input("Ingrese cargo (1: Piloto, 2: Piloto de reserva, 3: Mecánico, 4: Jefe de equipo): "))

    if cargo in [1, 2]:  # Piloto o Piloto de reserva
        score = int(input("Ingrese score: "))
        numero_auto = int(input("Ingrese número de auto: "))
        return Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, 0, False)
    elif cargo == 3:  # Mecánico
        score = int(input("Ingrese score: "))
        return Mecanico(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score)
    elif cargo == 4:  # Jefe de equipo
        return Director(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
    else:
        print("Cargo no válido.")
        return None

def alta_auto():
    modelo = input("Ingrese modelo: ")
    anio = int(input("Ingrese año: "))
    score = int(input("Ingrese score: "))
    return Auto(modelo, anio, score)

def alta_equipo(empleados, autos):
    nombre_equipo = input("Ingrese nombre del equipo: ")
    modelo_auto = input("Ingrese modelo de auto: ")

    equipo = Equipo(nombre_equipo)
    if modelo_auto in autos:
        equipo.asignar_auto(autos[modelo_auto])
    else:
        print("Modelo de auto no encontrado.")
        return None

    for _ in range(12):
        cedula_empleado = input("Ingrese cedula del empleado: ")
        if cedula_empleado in empleados:
            empleado = empleados[cedula_empleado]
            if empleado.tipo == "piloto":
                equipo.agregar_piloto(empleado)
            elif empleado.tipo == "mecanico":
                equipo.agregar_mecanico(empleado)
            elif empleado.tipo == "director":
                equipo.asignar_director(empleado)
        else:
            print("Empleado no encontrado.")

    return equipo

def consultas(equipos):
    while True:
        print("\nConsultas Disponibles:")
        print("1. Top 10 pilotos con más puntos en el campeonato")
        print("2. Resumen campeonato de constructores (equipos)")
        print("3. Top 5 pilotos mejores pagos")
        print("4. Top 3 pilotos más hábiles")
        print("5. Retornar jefes de equipo")
        print("6. Volver al menú principal")

        opcion = int(input("Seleccione una consulta: "))

        if opcion == 1:
         top_pilotos_puntos(equipos)
        elif opcion == 2:
         resumen_constructores(equipos)
        elif opcion == 3:
         top_pilotos_salario(equipos)
        elif opcion == 4:
         top_pilotos_habilidosos(equipos)
        elif opcion == 5:
         jefes_equipo(equipos)
        else:
         raise EntradaInvalida

def simular_Carrera():
    pass


def top_pilotos_puntos(equipos):
    pass

def resumen_constructores (equipos):
    pass

def top_pilotos_salario(equipos):
    pass

def top_pilotos_habilidosos(equipos):
    pass

def jefes_equipo(equipos):
    pass



def main():
    empleados = {}
    autos = {}
    equipos = []

    while True:
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")

        while True:
            opcion_usuario_input = input("Seleccione una opción: ")
            if not opcion_usuario_input.strip():
                # Si el usuario solo presiona Enter, se muestra de nuevo el menú
                continue
            try:
                opcion_usuario = int(opcion_usuario_input)
                if 1 <= opcion_usuario <= 6:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except EntradaInvalida:
                print("Por favor, ingrese un número válido.")

        if opcion_usuario == 1:
            empleado = alta_empleado()
            empleados[empleado.id] = empleado
            print(f"Empleado {empleado.nombre} agregado con éxito.")
        elif opcion_usuario == 2:
            auto = alta_auto()
            autos[auto.modelo] = auto
            print(f"Auto modelo {auto.modelo} agregado con éxito.")
        elif opcion_usuario == 3:
            equipo = alta_equipo(empleados, autos)
            equipos.append(equipo)
            print(f"Equipo {equipo.nombre} creado exitosamente.")
        elif opcion_usuario == 4:
            resultados_carrera = simular_Carrera(equipos)
            print(resultados_carrera)
        elif opcion_usuario == 5:
            consultas(equipos)
            print("Realizar consultas")
        elif opcion_usuario == 6:
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
    

