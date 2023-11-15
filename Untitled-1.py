
class MenuNoValido (Exception):
    def __init__ (self, opcion, mensaje = "Opcion de menu no valida"):
        self.opcion = opcion
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EntradaInvalida(Exception):
    def __str__(self):
        return "Entrada inválida, por favor intente nuevamente."

class Empleado:
    def __init__(self, id:int, nombre, fecha_nac, nacionalidad, salario, tipo):
        self._id = id
        self._nombre = nombre
        self._fecha_nac = fecha_nac
        self._nacionalidad = nacionalidad
        self._salario = salario
        self._tipo = tipo

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def salario(self):
        return self._salario

        
class Piloto(Empleado):
    def __init__(self, id, nombre, fecha_nac, nacionalidad, salario, score, numero_auto, puntaje_campeonato=0, esta_lesionado=False, es_titular=True):
        super().__init__(id, nombre, fecha_nac, nacionalidad, salario, 'piloto')
        self.score = score
        self.numero_auto = numero_auto
        self.puntaje_campeonato = puntaje_campeonato
        self.esta_lesionado = esta_lesionado
        self.es_titular = es_titular
        self.equipo = None
        self.abandonó = False
        self.errores_en_pits = 0
        self.penalidades = 0
        self.score_final = 0
        self.puntos_carrera = 0

 
        

class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nac, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_nac, nacionalidad, salario, 'mecanico')
        self.score = score

class Director(Empleado):
    def __init__(self, id, nombre, fecha_nac, nacionalidad, salario):
        super().__init__(id, nombre, fecha_nac, nacionalidad, salario, 'director')

class Auto:
     def __init__(self, modelo, anio, score):
        self._modelo = modelo
        self._anio = anio
        self._score = score

     @property
     def modelo(self):
        return self._modelo

     @property
     def anio(self):
        return self._anio

     @property
     def score(self):
        return self._score
        
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pilotos = []
        self.mecanicos = []
        self.director = None 
        self.auto = None

    def agregar_piloto(self, piloto):
        self.pilotos.append(piloto)
        piloto.equipo = self

    def agregar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)

    def asignar_director(self, director):
        self.director = director 

    def asignar_auto(self, auto):
        self.auto = auto





def alta_empleado():

    while True:
        try:
            cedula = input("Ingrese cedula (8 dígitos): ")
            if len(cedula) != 8 or not cedula.isdigit():
                raise EntradaInvalida()
            break
        except EntradaInvalida:
            print("La cédula debe tener exactamente 8 dígitos.")

    nombre = input("Ingrese nombre: ")

    while True:
        try:
            fecha_nacimiento = input("Ingrese su fecha de Nacimiento (DD/MM/AAAA): ")
            partes = fecha_nacimiento.split('/')
            if len(partes) != 3:
                raise EntradaInvalida()
                
            dia, mes, año = partes
            if not (dia.isdigit() and mes.isdigit() and año.isdigit() and len(dia) == 2 and len(mes) == 2 and len(año) == 4):
                raise EntradaInvalida()
            break  # Salir del bucle si la entrada es válida
        except EntradaInvalida:
            print("Formato de fecha inválido. Asegúrese de usar el formato DD/MM/AAAA.")

    
    while True:
        nacionalidad = input("Ingrese nacionalidad (máximo 30 caracteres): ")
        if 1 <= len(nacionalidad) <= 30:
            break
        else:
            raise EntradaInvalida ()

    salario = float(input("Ingrese salario: "))
    cargo = int(input("Ingrese cargo (1: Piloto, 2: Piloto de reserva, 3: Mecánico, 4: Jefe de equipo): "))

    if cargo in [1, 2]:  # Piloto o Piloto de reserva
        score = int(input("Ingrese score: "))
        numero_auto = int(input("Ingrese número de auto: "))
        es_titular = cargo == 1  # True si es piloto titular, False si es piloto de reserva
        return Piloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, 0, False, es_titular)
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

    # Buscar el auto por su modelo
    auto = autos.get(modelo_auto)  # Asumiendo que 'autos' es un diccionario con modelos como claves
    equipo = Equipo(nombre_equipo)
    equipo.asignar_auto(auto)

    for rol in ["piloto titular", "piloto titular", "piloto de reserva", "jefe de equipo"] + ["mecánico"] * 8:
        while True:
            try:
                cedula = input(f"Ingrese cédula del {rol} (8 dígitos): ")
                if len(cedula) != 8 or not cedula.isdigit():
                    raise EntradaInvalida()
                empleado = empleados.get(cedula)
                if empleado is None:
                    raise EntradaInvalida("Empleado no encontrado.")
                if rol in ["piloto titular", "piloto de reserva"]:
                    equipo.agregar_piloto(empleado)
                elif rol == "jefe de equipo":
                    equipo.asignar_director(empleado)
                else:
                    equipo.agregar_mecanico(empleado)
                break
            except EntradaInvalida as e:
                print(e)

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




