'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.'''

class User:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = []

    def adicionar_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)
            amigo.amigos.append(self)  
            print(f"{amigo.nome} foi adicionado como amigo de {self.nome}.\n")
        else:
            print(f"{amigo.nome} já é amigo de {self.nome}.")

class Post:
    def __init__(self, usuario, mensagem):
        self.usuario = usuario
        self.mensagem = mensagem
        self.comentarios = []

    def adicionar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def __str__(self):
        return f"{self.mensagem} (Publicado por: {self.usuario.nome}, Comentários: {len(self.comentarios)})"

class SocialNetwork:
    def __init__(self):
        self.usuarios = []
        self.posts = []  # Armazena todos os posts

    def adicionar_usuario(self, nome):
        usuario = User(nome)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} adicionado à rede social.\n")

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                print(f"Usuário {nome} encontrado!\n")
                return usuario
        print(f"Usuário {nome} não encontrado.\n")
        return None

    def publicar_post(self, nome_usuario, mensagem):
        usuario = self.buscar_usuario(nome_usuario)
        if usuario:
            post = Post(usuario, mensagem)
            self.posts.append(post)  # Adiciona o post à lista global de posts
            print("Post realizado com sucesso!\n")

    def listar_posts(self):
        if not self.posts:
            print("Nenhum post disponível.")
        else:
            print("Posts disponíveis:")
            for post in self.posts:
                print(post)

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
        print("6. Listar Posts")
        print("7. Sair")

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
            nome_usuario = input("Digite o nome do usuário que vai comentar: ")
            usuario = rede_social.buscar_usuario(nome_usuario)
            if usuario:
                rede_social.listar_posts()  # Lista todos os posts disponíveis
                mensagem = input("Digite a mensagem do post que deseja comentar: ")
                comentario = input("Digite seu comentário: ")
                post = next((p for p in rede_social.posts if p.mensagem.lower() == mensagem.lower()), None)
                if post:
                    post.adicionar_comentario(comentario)
                    print(f"{nome_usuario} comentou: {comentario}\n")
                else:
                    print("Post não encontrado.")
        elif escolha == '7':
            print("Saindo da rede social. Até logo!")
            print("-="*30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")

main()
'''
class User:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = []

    def adicionar_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)
            amigo.amigos.append(self)  
            print(f"{amigo.nome} foi adicionado como amigo de {self.nome}.\n")
        else:
            print(f"{amigo.nome} já é amigo de {self.nome}.")

class Post:
    def __init__(self, usuario, mensagem):
        self.usuario = usuario
        self.mensagem = mensagem
        self.comentarios = []

    def adicionar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def __str__(self):
        return f"{self.mensagem} (Publicado por: {self.usuario.nome}, Comentários: {len(self.comentarios)})"

class SocialNetwork:
    def __init__(self):
        self.usuarios = []
        self.posts = []  

    def adicionar_usuario(self, nome):
        usuario = User(nome)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} adicionado à rede social.\n")

    def buscar_usuario(self, nome, escolha=None):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                if escolha == "2":
                    print(f"Usuário {nome} encontrado!\n")
                return usuario
        print(f"Usuário {nome} não encontrado.\n")
        return None

    def publicar_post(self, nome_usuario, mensagem):
        usuario = self.buscar_usuario(nome_usuario)
        if usuario:
            post = Post(usuario, mensagem)
            self.posts.append(post)  
            print("Post realizado com sucesso!\n")

    def listar_posts(self):
        if not self.posts:
            print("Nenhum post disponível.")
        else:
            print("Posts disponíveis:")
            for post in self.posts:
                print(post)

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
            nome_usuario = input("Digite o nome do usuário que vai comentar: ")
            usuario = rede_social.buscar_usuario(nome_usuario)
            if usuario:
                rede_social.listar_posts()  # Lista todos os posts disponíveis
                mensagem = input("Digite a mensagem do post que deseja comentar: ")
                comentario = input("Digite seu comentário: ")
                post = next((p for p in rede_social.posts if p.mensagem.lower() == mensagem.lower()), None)
                if post:
                    post.adicionar_comentario(comentario)
                    print(f"{nome_usuario} comentou: {comentario}\n")
                else:
                    print("Post não encontrado.")
        elif escolha == '6':
            print("Saindo da rede social. Até logo!")
            print("-="*30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")

main()
'''