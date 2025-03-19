from superclase.vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, marca, modelo, tipo):
        super().__init__(color, ruedas)
        self.marca=marca
        self.modelo=modelo
        self.tipo=tipo
    def __str__(self):
        return "color {}, {} ruedas, {} {}, {}".format(self.color, self.ruedas, self.marca, self.modelo, self.tipo)
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")
    def arrancar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está lista para rodar.")
    def frenar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está frenando.")        