def simular_Carrera(equipos):
   
    pilotos_en_carrera = obtener_pilotos_para_carrera(equipos)
    #registrar_imprevistos(pilotos_en_carrera)
    calcular_scores(pilotos_en_carrera)
    ordenar_y_asignar_puntos(pilotos_en_carrera)
    restablecer_estado(pilotos_en_carrera)

    # Imprimir los resultados de la carrera
    for piloto in pilotos_en_carrera:
        print(f"{piloto.nombre}: Puntos en la carrera = {piloto.puntos_carrera}, Score final = {piloto.score_final}")

def obtener_pilotos_para_carrera(equipos):
    pilotos_en_carrera = []
    for equipo in equipos:
        pilotos_titulares = [p for p in equipo.pilotos if p.es_titular]
        piloto_reserva = next((p for p in equipo.pilotos if not p.es_titular), None)

        # Verificar disponibilidad de los pilotos titulares
        pilotos_disponibles = [p for p in pilotos_titulares if not p.esta_lesionado and not p.abandonó]

        if len(pilotos_disponibles) == 2:
            # Ambos titulares disponibles
            pilotos_en_carrera.extend(pilotos_disponibles)
        elif len(pilotos_disponibles) == 1:
            # Un titular disponible, el otro es reemplazado por el piloto de reserva
            pilotos_en_carrera.extend(pilotos_disponibles)
            if piloto_reserva:
                pilotos_en_carrera.append(piloto_reserva)
        elif piloto_reserva:
            # Ningún titular disponible, ambos reemplazados por el piloto de reserva
            pilotos_en_carrera.append(piloto_reserva)

    return pilotos_en_carrera

def registrar_imprevistos(pilotos):
    # ni idea aca
    pass

def calcular_scores(pilotos):
    # Calcula el score final de cada piloto
    for piloto in pilotos:
        if piloto.abandonó:
            piloto.score_final = 0
        else:
            score_mecanicos = sum(mecanico.score for mecanico in piloto.equipo.mecanicos)
            piloto.score_final = score_mecanicos + piloto.equipo.auto.score + piloto.score - 5 * piloto.errores_en_pits - 8 * piloto.penalidades

def ordenar_y_asignar_puntos(pilotos):
    # Ordena los pilotos según su score final y asigna puntos
    pilotos_ordenados = sorted(pilotos, key=lambda p: p.score_final, reverse=True)
    puntos_por_posicion = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    for i, piloto in enumerate(pilotos_ordenados):
        piloto.puntos_carrera = puntos_por_posicion[i] if i < len(puntos_por_posicion) else 0

def restablecer_estado(pilotos):
    # Restablece el estado de los pilotos después de la carrera
    for piloto in pilotos:
        piloto.esta_lesionado = False
        piloto.abandonó = False
        piloto.errores_en_pits = 0
        piloto.penalidades = 0




