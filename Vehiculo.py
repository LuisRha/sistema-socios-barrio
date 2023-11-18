class Vehiculo:
    def __init__(self, tipo, marca, color, año):
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.año = año

    def obtener_informacion_vehiculo(self):
        return f"Tipo: {self.tipo}\nMarca: {self.marca}\nColor: {self.color}\nAño: {self.año}"

    def mostrar_informacion(self):
        return f"Vehiculo: {self.obtener_informacion_vehiculo()}"

class Moto(Vehiculo):
    def __init__(self, tipo, marca, color, año, estacionado):
        super().__init__(tipo, marca, color, año)
        self.estacionado = estacionado

    def obtener_informacion_vehiculo(self):
        return f"{super().obtener_informacion_vehiculo()}\nEstacionado: {self.estacionado}"

    def mostrar_informacion(self):
        return f"Vehiculo: {self.obtener_informacion_vehiculo()}"

class Bus(Vehiculo):
    def __init__(self, tipo, marca, color, año, estacionado):
        super().__init__(tipo, marca, color, año)
        self.estacionado = estacionado

    def obtener_informacion_vehiculo(self):
        return f"{super().obtener_informacion_vehiculo()}\nEstacionado: {self.estacionado}"

    def mostrar_informacion(self):
        return f"Vehiculo: {self.obtener_informacion_vehiculo()}"

# Ejemplo de uso
vehiculo1 = Vehiculo("Automóvil", "Chevrolet", "Rojo", "2020")
vehiculo2 = Moto("Motocicleta", "Honda", "Negro", "2021", "Sí")
vehiculo3 = Bus("Autobús", "Mercedes", "Azul", "2019", "No")

motor = [vehiculo1, vehiculo2, vehiculo3]

for vehiculo in motor:
    print(vehiculo.mostrar_informacion())
    print("=" * 30)
