class Estudante:
    def __init__(self, codigo, nome, idade, altura, media):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.media = media

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Média: {self.media}"