class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem

# Exemplo de uso:
livro = Livro("Dom Casmurro", 29.99, "Machado de Assis")
eletronico = Eletronico("Smartphone", 799.99, "110V")

print(f"Produto: {livro.nome}, Preço: R${livro.preco}, Autor: {livro.autor}")
print(f"Produto: {eletronico.nome}, Preço: R${eletronico.preco}, Voltagem: {eletronico.voltagem}")