def top_pilotos_puntos(equipos):
    pilotos = []
    for equipo in equipos:
        for piloto in equipo.pilotos:
            pilotos.append((piloto.nombre, piloto.puntaje_campeonato))
    
    # Ordenando
    for i in range (len(pilotos)):
        for j in range (i + 1, len(pilotos)):
            if pilotos[i][1] < pilotos[j][1]:
                pilotos[i], pilotos[j] = pilotos[j], pilotos[i]

    # Mostrar top 10
    for i in range (min(10,len(pilotos))):
        print(f'{pilotos[i][0]}: {pilotos[i][1]} puntos')

def resumen_constructores (equipos):
    for equipo in equipos:
        puntos_equipo = 0 
        for piloto in equipo.pilotos:
            puntos_equipo += piloto.puntaje_campeonato
        
        print (f'{equipo.nombre}: {puntos_equipo} puntos')

def top_pilotos_salario(equipos):
    pilotos = [piloto for equipo in equipos for piloto in equipo.pilotos]
    pilotos_ordenados = sorted(pilotos, key=lambda p: p.salario, reverse=True)[:5]
    for piloto in pilotos_ordenados:
        print(f"{piloto.nombre}: {piloto.salario}")

def top_pilotos_habilidosos(equipos):
    pilotos = [piloto for equipo in equipos for piloto in equipo.pilotos]
    pilotos_ordenados = sorted(pilotos, key=lambda p: p.score, reverse=True)[:3]
    for piloto in pilotos_ordenados:
        print(f"{piloto.nombre}: {piloto.score} habilidad")

def jefes_equipo(equipos):
    jefes = [(equipo.director.nombre, equipo.nombre) for equipo in equipos if equipo.director]
    jefes_ordenados = sorted(jefes, key=lambda j: j[0])
    for jefe, equipo in jefes_ordenados:
        print(f"{jefe} - {equipo}")





def main():
    empleados = {}
    autos = {}
    equipos = []






    # Crear y añadir el auto
    auto_prueba = Auto("Modelo2023", 2023, 90)
    autos[auto_prueba.modelo] = auto_prueba
    # Crear y añadir los pilotos y el jefe de equipo
    empleados["12345678"] = Piloto("12345678", "Piloto Uno", "01/01/1990", "Nacionalidad1", 100000, 95, 1, 0, False, True)
    empleados["87654321"] = Piloto("87654321", "Piloto Dos", "02/02/1992", "Nacionalidad2", 95000, 92, 2, 0, True, True)
    empleados["11223344"] = Piloto("11223344", "Piloto Reserva", "03/03/1993", "Nacionalidad3", 90000, 90, 3, 0, False, False)
    empleados["44332211"] = Director("44332211", "Jefe Uno", "04/04/1980", "Nacionalidad4", 120000)
    # Crear y añadir los mecánicos
    for i in range(1, 9):
        cedula = f"1111{str(i).zfill(4)}"
        nombre = f"Mecanico {i}"
        fecha_nac = f"0{i}/0{i}/198{i}"
        nacionalidad = f"Nacionalidad{i+4}"
        salario = 50000 + i * 2000
        score = 85 + i
        empleados[cedula] = Mecanico(cedula, nombre, fecha_nac, nacionalidad, salario, score)
    # Crear y añadir el equipo
    equipo_prueba = Equipo("Equipo Prueba")
    equipo_prueba.asignar_auto(autos["Modelo2023"])
    equipo_prueba.asignar_director(empleados["44332211"])
    for cedula in ["12345678", "87654321", "11223344"]:
        equipo_prueba.agregar_piloto(empleados[cedula])
    for i in range(1, 9):
        cedula = f"1111{str(i).zfill(4)}"
        equipo_prueba.agregar_mecanico(empleados[cedula])
    equipos.append(equipo_prueba)

            
            
            # Continuación de tu código existente...

# Crear y añadir más autos
    autos["Modelo2024"] = Auto("Modelo2024", 2024, 88)
    autos["Modelo2025"] = Auto("Modelo2025", 2025, 92)
    autos["Modelo2026"] = Auto("Modelo2026", 2026, 95)

