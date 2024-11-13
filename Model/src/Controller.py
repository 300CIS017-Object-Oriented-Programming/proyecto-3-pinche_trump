
class Controller:

    def __init__(self):
        self.nombre = " "
        self.dict2 = {}
        self.lista1 = []

    def saludar(self, name):
        self.nombre = name
        self.lista1.append(name)
        print(f"{self.nombre} saludos {self.nombre}")
