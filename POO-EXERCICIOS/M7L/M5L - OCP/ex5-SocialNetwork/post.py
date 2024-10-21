class PostBase:
    def __init__(self, conteudo, autor):
        self.conteudo = conteudo
        self.autor = autor
        self.comentarios = []

    def adicionar_comentario(self, usuario, comentario):
        self.comentarios.append((usuario, comentario))

    def mostrar_post(self):
        print(f"Post de {self.autor.nome}: {self.conteudo}")
        if self.comentarios:
            print("Comentários:")
            for comentario in self.comentarios:
                print(f"   {comentario[0].nome} comentou: {comentario[1]}")


class PostImagem(PostBase):
    def __init__(self, conteudo, autor, imagem):
        super().__init__(conteudo, autor)
        self.imagem = imagem

    def mostrar_post(self):
        super().mostrar_post()
        print(f"Imagem: {self.imagem}")


class PostVideo(PostBase):
    def __init__(self, conteudo, autor, video):
        super().__init__(conteudo, autor)
        self.video = video

    def mostrar_post(self):
        super().mostrar_post()
        print(f"Vídeo: {self.video}")


class PostFactory:
    @staticmethod
    def criar_post(tipo_post, conteudo, autor, midia=None):
        if tipo_post == '1':
            return PostBase(conteudo, autor)
        elif tipo_post == '2':
            return PostImagem(conteudo, autor, midia)
        elif tipo_post == '3':
            return PostVideo(conteudo, autor, midia)
        else:
            raise ValueError("Tipo de post inválido.")