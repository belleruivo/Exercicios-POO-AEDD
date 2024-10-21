class UsuarioBase:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.amigos = []
        self.posts = []

    def adicionar_amigo(self, amigo):
        if amigo == self:
            print("Você não pode adicionar a si mesmo como amigo.")
            return

        if amigo not in self.amigos:
            self.amigos.append(amigo)
            amigo.amigos.append(self)
            print(f"{amigo.nome} agora é amigo(a) de {self.nome}.")
        else:
            print(f"{amigo.nome} já é seu amigo.")

    def publicar_post(self, post):
        self.posts.append(post)
        print(f"{self.nome} publicou: {post.conteudo}")

    def comentar_post(self, post, comentario):
        post.adicionar_comentario(self, comentario)
        print(f"{self.nome} comentou no post de {post.autor.nome}: {comentario}")

    def __str__(self):
        return self.nome
