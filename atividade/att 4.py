class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

# Exemplo de uso:
carro = Carro("Toyota", "Corolla", 2022, 4)
moto = Moto("Honda", "CBR600RR", 2021, 600)

print(f"Carro: Marca = {carro.marca}, Modelo = {carro.modelo}, Ano = {carro.ano}, Número de Portas = {carro.num_portas}")
print(f"Moto: Marca = {moto.marca}, Modelo = {moto.modelo}, Ano = {moto.ano}, Cilindradas = {moto.cilindradas}")