# Crear y añadir más pilotos, directores y mecánicos
# Equipo 2
    empleados["22334455"] = Piloto("22334455", "Piloto Tres", "05/05/1991", "Nacionalidad5", 98000, 93, 4, 0, False, True)
    empleados["55667788"] = Piloto("55667788", "Piloto Cuatro", "06/06/1994", "Nacionalidad6", 96000, 91, 5, 0, False, True)
    empleados["88990011"] = Piloto("88990011", "Piloto Reserva 2", "07/07/1995", "Nacionalidad7", 88000, 89, 6, 0, False, False)
    empleados["11224433"] = Director("11224433", "Jefe Dos", "08/08/1981", "Nacionalidad8", 115000)

    # Equipo 3
    empleados["33445566"] = Piloto("33445566", "Piloto Cinco", "09/09/1992", "Nacionalidad9", 97000, 94, 7, 0, True, True)
    empleados["66778899"] = Piloto("66778899", "Piloto Seis", "10/10/1996", "Nacionalidad10", 95000, 90, 8, 0, False, True)
    empleados["99001122"] = Piloto("99001122", "Piloto Reserva 3", "11/11/1997", "Nacionalidad11", 87000, 88, 9, 0, False, False)
    empleados["22446688"] = Director("22446688", "Jefe Tres", "12/12/1982", "Nacionalidad12", 110000)

    # Equipo 4
    empleados["77889900"] = Piloto("77889900", "Piloto Siete", "13/13/1993", "Nacionalidad13", 99000, 99, 10, 0, False, True)
    empleados["00112233"] = Piloto("00112233", "Piloto Ocho", "14/14/1998", "Nacionalidad14", 94000, 89, 11, 0, True, True)
    empleados["44556677"] = Piloto("44556677", "Piloto Reserva 4", "15/15/1999", "Nacionalidad15", 86000, 87, 12, 0, False, False)
    empleados["33669900"] = Director("33669900", "Jefe Cuatro", "16/16/1983", "Nacionalidad16", 105000)

    # Añadir más mecánicos
    for i in range(9, 17):
        cedula = f"2222{str(i).zfill(4)}"
        nombre = f"Mecanico {i}"
        fecha_nac = f"2{i}/2{i}/19{i}"
        nacionalidad = f"Nacionalidad{i+8}"
        salario = 48000 + i * 2000
        score = 80 + i
        empleados[cedula] = Mecanico(cedula, nombre, fecha_nac, nacionalidad, salario, score)

    # Crear y añadir más equipos
    # Equipo 2
    equipo2 = Equipo("Equipo Prueba 2")
    equipo2.asignar_auto(autos["Modelo2024"])
    equipo2.asignar_director(empleados["11224433"])
    for cedula in ["22334455", "55667788", "88990011"]:
        equipo2.agregar_piloto(empleados[cedula])
    for i in range(9, 17):
        cedula = f"2222{str(i).zfill(4)}"
        equipo2.agregar_mecanico(empleados[cedula])
    equipos.append(equipo2)

    # Equipo 3
    equipo3 = Equipo("Equipo Prueba 3")
    equipo3.asignar_auto(autos["Modelo2025"])
    equipo3.asignar_director(empleados["22446688"])
    for cedula in ["33445566", "66778899", "99001122"]:
        equipo3.agregar_piloto(empleados[cedula])
    for i in range(9, 17):
        cedula = f"2222{str(i).zfill(4)}"
        equipo3.agregar_mecanico(empleados[cedula])
    equipos.append(equipo3)

    # Equipo 4
    equipo4 = Equipo("Equipo Prueba 4")
    equipo4.asignar_auto(autos["Modelo2026"])
    equipo4.asignar_director(empleados["33669900"])
    for cedula in ["77889900", "00112233", "44556677"]:
        equipo4.agregar_piloto(empleados[cedula])
    for i in range(9, 17):
        cedula = f"2222{str(i).zfill(4)}"
        equipo4.agregar_mecanico(empleados[cedula])
    equipos.append(equipo4)

    # Continuación de tu método main()...

            
            

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
            print("Realizar consultas (Función aún no implementada).")
        elif opcion_usuario == 6:
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")



if __name__ == "__main__":
    main()
    

