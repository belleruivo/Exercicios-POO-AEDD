'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.'''

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.amigos = []
        self.posts = []

    def adicionar_amigo(self, amigo):
        if amigo == self:  # Verifica se o usuário está tentando adicionar a si mesmo
            print("Você não pode adicionar a si mesmo como amigo.\n")
            return
        
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

    def adicionar_usuario(self, nome, email):
        if any(usuario.email == email for usuario in self.usuarios):
            print(f"Já existe um usuário cadastrado com o email {email}.\n")
            return None

        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} ({email}) foi adicionado à rede.\n")
        return usuario

    def buscar_usuario_por_numero(self, numero):
        if 0 <= numero < len(self.usuarios):
            return self.usuarios[numero]
        print("Número de usuário inválido.\n")
        return None

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.\n")
            return
        print("Usuários cadastrados:")
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario.nome} ({usuario.email})")
        print()  # Adiciona uma nova linha após a lista

    def listar_posts(self, usuario):
        if not usuario.posts:
            print(f"{usuario.nome} não tem posts.\n")
            return
        print(f"Posts de {usuario.nome}:")
        for i, post in enumerate(usuario.posts, start=1):
            print(f"{i}. {post.conteudo}")
        print()  # Adiciona uma nova linha após a lista


def menu():
    rede = SocialNetwork()
    print("-=" * 30)
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
            email = input("Email do usuário: ")
            rede.adicionar_usuario(nome, email)

        elif escolha == '2':
            rede.listar_usuarios()  # Exibir lista de usuários
            try:
                num1 = int(input("\nNúmero do usuário que vai adicionar um amigo: ")) - 1
                num2 = int(input("Número do amigo a ser adicionado: ")) - 1
                usuario1 = rede.buscar_usuario_por_numero(num1)
                usuario2 = rede.buscar_usuario_por_numero(num2)
                if usuario1 and usuario2:
                    usuario1.adicionar_amigo(usuario2)
            except ValueError:
                print("Entrada inválida. Por favor, insira números.\n")

        elif escolha == '3':
            rede.listar_usuarios()  # Exibir lista de usuários
            try:
                num = int(input("\nNúmero do usuário que vai publicar: ")) - 1
                usuario = rede.buscar_usuario_por_numero(num)
                if usuario:
                    conteudo = input("Escreva o conteúdo do post: ")
                    usuario.publicar_post(conteudo)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.\n")

        elif escolha == '4':
            rede.listar_usuarios()  # Exibir lista de usuários
            try:
                num = int(input("\nNúmero do usuário que vai comentar: ")) - 1
                usuario = rede.buscar_usuario_por_numero(num)
                if usuario:
                    # Exibir posts dos amigos
                    print("Posts dos amigos:")
                    for amigo in usuario.amigos:
                        rede.listar_posts(amigo)

                    if not usuario.amigos or not any(amigo.posts for amigo in usuario.amigos):
                        print("Você não tem amigos com posts.\n")
                        continue

                    autor_post_num = int(input("Número do autor do post que você deseja comentar: ")) - 1
                    usuario_autor = rede.buscar_usuario_por_numero(autor_post_num)
                    if usuario_autor:
                        rede.listar_posts(usuario_autor)
                        try:
                            num_post = int(input("\nNúmero do post para comentar: ")) - 1
                            if 0 <= num_post < len(usuario_autor.posts):
                                comentario = input("Escreva seu comentário: ")
                                usuario.comentar_post(usuario_autor.posts[num_post], comentario)
                            else:
                                print("Número de post inválido.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número.\n")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.\n")

        elif escolha == '5':
            rede.listar_usuarios()  # Exibir lista de usuários
            try:
                num = int(input("\nNúmero do usuário para buscar: ")) - 1
                usuario = rede.buscar_usuario_por_numero(num)
                if usuario:
                    print(f"Usuário encontrado: {usuario.nome} ({usuario.email})\n")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.\n")

        elif escolha == '6':
            print("\nSaindo...")
            print("-=" * 30)
            break

        else:
            print("Opção inválida, tente novamente.\n")


menu()