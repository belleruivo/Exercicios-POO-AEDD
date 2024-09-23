'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.'''

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = []
        self.posts = []

    def adicionar_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)
            amigo.amigos.append(self)
            print(f"{amigo.nome} agora é amigo(a) de {self.nome}.\n")
        else:
            print(f"{amigo.nome} já é seu amigo.\n")

    def publicar_post(self, conteudo):
        post = Post(conteudo, self)
        self.posts.append(post)
        print(f"{self.nome} publicou: {conteudo}\n")
        return post

    def comentar_post(self, post, comentario):
        post.adicionar_comentario(self, comentario)
        print(f"{self.nome} comentou no post de {post.autor.nome}: {comentario}\n")

    def __str__(self):
        return self.nome


class Post:
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


class SocialNetwork:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome):
        usuario = Usuario(nome)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} foi adicionado à rede.\n")
        return usuario

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome == nome:
                return usuario
        print(f"Usuário {nome} não encontrado.\n")
        return None
    

def menu():
    rede = SocialNetwork()
    print("-="*30)
    while True:
        print("MENU:")
        print("1. Adicionar Usuário")
        print("2. Adicionar Amigo")
        print("3. Publicar Post")
        print("4. Comentar em Post")
        print("5. Buscar Usuário")
        print("6. Sair")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            nome = input("\nNome do usuário: ")
            rede.adicionar_usuario(nome)

        elif escolha == '2':
            nome1 = input("\nNome do usuário que vai adicionar um amigo: ")
            nome2 = input("Nome do amigo a ser adicionado: ")
            usuario1 = rede.buscar_usuario(nome1)
            usuario2 = rede.buscar_usuario(nome2)
            if usuario1 and usuario2:
                usuario1.adicionar_amigo(usuario2)

        elif escolha == '3':
            nome = input("\nNome do usuário que vai publicar: ")
            usuario = rede.buscar_usuario(nome)
            if usuario:
                conteudo = input("Escreva o conteúdo do post: ")
                usuario.publicar_post(conteudo)

        elif escolha == '4':
            nome = input("Nome do usuário que vai comentar: ")
            usuario = rede.buscar_usuario(nome)
            if usuario:
                autor_post = input("Nome do autor do post: ")
                usuario_autor = rede.buscar_usuario(autor_post)
                if usuario_autor:
                    if usuario_autor.posts:
                        for i, post in enumerate(usuario_autor.posts):
                            print(f"Post {i+1}: {post.conteudo}")
                        num_post = int(input("\nNúmero do post para comentar: ")) - 1
                        if 0 <= num_post < len(usuario_autor.posts):
                            comentario = input("Escreva seu comentário: ")
                            usuario.comentar_post(usuario_autor.posts[num_post], comentario)
                        else:
                            print("Número de post inválido.")
                    else:
                        print(f"{usuario_autor.nome} não tem posts para comentar.\n")

        elif escolha == '5':
            nome = input("\nNome do usuário para buscar: ")
            usuario = rede.buscar_usuario(nome)
            if usuario:
                print(f"Usuário encontrado: {usuario.nome}\n")

        elif escolha == '6':
            print("\nSaindo...")
            print("-="*30)
            break

        else:
            print("Opção inválida, tente novamente.\n")


menu()