'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.'''

class User:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = []
        self.posts = []

    def adicionar_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)
            print(f"{amigo.nome} foi adicionado como amigo de {self.nome}.")
        else:
            print(f"{amigo.nome} já é amigo de {self.nome}.")

    def publicar_mensagem(self, mensagem):
        self.posts.append(mensagem)
        print(f"{self.nome} publicou: {mensagem}")

    def comentar_post(self, post, comentario):
        if post in self.posts:
            post.adicionar_comentario(comentario)
            print(f"{self.nome} comentou: {comentario}")
        else:
            print("Post não encontrado.")

class Post:
    def __init__(self, usuario, mensagem):
        self.usuario = usuario
        self.mensagem = mensagem
        self.comentarios = []

    def adicionar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def __str__(self):
        return f"{self.usuario.nome}: {self.mensagem} (Comentários: {len(self.comentarios)})"

class SocialNetwork:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome):
        usuario = User(nome)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} adicionado à rede social.\n")

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                print(f"Usuario {nome} encontrado!\n")
                return usuario
        print(f"Usuário {nome} não encontrado.\n")
        return None

    def publicar_post(self, nome_usuario, mensagem):
        usuario = self.buscar_usuario(nome_usuario)
        if usuario:
            post = Post(usuario, mensagem)
            usuario.publicar_mensagem(post)
            print("Post realizado com sucesso!\n")

def main():
    rede_social = SocialNetwork()
    print("-="*30)
    while True:
        print("Menu:")
        print("1. Adicionar Usuário")
        print("2. Buscar Usuário")
        print("3. Publicar Post")
        print("4. Adicionar Amigo")
        print("5. Comentar em Post")
        print("6. Sair")

        escolha = input("\nEscolha uma opção: ")
        print()

        if escolha == '1':
            nome = input("Digite o nome do usuário: ")
            rede_social.adicionar_usuario(nome)
        elif escolha == '2':
            nome = input("Digite o nome do usuário a ser buscado: ")
            rede_social.buscar_usuario(nome)
        elif escolha == '3':
            nome_usuario = input("Digite o nome do usuário que publicará: ")
            mensagem = input("Digite a mensagem do post: ")
            rede_social.publicar_post(nome_usuario, mensagem)
        elif escolha == '4':
            nome_usuario = input("Digite o nome do usuário: ")
            nome_amigo = input("Digite o nome do amigo a ser adicionado: ")
            usuario = rede_social.buscar_usuario(nome_usuario)
            amigo = rede_social.buscar_usuario(nome_amigo)
            if usuario and amigo:
                usuario.adicionar_amigo(amigo)
        elif escolha == '5':
            nome_usuario = input("Digite o nome do usuário que comentou: ")
            mensagem = input("Digite a mensagem do post: ")
            comentario = input("Digite seu comentário: ")
            usuario = rede_social.buscar_usuario(nome_usuario)
            post = usuario.buscar_post(mensagem) if usuario else None
            if post:
                usuario.comentar_post(post, comentario)
        elif escolha == '6':
            print("Saindo da rede social. Até logo!")
            print("-="*30)
            break
        else:
            print("Opção inválida! Tente novamente.")
    
main()