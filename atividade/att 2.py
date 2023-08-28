class Forma:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

class Retangulo(Forma):
    def calcular_area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def calcular_area(self):
        return (self.largura * self.altura) / 2

# Exemplo de uso:
retangulo = Retangulo(5, 4)
triangulo = Triangulo(6, 3)

area_retangulo = retangulo.calcular_area()
area_triangulo = triangulo.calcular_area()

print(f"Área do retângulo: {area_retangulo}")
print(f"Área do triângulo: {area_triangulo}")
