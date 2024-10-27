from abc import ABC, abstractmethod

class PostBase(ABC):
    def __init__(self, conteudo, autor):
        self.conteudo = conteudo
        self.autor = autor
        self.comentarios = []

    @abstractmethod
    def mostrar_post(self):
        pass

    def adicionar_comentario(self, usuario, comentario):
        self.comentarios.append((usuario, comentario))

class PostTexto(PostBase):
    def __init__(self, conteudo, autor):
        super().__init__(conteudo, autor)

    def mostrar_post(self):
        print(f"\nPost de {self.autor.nome}: {self.conteudo}")

class PostImagem(PostBase):
    def __init__(self, conteudo, autor, imagem):
        super().__init__(conteudo, autor)
        self.imagem = imagem

    def mostrar_post(self):
        super().mostrar_post()
        print(f"Imagem: {self.imagem}")

class PostFactory:
    @staticmethod
    def criar_post(tipo_post, conteudo, autor, midia=None):
        if tipo_post == '1':
            return PostTexto(conteudo, autor)
        elif tipo_post == '2':
            return PostImagem(conteudo, autor, midia)
        else:
            raise ValueError("Tipo de post inválido.")