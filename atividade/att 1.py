class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

# Exemplo de uso:
pessoa1 = Pessoa("João", 25)
aluno1 = Aluno("Maria", 20, "12345")

print(f"Pessoa: Nome = {pessoa1.nome}, Idade = {pessoa1.idade}")
print(f"Aluno: Nome = {aluno1.nome}, Idade = {aluno1.idade}, Matrícula = {aluno1.matricula}")
