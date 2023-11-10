





class Error (Exception):
    pass


class Empleado:
    def __init__(self, id_empleado, nombre, fecha_nacimiento, nacionalidad, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.salario = salario




    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, value):
        if len(value) != 8:
            raise Error("El ID del empleado debe tener exactamente 8 dígitos.")

        for i in value:
            if i < '0' or i > '9':
                raise Error("El ID del empleado debe contener solo números del 0 al 9.")
        
        self._id_empleado = value




    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value:  
            raise Error("El nombre no puede estar vacío.")
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
                raise Error("Fecha de nacimiento debe estar en formato DD/MM/AAAA y ser válida.")
            self._fecha_nacimiento = value
        else:
            raise Error("Fecha de nacimiento debe estar en formato DD/MM/AAAA.")
        



    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, value):
        if not value:
            raise Error("La nacionalidad no puede estar vacía.")
        self._nacionalidad = value



    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        if type(value) not in [int, float] or value <= 0:
            raise Error("El salario debe ser un número positivo.")
        self._salario = value





class Piloto(Empleado):
    def __init__(self, id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto):
        super().__init__(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
        self.numero_auto = numero_auto
        self.puntaje_campeonato = 0
        self.lesionado = False






    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if 1 <= value <= 99:
            self._score = value
        else:
            raise Error("El score debe ser un número entero entre 1 y 99.")






    @property
    def numero_auto(self):
        return self._numero_auto

    @numero_auto.setter
    def numero_auto(self, value):
        value_str = str(value)
        for char in value_str:
            if char not in '0123456789':
                raise Error("El número de auto debe ser un número entero positivo.")

        # Si todos los caracteres son dígitos, convertir a entero y verificar si es positivo

        numero = int(value_str)
        if numero <= 0:
            raise Error("El número de auto debe ser un número entero positivo.")

        self._numero_auto = numero


class DirectorEquipo(Empleado):
    # No additional attributes for now
    pass



class Mecanico(Empleado):
    def __init__(self, id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        score_int = int(value)
        if score_int < 1 or score_int > 99:
            raise Error("El score debe ser un número entero entre 1 y 99.")
        self._score = score_int


class Modelo_Auto:
    def __init__(self, modelo, anio, score):
        self.modelo = modelo
        self.anio = anio
        self.score = score

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        if not value or type(value) is not str:
            raise Error("El modelo debe ser una cadena no vacía.")
        self._modelo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        try:
            anio_int = int(value)
            if anio_int < 1885 or anio_int > 2023:  # Rango de años válido
                raise Error("El año debe ser un entero que represente un año válido de fabricación de autos.")
            self._anio = anio_int
        except ValueError:
            raise Error("El año debe ser un número entero válido.")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        try:
            score_int = int(value)
            if score_int < 1 or score_int > 99:  # Rango de score válido
                raise Error("El score debe ser un número entero entre 1 y 99.")
            self._score = score_int
        except ValueError:
            raise Error("El score debe ser un número entero válido.")
        











        




       


    