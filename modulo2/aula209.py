class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def pessoa_com_cinquenta(cls, nome):
        return cls(nome, 50)   

Pessoa.metodo_de_classe()
p2 = Pessoa.pessoa_com_cinquenta('Jonny')

print(p2.idade)