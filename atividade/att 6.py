class Bebida:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Refrigerante(Bebida):
    def __init__(self, espuma, nome):
        super().__init__(self, nome, 'Refrigerante')
        self.espuma = espuma

class Cafe(Bebida):
    def __init__(self, cafeina, nome):
        super().__init__(self, nome, 'Café')
        self.cafeina = cafeina
